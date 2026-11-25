import json

jauns = {"vards": "Drosmīgais", "punkti": 120}

try:
    with open("64_scores.json", "r", encoding="utf-8") as f:
        top = json.load(f)
except FileNotFoundError:
    top = []

top.append(jauns)
top.sort(key=lambda x: x["punkti"], reverse=True)
for ieraksts in top[:5]:
    print(ieraksts)
with open("64_scores.json", "w", encoding="utf-8") as f:
    json.dump(top, f, indent=4)