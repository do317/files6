import csv

with open('62_pasaule.csv', mode='r', encoding='utf-8') as f:

    lasitajs = csv.DictReader(f)
    lasitajs = list(lasitajs)

    visi_id = []

    for rinda in lasitajs:
        visi_id.append(rinda['id'])
    for rinda in lasitajs:
        if not (rinda['merkis_a'] in visi_id):
            print("error: merkis_a nav legals id")



pasaules_karte = {}
with open('63_pasaule.csv', mode='r', encoding='utf-8') as f:
    lasitajs = csv.DictReader(f)
    
    for rinda in lasitajs:
        id_skaitlis = int(rinda['id'].strip())
        
        pasaules_karte[id_skaitlis] = rinda

print(pasaules_karte[2]['teksts'])
print(pasaules_karte.len())