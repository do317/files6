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