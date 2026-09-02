# =============================================================================
# build_vs3.py - Construcción de [VO(8-hidroxiquinolinato)2] (VS3)
# =============================================================================
# Objetivo: Generar un archivo .pdbqt de un complejo de oxovanadio(IV) con 
# dos ligandos 8-hidroxiquinolina, diseñado específicamente para atacar 
# el bolsillo ATP de BRAF V600E mediante apilamiento aromático (mimetismo de adenina).
# 
# Autor: Basado en pipeline de VS2 (deferiprona)
# Fecha: 2026-07-31
# =============================================================================

import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
import sys
import os

# -----------------------------------------------------------------------------
# 1. FUNCIÓN DE ALINEAMIENTO KABSCH (para posicionar los ligandos)
# -----------------------------------------------------------------------------
# Esta función toma dos conjuntos de puntos (coordenadas atómicas).
# Calcula la rotación y traslación óptimas para que el primer conjunto
# se superponga al segundo (mínimos cuadrados).
# La usaremos para colocar el ligando (generado por RDKit) exactamente
# donde queremos alrededor del vanadio.
# -----------------------------------------------------------------------------
def kabsch_align(coords, target_coords):
    """
    Alinea 'coords' a 'target_coords' usando el algoritmo de Kabsch.
    coords: array Nx3 (puntos a mover)
    target_coords: array Nx3 (puntos objetivo)
    Retorna: array Nx3 (coords alineadas)
    """
    # 1. Centrar los conjuntos de puntos restando sus centroides
    centroid = np.mean(coords, axis=0)
    target_centroid = np.mean(target_coords, axis=0)
    P = coords - centroid
    Q = target_coords - target_centroid
    
    # 2. Calcular la matriz de covarianza H
    H = P.T @ Q
    
    # 3. Descomposición en valores singulares (SVD)
    U, S, Vt = np.linalg.svd(H)
    
    # 4. Calcular la matriz de rotación R
    R = Vt.T @ U.T
    
    # 5. Corrección de reflexión (para evitar espejos)
    if np.linalg.det(R) < 0:
        Vt[-1, :] *= -1
        R = Vt.T @ U.T
    
    # 6. Aplicar rotación y traslación
    aligned_coords = (coords - centroid) @ R + target_centroid
    return aligned_coords


# -----------------------------------------------------------------------------
# 2. GENERAR LA GEOMETRÍA DEL LIGANDO (8-hidroxiquinolina) CON RDKit
# -----------------------------------------------------------------------------
# La 8-hidroxiquinolina (también llamada oxina) tiene un grupo OH fenólico
# y un N en el anillo piridínico. Al coordinar al V, el OH se desprotona
# (pierde el H) y se une como O-fenolato. El N también coordina.
# El SMILES canónico es: "Oc1cccc2ncccc12" (el OH está en la posición 8).
# -----------------------------------------------------------------------------

print("1. Generando ligando 8-hidroxiquinolina con RDKit...")

# SMILES de la 8-hidroxiquinolina (desprotonada en el OH, aunque RDKit la pondrá con H)
smi = "Oc1cccc2ncccc12"
mol = Chem.MolFromSmiles(smi)
mol = Chem.AddHs(mol)  # Añadimos hidrógenos explícitos para la optimización

# Generar una geometría 3D inicial y optimizarla con el campo de fuerza MMFF
AllChem.EmbedMolecule(mol, randomSeed=42)
AllChem.MMFFOptimizeMolecule(mol)

# Calcular cargas Gasteiger (las usaremos de base, aunque luego las ajustaremos)
AllChem.ComputeGasteigerCharges(mol)

# Extraer las coordenadas de todos los átomos (en forma de lista de listas)
conf = mol.GetConformer()
lig_coords = np.array([conf.GetAtomPosition(i) for i in range(mol.GetNumAtoms())])

# Identificar el O del fenolato (OH) y el N de la piridina
# Buscamos el primer átomo de Oxígeno y el primer átomo de Nitrógeno.
# En la 8-hidroxiquinolina, son fáciles de identificar.
oxygen_idx = None
nitrogen_idx = None
for atom in mol.GetAtoms():
    if atom.GetAtomicNum() == 8 and oxygen_idx is None:
        oxygen_idx = atom.GetIdx()
    if atom.GetAtomicNum() == 7 and nitrogen_idx is None:
        nitrogen_idx = atom.GetIdx()

print(f"   Átomo de O encontrado en índice: {oxygen_idx}")
print(f"   Átomo de N encontrado en índice: {nitrogen_idx}")

if oxygen_idx is None or nitrogen_idx is None:
    print("Error: No se encontraron O o N en el ligando. Verifica el SMILES.")
    sys.exit(1)

# Guardamos las posiciones originales de los átomos donores (O y N) del ligando.
# Estos son los puntos que alinearemos al vanadio.
donor_atoms_coords = lig_coords[[oxygen_idx, nitrogen_idx]]

# -----------------------------------------------------------------------------
# 3. DEFINIR LA GEOMETRÍA OBJETIVO ALREDEDOR DEL VANADIO (PIRÁMIDE CUADRADA)
# -----------------------------------------------------------------------------
# El V(IV) tiene un oxo terminal (V=O) axial. La geometría es pirámide cuadrada.
# 
# Parámetros:
# - Distancia V=O (axial): 1.60 Å (típico para vanadilo)
# - Distancia V-O (ecuatorial, fenolato): 1.97 Å (típico para V(IV)-O)
# - Distancia V-N (ecuatorial, piridina): 2.10 Å (típico para V(IV)-N)
# - Ángulo de mordida (O-V-N) dentro del quelato: 82° (típico para 8-hidroxiquinolina)
# 
# Colocamos los dos ligandos en el plano XY.
# Ligando 1: O en ángulo 0°, N en ángulo 82°.
# Ligando 2: O en ángulo 180°, N en ángulo 262° (180+82).
# -----------------------------------------------------------------------------

print("2. Definición de la geometría objetivo...")

# Posición del vanadio (origen)
V_pos = np.array([0.0, 0.0, 0.0])

# Posición del oxo terminal (axial, sobre el eje Z)
oxo_pos = np.array([0.0, 0.0, 1.60])

# Radio de los donores ecuatoriales
r_O = 1.97
r_N = 2.10

# Ángulo de mordida en radianes (82°)
bite_angle = np.radians(82.0)

# Definir los 4 puntos donores objetivo en el plano XY
# Lista de tuplas: (ángulo en radianes, distancia, tipo)
donor_targets = []

# Ligando 1
ang_O1 = 0.0
ang_N1 = ang_O1 + bite_angle
donor_targets.append(('O1', ang_O1, r_O))
donor_targets.append(('N1', ang_N1, r_N))

# Ligando 2 (girado 180° para que quede opuesto)
ang_O2 = np.pi  # 180°
ang_N2 = ang_O2 + bite_angle
donor_targets.append(('O2', ang_O2, r_O))
donor_targets.append(('N2', ang_N2, r_N))

# Convertir de coordenadas polares (ángulo, radio) a cartesianas (x, y)
target_donors_coords = []
for label, ang, r in donor_targets:
    x = r * np.cos(ang)
    y = r * np.sin(ang)
    target_donors_coords.append([x, y, 0.0])  # z=0 porque están en el plano ecuatorial

target_donors_coords = np.array(target_donors_coords)

# -----------------------------------------------------------------------------
# 4. ALINEAR CADA LIGANDO A SU POSICIÓN MEDIANTE KABSCH
# -----------------------------------------------------------------------------
# Vamos a generar el complejo completo.
# Empezamos con el vanadio y el oxo.
# Luego, para cada ligando, tomamos sus coordenadas originales (generadas por RDKit),
# las alineamos de modo que sus átomos donores (O y N) caigan en las posiciones 
# objetivo definidas arriba.
# -----------------------------------------------------------------------------

print("3. Alineando ligandos al vanadio...")

# Inicializamos la lista de coordenadas de todo el complejo
# Empezamos con el Vanadio y el Oxo terminal
complex_coords = [V_pos, oxo_pos]
complex_atoms_info = [
    ('V', 'V', 0, 'Fe'),      # Tipo AutoDock "Fe" para V
    ('O', 'O1', 1, 'OA')      # Oxo terminal (aceptor)
]

# Desglosamos los donores objetivos en dos grupos: ligando 1 (dos primeros) y ligando 2 (dos últimos)
target_lig1 = target_donors_coords[0:2]  # O1 y N1
target_lig2 = target_donors_coords[2:4]  # O2 y N2

# Función para añadir un ligando
def add_ligand(lig_coords, oxygen_idx, nitrogen_idx, target_positions, offset_idx):
    """
    Alinea 'lig_coords' para que los átomos 'oxygen_idx' y 'nitrogen_idx'
    caigan en 'target_positions' (array 2x3).
    Retorna las coordenadas alineadas y los átomos.
    """
    # Puntos a alinear (los donores del ligando)
    donor_coords_lig = lig_coords[[oxygen_idx, nitrogen_idx]]
    
    # Aplicar Kabsch
    aligned_lig_coords = kabsch_align(lig_coords, target_positions)
    
    return aligned_lig_coords

# Alinear ligando 1
aligned_lig1 = add_ligand(lig_coords, oxygen_idx, nitrogen_idx, target_lig1, 2)

# Alinear ligando 2 (usamos la MISMA geometría de ligando, solo cambiamos el objetivo)
aligned_lig2 = add_ligand(lig_coords, oxygen_idx, nitrogen_idx, target_lig2, 2)

# Agregar los átomos del ligando 1 al complejo
for i, atom in enumerate(mol.GetAtoms()):
    pos = aligned_lig1[i]
    # Determinar el nombre del átomo (elemento + índice)
    elem = atom.GetSymbol()
    name = f"{elem}{i+1}"
    # Determinar el tipo AutoDock (AD4)
    # Carbono = 'C' (indistinto), Oxígeno = 'OA' o 'O'? Usamos 'OA' para aceptor, 'O' para no aceptor?
    # En AutoDock, 'OA' es oxígeno aceptor de puente de H. El fenolato es aceptor.
    # Nitrógeno = 'N' (no aceptor, ya que está en anillo y no tiene H, aunque puede aceptar H, 
    # pero en AD4 el tipo 'N' es para aminas alifáticas). En los grids de VS2 usamos 'N'.
    # Para este complejo, mejor usamos 'OA' para O fenolato y 'N' para N de anillo.
    if elem == 'O':
        ad_type = 'OA'
    elif elem == 'N':
        ad_type = 'N'
    elif elem == 'C':
        ad_type = 'C'
    else:
        ad_type = 'A'  # default
    complex_coords.append(pos)
    complex_atoms_info.append((elem, name, i+2, ad_type))

# Agregar los átomos del ligando 2 (los índices empiezan desde el total actual)
offset = len(complex_atoms_info)
for i, atom in enumerate(mol.GetAtoms()):
    pos = aligned_lig2[i]
    elem = atom.GetSymbol()
    name = f"{elem}{i+1+10}"  # nombre único
    if elem == 'O':
        ad_type = 'OA'
    elif elem == 'N':
        ad_type = 'N'
    elif elem == 'C':
        ad_type = 'C'
    else:
        ad_type = 'A'
    complex_coords.append(pos)
    complex_atoms_info.append((elem, name, i+offset, ad_type))

# -----------------------------------------------------------------------------
# 5. ASIGNACIÓN DE CARGAS (AJUSTADAS PARA QUE EL COMPLEJO SEA NEUTRO)
# -----------------------------------------------------------------------------
# El complejo real es neutro: V(IV) (carga +4) + 2 ligandos desprotonados (-1 c/u) + oxo (-2) = 0.
# Usamos cargas Gasteiger de RDKit como punto de partida para el ligando,
# pero luego ajustamos manualmente el V y el Oxo, y distribuimos uniformemente 
# la diferencia residual para que la suma total sea 0.
# -----------------------------------------------------------------------------

print("4. Asignando cargas...")

total_atoms = len(complex_coords)
charges = np.zeros(total_atoms)

# Obtener cargas Gasteiger de RDKit para el ligando (guardadas en la propiedad 'GasteigerCharge')
gasteiger_charges = []
for atom in mol.GetAtoms():
    charge = atom.GetDoubleProp('_GasteigerCharge')
    gasteiger_charges.append(charge)

# 1. Cargar las cargas Gasteiger para los átomos de los ligandos
# Ligando 1 (índices 2 a 2+N_lig-1)
lig_start_idx = 2
lig_end_idx = 2 + mol.GetNumAtoms()
for i in range(mol.GetNumAtoms()):
    charges[lig_start_idx + i] = gasteiger_charges[i]

# Ligando 2 (índices lig_end_idx a lig_end_idx + N_lig)
lig2_start = lig_end_idx
for i in range(mol.GetNumAtoms()):
    charges[lig2_start + i] = gasteiger_charges[i]

# 2. Carga del Vanadio: +0.60 (típico para parámetros AD4 en complejos de V, ya usado en la serie)
# NOTA: en realidad V(IV) es +4, pero en el modelo de carga parcial de AutoDock 
# se fracciona entre los ligandos. Mantenemos +0.60 como en monovanadato y decavanadato.
charges[0] = 0.60

# 3. Carga del Oxo terminal (V=O): -0.60 (para que sume 0 con el V)
charges[1] = -0.60

# 4. Calcular la carga total actual
total_charge = sum(charges)
print(f"   Carga total antes de ajuste: {total_charge:.4f}")

# 5. Ajuste fino: redistribuir la diferencia de forma uniforme entre todos los átomos
# para que el complejo sea neutro (carga neta 0). 
# Esto es una práctica común en AutoDock para evitar cargas no enteras que rompan el balance.
diff = -total_charge
adjustment = diff / total_atoms
charges += adjustment
print(f"   Ajuste aplicado: {adjustment:.6f} por átomo")

# Verificar que la suma sea ~0
print(f"   Carga total final: {sum(charges):.4f} (debe ser ~0)")

# -----------------------------------------------------------------------------
# 6. ESCRIBIR EL ARCHIVO PDBQT (formato estricto de AutoDock-GPU)
# -----------------------------------------------------------------------------
# El formato es crítico: columnas fijas.
# ATOM  serial  name resName chain resSeq x y z occupancy tempFactor charge type
# La cadena 'resName' debe ser 'VS3' y el residuo 1.
# Dos espacios entre serial y nombre para que 'LIG' caiga en la columna 18.
# -----------------------------------------------------------------------------

print("5. Escribiendo archivo vs3.pdbqt...")

outfile = "vs3.pdbqt"
with open(outfile, 'w') as f:
    f.write(f"REMARK  Generated by build_vs3.py for BRAF V600E docking\n")
    f.write(f"REMARK  Complex: [VO(8-hydroxyquinoline)2]  (VS3)\n")
    f.write(f"REMARK  Total atoms: {total_atoms}\n")
    
    for idx, (pos, info) in enumerate(zip(complex_coords, complex_atoms_info)):
        elem, name, serial, ad_type = info
        x, y, z = pos
        charge = charges[idx]
        # Formato: ATOM  (serial)  (name) (resName) (chain) (resSeq) (x) (y) (z) (occ) (temp) (charge) (type)
        # Usamos 5 dígitos para serial (con espacios), 4 para nombre (alineado a la izquierda)
        # Importante: dos espacios entre serial y nombre para que 'VS3' caiga en col 18
        name_field = f"{name:<4}"  # alineado a la izquierda, 4 caracteres
        # Para AutoDock-GPU, el residuo se llama 'VS3' y está en la cadena A
        # Aseguramos que la línea tiene exactamente el formato esperado.
        line = f"ATOM  {serial:5d} {name_field}VS3 A   1    {x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00    {charge:6.3f} {ad_type}\n"
        f.write(line)
    
    # Fin del archivo
    f.write("ENDMDL\n")
    f.write("TER\n")

print("   Archivo vs3.pdbqt generado exitosamente.")
print("   Listo para dockear en el bolsillo ATP.")
print("   Comando de ejemplo:")
print(f"   /mnt/s/CANIFARMA/Programas/AutoDock-GPU.exe --ffile receptor_v2.maps.fld --lfile vs3.pdbqt --nrun 50 --resnam vs3_ATPpocket")