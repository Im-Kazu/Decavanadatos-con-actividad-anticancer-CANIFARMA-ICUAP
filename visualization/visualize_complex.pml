# Visualización del complejo BRAF V600E + Decavanadato
# Cargar archivos
load C:/Users/Me/Desktop/CANIFARMA/visualization/4wo5_chainA_clean.pdb, receptor
load C:/Users/Me/Desktop/CANIFARMA/visualization/best_pose_blind_clean.pdb, ligand

# Configurar fondo
bg_color white

# Representación del receptor (proteína)
hide everything, receptor
show cartoon, receptor
color lightblue, receptor
set cartoon_transparency, 0.3

# Representación del ligando (decavanadato)
hide everything, ligand
show spheres, ligand
show sticks, ligand
set sphere_scale, 0.4, ligand
set stick_radius, 0.3, ligand

# Colorear por elemento: Vanadio en naranja, Oxígeno en rojo
color orange, ligand and elem V
color red, ligand and elem O

# Mostrar superficie de la proteína para ver dónde se une
show surface, receptor
set surface_transparency, 0.7
set surface_color, gray80, receptor

# Centrar la vista en el ligando
zoom ligand, 10

# Rayos para mejor calidad
set ray_shadows, 1
set ray_trace_mode, 1

# Mensaje informativo
print "Complejo BRAF V600E + Decavanadato cargado"
print "Vanadio (V) = esferas naranjas"
print "Oxigeno (O) = esferas rojas"
print "Energía de unión: -2.12 kcal/mol (docking ciego)"
