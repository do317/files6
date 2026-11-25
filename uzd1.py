with open("61_dati.txt", "a", encoding="utf-8") as f:
    f.write("Pirmā rinda\n")
with open("61_dati.txt", "r", encoding="utf-8") as f: 
    print(f.read())


import json
dati = {"vards":"ana", "punkti":2, "materiali":[1,2,3]}

with open("61_save.json", "w", encoding="utf-8") as f:
    json.dump(dati, f, indent=4)

with open("61_save.json", "r", encoding="utf-8") as f: 
    ielade = json.load(f)
    print(ielade["punkti"])