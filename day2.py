# List komentar
komentar_list = [
    "Main slot gampang menang",
    "WD cepat cair",
    "Belajar Python itu seru",
    "Makan bakso di Depok",
    "Jangan lupa olahraga"
]

# Loop dan cek
for komentar in komentar_list:
    if "slot" in komentar.lower() or "wd" in komentar.lower():
        print(f"{komentar} -> Mencurigakan")
    else:
        print(f"{komentar} -> Aman")
