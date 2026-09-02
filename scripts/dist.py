import sys, math

AA = set("""ALA ARG ASN ASP CYS GLN GLU GLY HIS HSD HSE HSP HIP HID HIE
ILE LEU LYS MET PHE PRO SER THR TRP TYR VAL ACE NME
HOH WAT SOL NA CL MG ZN K CA""".split())

pdb = sys.argv[1]
cutoff = float(sys.argv[2]) if len(sys.argv) > 2 else 5.0

lig, prot = [], []
with open(pdb) as f:
    for line in f:
        if not line.startswith(("ATOM","HETATM")): continue
        try:
            resn   = line[17:20].strip()
            resnum = line[22:26].strip()
            aname  = line[12:16].strip()
            x = float(line[30:38]); y = float(line[38:46]); z = float(line[46:54])
        except: continue
        (prot if resn in AA else lig).append((resn,resnum,aname,x,y,z))

if not lig:
    print("No se detectó ligando"); sys.exit()

print(f"Ligando: {sorted(set(a[0] for a in lig))} ({len(lig)} átomos)")
print(f"\nResiduos a < {cutoff} Å del ligando:\n")
print(f"{'Residuo':<10}{'Dist(Å)':<9}{'Át.prot':<10}{'Át.lig':<9}Contacto")

res_min = {}
for (rn,rnum,an,x,y,z) in prot:
    for (lr,lnum,la,lx,ly,lz) in lig:
        d = math.sqrt((x-lx)**2+(y-ly)**2+(z-lz)**2)
        key = f"{rn} {rnum}"
        if key not in res_min or d < res_min[key][0]:
            ct = ""
            if rn in ("ARG","LYS","HIP") and d < 4.0: ct = "<<< PUENTE SALINO"
            elif d < 3.5: ct = "< H-bond/vdW"
            res_min[key] = (d, an, la, ct)

for key,(d,an,la,ct) in sorted(res_min.items(), key=lambda kv: kv[1][0]):
    if d <= cutoff:
        print(f"{key:<10}{d:<9.2f}{an:<10}{la:<9}{ct}")
