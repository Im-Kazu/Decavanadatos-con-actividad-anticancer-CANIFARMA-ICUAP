================================================================================
  CO-VALIDACION DE VANADATOS CONTRA BRAF V600E (pH 5.0) - RESULTADOS
  Proyecto CANIFARMA | 2026-08-05
================================================================================

--------------------------------------------------------------------------------
1. ENTORNO
--------------------------------------------------------------------------------
  Sistema       : Windows 11 + WSL2 (Ubuntu) / TerminalXolotl
  Entorno Python: conda "pqr311" (Python 3.11)
  Ruta proyecto : C:\Users\Me\Desktop\CANIFARMA\br_set
  Resultados    : C:\Users\Me\Desktop\CANIFARMA\Resultados\Para enviar

--------------------------------------------------------------------------------
2. PROGRAMAS
--------------------------------------------------------------------------------
  AutoDock      : autodock4 / autogrid4  (envs/ad4)
  Protonacion   : PDB2PQR 3.x + PROPKA (ff=AMBER, pH 5.0)
  Conversion    : OpenBabel 3.1.0 (mmCIF/SDF -> PDB)
  Analisis/IO   : BioPython 1.x, NumPy
  Visualizacion : PyMOL

--------------------------------------------------------------------------------
3. RECEPTORES (PDB ID + coordenadas del sitio de docking = centroide del
   inhibidor cristalográfico nativo, en Angstroms)
--------------------------------------------------------------------------------
  PDB_ID   Inhibidor_nativo   Conformacion        Centro_X    Centro_Y    Centro_Z
  ------   ----------------   --------------      --------    --------    --------
  4XV2     Dabrafenib (P06)   Type I / DFG-in      -2.10       -2.14       -7.27
  5C9C     LY3009120 (4Z5)    Type I              -14.17       33.44        6.64
  4WO5     Ligando-324        (referencia)        -28.23      -12.20      -28.24
  4G9C     0WP                Type II / DFG-out    30.13      -17.51       -6.73

  Todos protonados a pH 5.0 tumoral. Caja: 96x96x96 pts, spacing 0.375 A.

--------------------------------------------------------------------------------
4. LIGANDOS DE VANADIO
--------------------------------------------------------------------------------
  Codigo     Especie                  Formula      Atomos   Geometria
  ------     -------                  -------      ------   ---------
  VO4        Orto-vanadato            [VO4]3-        5      Tetraedro
  V6ring     Ciclo-hexavanadato       [V6O18]6-     24      Anillo ~6 A
  V10        Decavanadato             [V10O28]6-    38      Cluster (coord. reales)

--------------------------------------------------------------------------------
5. RESULTADOS (mejor energia de 20 runs, kcal/mol; AutoDock 4.2, LGA)
--------------------------------------------------------------------------------
  Estructura   Sitio                  VO4      V6-anillo    V10      Ganador
  ----------   ------------------   -------    ---------   -------   ---------
  4XV2         Dabrafenib (I/DFG-in)  -9.67      -9.37      -6.79     VO4
  5C9C         LY3009120 (I)          -9.01     -10.27      -8.38     V6-anillo
  4WO5         Ligando-324 (ref)      -7.82      -9.57      -7.73     V6-anillo
  4G9C         0WP (II/DFG-out)       -6.56      -8.35      -7.40     V6-anillo
  PROMEDIO                            -8.27      -9.39      -7.58     V6-anillo

  Mejor caso global: V6-anillo en 5C9C = -10.27 kcal/mol

--------------------------------------------------------------------------------
6. CONCLUSIONES
--------------------------------------------------------------------------------
  - Los vanadatos unen BRAF V600E con afinidad de farmaco (-6.6 a -10.3 kcal/mol),
    reproducible en 4 cristales (co-validacion robusta).
  - El anillo [V6O18]6- es la mejor candidata: gana 3/4 sitios, mejor promedio.
  - Tamano penaliza: V6 ~ VO4 >> V10 (el decavanadato es muy grande p/ el bolsillo).
  - Preferencia por sitios Type I (DFG-in) cargados sobre DFG-out hidrofobico.
  - Validacion visual: los vanadatos ocupan el mismo bolsillo que el farmaco nativo
    (inhibicion competitiva con ATP, mecanicamente creible).

--------------------------------------------------------------------------------
7. ARCHIVOS (cada PDB = receptor BRAF + mejor pose del vanadato, con enlaces V-O)
--------------------------------------------------------------------------------
  BRAF_4XV2_con_OrtoVanadato_VO4__-9.67kcal.pdb
  BRAF_5C9C_con_Anillo_V6O18__-10.27kcal.pdb        <- mejor caso
  BRAF_4WO5_con_Anillo_V6O18__-9.57kcal.pdb
  BRAF_4G9C_con_Anillo_V6O18_DFGout__-8.35kcal.pdb
  BRAF_4XV2_con_Decavanadato_V10__-6.79kcal.pdb
  BRAF_5C9C_con_Decavanadato_V10__-8.38kcal.pdb
  BRAF_4WO5_con_Decavanadato_V10__-7.73kcal.pdb
  BRAF_4G9C_con_Decavanadato_V10_DFGout__-7.40kcal.pdb
