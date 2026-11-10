import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def stem_teks(teks):
    kata_kata = teks.split()
    hasil = [stemmer.stem(k) for k in kata_kata]
    return " ".join(hasil)

df = pd.read_excel("dataset_komentar_hari6.xlsx")

# terapkan stemming ke tiap baris, simpan ke kolom baru
df["teks_stemmed"] = df["teks_komentar"].apply(stem_teks)

# tampilkan perbandingan sebelum vs sesudah untuk semua baris
for _, row in df.iterrows():
    print("ASLI   :", row["teks_komentar"][:70])
    print("STEMMED:", row["teks_stemmed"][:70])
    print("-" * 50)

# simpan hasilnya ke file baru biar bisa dicek ulang / dipakai lagi nanti
df.to_excel("dataset_komentar_hari9.xlsx", index=False)
print("\nSelesai, tersimpan ke dataset_komentar_hari9.xlsx")