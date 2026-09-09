"""
Daftar kata kunci & pola judi online (judol) hasil riset hari 5-6.
Disusun dari data komentar YouTube asli, bukan asumsi generik.
"""

import re

# 1. Kata kunci inti yang sering muncul di komentar judol
KATA_KUNCI_JUDOL = [
    "slot", "gacor", "maxwin", "jp", "scatter",
    "depo", "modal", "wd", "menang", "hoki", "rezeki",
]

# 2. Pola nama situs yang disamarkan: kata + angka nempel (MAGNUM62, MONA4D, MAWAR61)
POLA_NAMA_SITUS = re.compile(r"[a-zA-Z]{4,}\d{1,3}")

# 3. Pola trik kapital+spasi menyisip di tengah kata (contoh: "keP U L A U W I N")
POLA_SPASI_KAPITAL = re.compile(r"([A-Z]\s){3,}[A-Z]")

# 4. Pola link/kontak mencurigakan (dipakai lagi nanti pas integrasi YouTube API)
POLA_KONTAK = re.compile(r"wa\.me|bit\.ly|t\.me|\d{9,}")


def cek_komentar(teks: str) -> dict:
    """Cek satu komentar, kembalikan dict berisi status & alasan deteksi."""
    teks_lower = teks.lower()
    alasan = []

    ditemukan_kata = [k for k in KATA_KUNCI_JUDOL if k in teks_lower]
    if ditemukan_kata:
        alasan.append(f"kata kunci: {', '.join(ditemukan_kata)}")

    if POLA_NAMA_SITUS.search(teks):
        alasan.append("pola nama situs disamarkan")

    if POLA_SPASI_KAPITAL.search(teks):
        alasan.append("pola trik spasi+kapital")

    if POLA_KONTAK.search(teks_lower):
        alasan.append("pola link/kontak mencurigakan")

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
    ]
    for teks in contoh:
        hasil = cek_komentar(teks)
        status = "JUDOL" if hasil["terdeteksi"] else "aman"
        print(f"[{status}] {teks}")
        if hasil["alasan"]:
            print("   ->", "; ".join(hasil["alasan"]))
