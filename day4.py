import re

def bersihkan_teks(teks: str) -> str:
    # 1. Ubah ke huruf kecil
    teks = teks.lower()
    
    # 2. Hapus semua spasi berlebih
    teks = re.sub(r"\s+", "", teks)
    
    # 3. Ganti angka dengan huruf yang sesuai
    mapping = {
        "1": "i",
        "4": "a",
        "0": "o",
        "3": "e"
    }
    for angka, huruf in mapping.items():
        teks = teks.replace(angka, huruf)
    
    return teks

# Contoh penggunaan
contoh_input = "S L O T   G4C0R   H4R1   1N1"
hasil = bersihkan_teks(contoh_input)
print(hasil)  # Output: slotgacorhariini
