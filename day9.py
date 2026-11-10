from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def stem_teks(teks):
    kata_kata = teks.split()
    hasil = [stemmer.stem(k) for k in kata_kata]
    return " ".join(hasil)

print(stem_teks("dapat kemenangan besar hari ini"))