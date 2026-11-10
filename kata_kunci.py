"""
Daftar kata kunci & pola judi online (judol) hasil riset hari 5-6.
Disusun dari data komentar YouTube asli, bukan asumsi generik.
"""

import re

# 1. Kata kunci inti yang sering muncul di komentar judol
KATA_KUNCI_JUDOL = [
    "slot", "gacor", "maxwin", "jp", "scatter",
    "depo", "modal", "wd", "menang", "hoki", "rezeki",
    "pulauwin", "magnum", "mona", "mawar",  # nama situs spesifik dari data kamu
]


# 2. Pola nama situs yang disamarkan: kata + angka nempel (MAGNUM62, MONA4D, MAWAR61)
POLA_NAMA_SITUS = re.compile(r"[a-zA-Z]{4,}\d{2,3}")  # wajib 2-3 digit

# 3. Pola trik kapital+spasi menyisip di tengah kata (contoh: "keP U L A U W I N")
POLA_SPASI_KAPITAL = re.compile(r"([A-Z]\s){3,}[A-Z]")

# 4. Pola link/kontak mencurigakan (dipakai lagi nanti pas integrasi YouTube API)
POLA_KONTAK = re.compile(r"wa\.me|bit\.ly|t\.me|\d{9,}")
POLA_LINK_UMUM = re.compile(r"\b[a-z0-9-]+\.(com|net|id|xyz|link|vip)\b")
LEET_MAP = {"1": "i", "4": "a", "0": "o", "3": "e"}

# token uang: angka (boleh pakai titik/koma) + satuan, contoh: 1jt, 120k, 1,2jt, 55rb
POLA_UANG = re.compile(r"\d+([.,]\d+)?(jt|rb|k|juta|ribu)")

def normalisasi_leetspeak(teks):
    hasil = []
    for kata in teks.split():
        if POLA_UANG.fullmatch(kata):
            hasil.append(kata)  # token uang dibiarkan apa adanya
        elif any(c.isalpha() for c in kata) and any(c in LEET_MAP for c in kata):
            hasil.append("".join(LEET_MAP.get(c, c) for c in kata))
        else:
            hasil.append(kata)
    return " ".join(hasil)

def bersihkan_teks(teks):
    teks = teks.lower()
    teks = normalisasi_leetspeak(teks)
    teks = re.sub(r"[!?#*]{2,}", " ", teks)          # hapus simbol berlebih
    teks = re.sub(r"([a-z])\1+", r"\1", teks)
    teks = re.sub(r"\s+", " ", teks).strip()         # rapikan spasi ganda jadi satu
    return teks


def cek_komentar(teks: str) -> dict:
    teks_bersih = bersihkan_teks(teks)  # untuk cek kata kunci & kontak
    alasan = []

    ditemukan_kata = [k for k in KATA_KUNCI_JUDOL if k in teks_bersih]
    if ditemukan_kata:
        alasan.append(f"kata kunci: {', '.join(ditemukan_kata)}")

    if POLA_NAMA_SITUS.search(teks):        # tetap pakai teks ASLI
        alasan.append("pola nama situs disamarkan")

    if POLA_SPASI_KAPITAL.search(teks):     # tetap pakai teks ASLI (butuh huruf besar)
        alasan.append("pola trik spasi+kapital")

    if POLA_KONTAK.search(teks_bersih):
        alasan.append("pola link/kontak mencurigakan")
    if POLA_LINK_UMUM.search(teks_bersih):
        alasan.append("pola link domain mencurigakan")
    return {
        "teks": teks,
        "terdeteksi": len(alasan) > 0,
        "alasan": alasan,
    }


if __name__ == "__main__":
    contoh = [
        "gue cuman main di MAGNUM62 king perdana full modif. Padahal depo 1,2jt jadi 55jt",
        "keP U L A U W I N",
        "Musiknya beneran bikin merinding",
        "Cantik baik g ada minus",
        # tambahan baru:
        "g4c0r parah depo 1jt jadi 55jt",
        "cek pulauwin.vip sekarang",
        "temen2 gue pada suka lagu ini",
    ]
    for teks in contoh:
        hasil = cek_komentar(teks)
        status = "JUDOL" if hasil["terdeteksi"] else "aman"
        print(f"[{status}] {teks}")
        if hasil["alasan"]:
            print("   ->", "; ".join(hasil["alasan"]))

    # tes normalisasi (di luar loop, tapi masih di dalam blok if)
    print()
    print(normalisasi_leetspeak("g4c0r parah depo 1jt jadi 120k"))
    print(bersihkan_teks("G4C0RRR PARAH depo 1jt jadi 55jt!!!"))