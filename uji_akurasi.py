import pandas as pd
from kata_kunci import cek_komentar

df = pd.read_excel("dataset_komentar_hari6.xlsx")

benar = 0
for _, row in df.iterrows():
    hasil = cek_komentar(row["teks_komentar"])
    prediksi = "judol" if hasil["terdeteksi"] else "bukan"
    label_asli = row["label"]
    cocok = "OK" if prediksi == label_asli else "SALAH"

    if cocok == "OK":
        benar += 1
    else:
        print(f"[{cocok}] asli={label_asli:5} | prediksi={prediksi:5} | {row['teks_komentar'][:70]}")

print(f"\nAkurasi: {benar}/{len(df)} = {benar/len(df)*100:.0f}%")