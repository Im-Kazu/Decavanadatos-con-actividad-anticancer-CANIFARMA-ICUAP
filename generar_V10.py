from ccdc.io import EntryReader, MoleculeWriter

reader = EntryReader('CSD')
entry = reader.entry('ACOTER')
crystal = entry.crystal

packed = crystal.packing(box_dimensions=((0,0,0),(1,1,1)), inclusion='CentreOfMassWithin')

with MoleculeWriter(r'C:\Users\Me\Desktop\Proyectos\Decavanatos\V10_packed.mol2') as w:
    for component in packed.components:
        if 'V' in component.formula:
            w.write(component)
            print("Guardado:", component.formula)
            break