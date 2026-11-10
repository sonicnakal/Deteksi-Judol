LEET_MAP = {"1": "i", "4": "a", "0": "o", "3": "e"}

def normalisasi_leetspeak(teks):
    kata_kata = teks.split()
    hasil = []
    for kata in kata_kata:
        if any(c.isalpha() for c in kata) and any(c in LEET_MAP for c in kata):
            kata_baru = "".join(LEET_MAP.get(c, c) for c in kata)
            hasil.append(kata_baru)
        else:
            hasil.append(kata)
    return " ".join(hasil)

print(normalisasi_leetspeak("g4c0r parah s1t3 ini"))  # gacor parah site ini