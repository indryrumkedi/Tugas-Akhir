class Kalkulator:
  def tambah(self, a, b):
    return a + b

  def kurang(self, a, b):
    return a - b

  def kali(self, a, b):
    return a * b

  def bagi(self, a, b):
    return a / b

kalkulator = Kalkulator()

hasil_tambah = kalkulator.tambah(25, 5)
print(f"Hasil penjumlahan: {hasil_tambah}")

hasil_kurang = kalkulator.kurang(15, 12)
print(f"Hasil pengurangan: {hasil_kurang}")

hasil_kali = kalkulator.kali(8, 3)
print(f"Hasil perkalian: {hasil_kali}")

hasil_bagi = kalkulator.bagi(30, 4)
print(f"Hasil pembagian: {hasil_bagi}")