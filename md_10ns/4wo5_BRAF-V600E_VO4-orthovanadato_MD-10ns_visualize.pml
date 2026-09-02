# Visualización del frame final de MD (10 ns)
load C:/Users/Me/Desktop/CANIFARMA/Resultados/md_10ns/4wo5_BRAF-V600E_VO4-orthovanadato_MD-10ns_complex_final-frame.pdb, md_final

# Fondo blanco profesional
bg_color white

# Proteína
show cartoon, md_final and polymer.protein
color lightblue, md_final and polymer.protein
set cartoon_transparency, 0.5

# Agua e iones (ocultos por defecto)
hide everything, md_final and solvent
hide everything, md_final and resn NA+CL

# VO4 destacado
show spheres, md_final and resn VO4
show sticks, md_final and resn VO4
set sphere_scale, 0.5, md_final and resn VO4
color orange, md_final and resn VO4 and elem V
color red, md_final and resn VO4 and elem O

# Superficie semitransparente
show surface, md_final and polymer.protein
set surface_transparency, 0.7
set surface_color, gray80, md_final and polymer.protein

# Centrar en VO4
zoom md_final and resn VO4, 15

# Mensaje
print "=== Frame final de MD (10 ns) ==="
print "RMSD proteína: 0.384 nm"
print "RMSD VO4: 0.571 nm"
print "Distancia VO4-Proteína: 0.958 nm"
print "Conclusión: VO4 no forma complejo estable"
