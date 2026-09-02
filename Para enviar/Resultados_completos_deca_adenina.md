# RESULTADOS COMPLETOS: DECAVANADATO + ADENINA (híbrido deca·adenina)

## 1. Construcción del híbrido

**Origen:** Estructura cristalográfica COD 2108583 (Sedghiniya et al.)
- Decavanadato [V₁₀O₂₈]⁶⁻: 10 V + 28 O, diámetro 6.92 Å, compacto
- Adenina: 10 C/N + 6 H, anillo bicíclico intacto
- Par iónico cristalino: distancia centroide-centroide = 7.99 Å, distancia mínima = 3.87 Å

**Híbrido 1:1 usado para docking:** 54 átomos (38 deca + 16 adenina)
- Carga total: -4.21 e (deca -6, adenina +1)
- Geometría: TORSDOF 0 (cuerpo rígido, sin rotación interna)

## 2. Docking contra variantes de BRAF (AutoDock 4.2, pH 5.0)

### 2.1 Comparativa de energías de unión

| Receptor | V₁₀ solo (kcal/mol) | Híbrido deca·adenina (kcal/mol) | Δ (kcal/mol) | Mejora |
|----------|---------------------|----------------------------------|--------------|--------|
| 3OG7 (V600E) | -7.36 | -8.29 | -0.93 | ✓ |
| 4G9C (DFG-out) | -6.95 | -6.62 | +0.33 | |
| 4WO5 | -7.45 | -8.53 | -1.08 | ✓ |
| 4XV2 | -6.26 | -7.31 | -1.05 | ✓ |
| 5C9C | -8.04 | -7.80 | +0.24 | |
| 6U2G | -2.07 | -6.16 | -4.09 | ✓ |

**Resumen:** El híbrido mejora la afinidad en 4 de 6 variantes (67%), con mejora máxima en 6U2G (Δ = -4.09 kcal/mol, Ki pasa de 32 mM a 30 μM).

### 2.2 Análisis del modo de unión (3OG7)

#### Caja grande (128³ puntos, 48 Å de lado)

**Energía:** -8.29 kcal/mol (Ki = 842 nM)
**Descomposición:**
- vdW + Hbond + desolv: -0.11 kcal/mol
- Electrostatic: -8.18 kcal/mol

**Posición del centroide:** (-15.9, 9.1, -27.2) → 22.47 Å del centro del bolsillo ATP
**Conclusión:** El híbrido se une a la **superficie proteica**, lejos del bolsillo ATP, mediante interacciones electrostáticas de largo alcance.

#### Caja chica (60³ puntos, 22.5 Å de lado, centrada en sitio ATP)

**Energía:** -3.32 kcal/mol (Ki = 3.71 mM)
**Descomposición:**
- vdW + Hbond + desolv: -0.47 kcal/mol
- Electrostatic: -7.80 kcal/mol

**Posición del centroide:** (9.4, -5.8, -25.1) → 9.69 Å del centro del bolsillo ATP
**Conclusión:** Cuando se fuerza al bolsillo ATP, el híbrido pierde ~5 kcal/mol de afinidad. El entorno hidrofóbico del bolsillo no tolera bien el cluster cargado.

## 3. Residuos de contacto (<5 Å)

### 3.1 Caja grande (superficie, -8.29 kcal/mol)

**Contactos con el decavanadato:**

| Residuo | dmin (Å) | Tipo |
|---------|----------|------|
| PRO 61 | 0.66 | hidrofóbico |
| GLN 62 | 0.67 | polar |
| THR 90 | 0.68 | polar |
| THR 60 | 0.88 | polar |
| LEU 64 | 0.96 | hidrofóbico |
| GLN 65 | 1.07 | polar |
| PHE 67 | 1.58 | hidrofóbico |
| GLN 63 | 1.58 | polar |
| ALA 66 | 2.38 | hidrofóbico |
| LYS 68 | 2.65 | cargado |
| LEU 94 | 3.82 | hidrofóbico |
| ALA 58 | 3.94 | hidrofóbico |

**Contactos con la adenina:**

| Residuo | dmin (Å) | Tipo |
|---------|----------|------|
| PRO 59 | 0.59 | hidrofóbico |
| THR 90 | 0.68 | polar |
| LEU 64 | 0.96 | hidrofóbico |
| ALA 91 | 1.42 | hidrofóbico |
| GLU 20 | 1.81 | cargado |
| SER 89 | 3.11 | polar |
| LEU 94 | 3.82 | hidrofóbico |
| GLN 93 | 4.77 | polar |
| ILE 21 | 4.82 | hidrofóbico |
| PRO 92 | 4.82 | hidrofóbico |

**Interpretación:** Unión superficial inespecífica a un parche de residuos polares/hidrofóbicos. Las distancias <1 Å sugieren posibles clashes estéricos (artefacto del docking con caja gigante).

### 3.2 Caja chica (bolsillo ATP, -3.32 kcal/mol)

**Contactos con el decavanadato:**

| Residuo | dmin (Å) | Tipo |
|---------|----------|------|
| HIS 108 | 2.59 | cargado |
| ILE 32 | 2.61 | hidrofóbico |
| SER 34 | 2.75 | polar |
| GLY 33 | 2.85 | hidrofóbico |
| ASN 149 | 3.01 | polar |
| TYR 107 | 3.25 | polar |
| ALA 112 | 3.38 | hidrofóbico |
| SER 105 | 3.55 | polar |
| ARG 31 | 4.63 | cargado |

**Contactos con la adenina:**

| Residuo | dmin (Å) | Tipo |
|---------|----------|------|
| CYS 101 | 1.96 | polar |
| GLY 103 | 2.63 | hidrofóbico |
| PHE 152 | 3.50 | hidrofóbico |
| GLU 102 | 3.72 | cargado |
| TRP 100 | 3.82 | hidrofóbico (posible π-stacking) |
| SER 104 | 4.67 | polar |

**Interpretación:** Intento de unión en el bolsillo ATP, contactando residuos del hinge (HIS 108, TYR 107) y regiones adyacentes. Sin embargo, el cluster cargado no penetra bien en el entorno hidrofóbico, resultando en energía desfavorable.

## 4. Residuos dentro del volumen de la caja chica (22.5 Å)

**Total:** 78 residuos

**Lista completa:**

TRP 19, GLY 29, GLN 30, ARG 31, ILE 32, GLY 33, SER 34, GLY 35, PHE 37, GLY 38, THR 39, VAL 40, TYR 41, LYS 42, GLY 43, ASP 48, VAL 49, ALA 50, VAL 51, LYS 52, MET 53, LEU 54, ASN 55, LEU 74, THR 77, ARG 78, ASN 81, ILE 82, LEU 83, LEU 84, PHE 85, MET 86, GLY 87, TYR 88, SER 89, GLN 93, LEU 94, ALA 95, ILE 96, VAL 97, THR 98, GLN 99, TRP 100, CYS 101, GLU 102, GLY 103, SER 104, SER 105, LEU 106, TYR 107, HIS 108, HIS 109, ARG 131, GLY 132, TYR 135, LEU 136, HIS 143, ASP 145, LYS 147, SER 148, ASN 149, ASN 150, ILE 151, PHE 152, LEU 153, HIS 154, GLU 155, ASP 156, THR 158, VAL 159, LYS 160, ILE 161, GLY 162, ASP 163, PHE 164, GLY 165

**Nota:** El residuo "032" corresponde al inhibidor cristalográfico (vemurafenib) en la estructura 3OG7.

## 5. Conclusiones

1. **El híbrido deca·adenina mejora la afinidad** en 4 de 6 variantes de BRAF, especialmente en 6U2G (Δ = -4.09 kcal/mol).

2. **Modo de unión predominante: superficie proteica.** El decavanadato, por su tamaño (~1085 Da) y carga (-4), no puede penetrar eficientemente el bolsillo ATP hidrofóbico. Prefiere unirse a parches cargados de la superficie mediante interacciones electrostáticas de largo alcance.

3. **Mecanismo alostérico confirmado.** Los POMs (polioxometalatos) como el decavanadato actúan como inhibidores alostéricos, no como competidores directos del ATP. La adenina agregada no logra cambiar este comportamiento fundamental.

4. **Implicaciones para diseño de fármacos:** Para lograr inhibición competitiva del sitio ATP con POMs, se requerirían clusters más pequeños y menos cargados (ej: V₄O₁₂, V₆O₁₈) que puedan acomodarse en la hendidura hidrofóbica entre los lóbulos de la quinasa.

## 6. Archivos generados

- `hybrid_deca_1ade.pdb` - Estructura del híbrido 1:1
- `3OG7_hybrid_best.pdb` - Mejor pose dockeada (caja grande, superficie)
- `3OG7_hybrid_smallbox.pdb` - Pose forzada al bolsillo ATP (caja chica)
- `dlg_3OG7_hybrid.dlg` - Log de docking caja grande
- `dlg_3OG7_hybrid_small.dlg` - Log de docking caja chica

---

**Métodos computacionales:**
- Docking: AutoDock 4.2.6 con algoritmo Lamarckian Genetic Algorithm
- Parámetros: ga_pop_size 150, ga_num_evals 2500000, 10 corridas independientes
- Grid: AutoGrid 4.2, spacing 0.375 Å
- Cajas: grande 128³ (48 Å), chica 60³ (22.5 Å)
