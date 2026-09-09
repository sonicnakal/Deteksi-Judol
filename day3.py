

with open("contoh_komen.txt", "r") as file:
    baris = file.readlines()

for komentar in baris:
    komentar = komentar.strip()
    if "slot" in komentar.lower() or "wd" in komentar.lower():
        print(f"{komentar} -> Mencurigakan")
    else:
        print(f"{komentar} -> Aman")
