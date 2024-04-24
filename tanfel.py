# tantargyFelosztas=[]
# with open("beosztas.txt", "r", encoding="utf-8") as fin:
#     for sor in fin:
#         tantargyFelosztas.append(sor.strip())
        
# for elem in tantargyFelosztas:
#     print(f"{elem}," )
    
# print(f"A listaban  {int(tantargyFelosztas)/4} elem van")

# ver2
tanarok=[]
tantargyak=[]
osztalyok=[]
oraszamok=[]
rekord=[]
with open("beosztas.txt", "r", encoding="utf-8") as fin:
    for sor in fin:
        rekord.append(sor.strip())
        if len(rekord)==4:
            tanarok.append(rekord[0])
            tantargyak.append(rekord[1])
            osztalyok.append(rekord[2])
            oraszamok.append(int(rekord[3]))
            rekord=[]

#for in range(len(tanarok)):
        print(f"{tanarok[i]}, {tantargyak[i]}, {osztalyok[i]} {oraszamok[i]} ")
print("2. feladat")
print(f"A bejegyzesek szama {len(tanarok)}")


print ("3. feladat")
print(f"az iskolaban a heti összoraszam: {sum(oraszamok)}") 


def osszegzes( beTanar, oraszamok, tanarok,tantargyak):
    osszOraszam=0
    
    for i in range(len(tanarok)):
        if tanarok[i]==beTanar:
            osszOraszam+=oraszamok[i]
        
    return osszOraszam
print("4. feladat")
beTanar=input("Egy tanár neve") or "Albatrosz Aladin A tanár heti óraszáma: 24"
print(f"A tanar heti óraszáma: {osszegzes( beTanar, oraszamok, tanarok,tantargyak)}")


print("6. feladat")
def eldontes(beOsztaly, beTantargy, tantargyak, osztalyok):
    i=0
    while(i<len(tantargyak)and not ( beTantargy==tantargyak[i] and  beOsztaly.slipt(".")==osztalyok[i].slipt(".") and "x" in osztalyok[i])  ) 
    i+=1
    if i<len (tantargyak):
        van=True
beOsztaly=input("osztály=") or "9.a"
beTantargy=input("Tantárgy =") or "Kémia"
if eldontes(beOsztaly, beTantargy, tantargyak, osztalyok):
    print("Csoportbontas")
else:
    print("Nem tanuljak csoport munkaban")


print("7. feladat")

tanarokEgyedi=[]
for tanar in tanarok:
    if tanar in tanarokEgyedi:
        tanarokEgyedi.append(tanar)


print(tanarokEgyedi)