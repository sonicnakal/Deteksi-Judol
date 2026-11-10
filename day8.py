import re

teks = "modal receh jadi jutaan!!!! parah bgt###"
teks_bersih = re.sub(r"[!?#*]{2,}", " ", teks)  # ganti simbol berulang (2x atau lebih) jadi spasi
print(teks_bersih)  # modal receh jadi jutaan  parah bgt

def normalisasi_huruf_berulang(teks):
    # (.) menangkap satu karakter apa saja, \1{2,} artinya karakter itu berulang 2x+
    return re.sub(r"(.)\1{1,}", r"\1", teks)

print(normalisasi_huruf_berulang("gacorrrr banget"))   # gacor banget
print(normalisasi_huruf_berulang("yukkkk gabung yaa"))  # yuk gabung ya

def bersihkan_teks(teks):
    teks = teks.lower()
    teks = re.sub(r"[!?#*]{2,}", " ", teks)          # hapus simbol berlebih
    teks = re.sub(r"(.)\1{2,}", r"\1", teks)         # normalisasi huruf berulang
    teks = re.sub(r"\s+", " ", teks).strip()         # rapikan spasi ganda jadi satu
    return teks

print(bersihkan_teks("GACORRRR PARAH!!!! WDDDD lancarrrr###"))
# hasil: gacor parah wd lancar