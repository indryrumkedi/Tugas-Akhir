import math

def hitung_luas_lingkaran(jari_jari):
  luas = math.pi * jari_jari * jari_jari
  return luas

jari_jari = 5
luas_lingkaran = hitung_luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas_lingkaran}")