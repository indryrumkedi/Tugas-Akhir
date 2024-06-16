import math
from abc import ABC, abstractmethod


class BangunDatar(ABC):
  """Kelas abstrak untuk bangun datar."""

  def __init__(self, warna):
    self.warna = warna

  @abstractmethod
  def hitung_luas(self):
    """Metode abstrak untuk menghitung luas bangun datar."""
    pass

  @abstractmethod
  def hitung_keliling(self):
    """Metode abstrak untuk menghitung keliling bangun datar."""
    pass


class Persegi(BangunDatar):
  """Kelas konkrit untuk persegi."""

  def __init__(self, sisi, warna):
    super().__init__(warna)
    self.sisi = sisi

  def hitung_luas(self):
    """Menghitung luas persegi."""
    return self.sisi * self.sisi

  def hitung_keliling(self):
    """Menghitung keliling persegi."""
    return 4 * self.sisi


class Lingkaran(BangunDatar):
  """Kelas konkrit untuk lingkaran."""

  def __init__(self, jari_jari, warna):
    super().__init__(warna)
    self.jari_jari = jari_jari

  def hitung_luas(self):
    """Menghitung luas lingkaran."""
    return math.pi * self.jari_jari * self.jari_jari

  def hitung_keliling(self):
    """Menghitung keliling lingkaran."""
    return 2 * math.pi * self.jari_jari


def main():
  """Fungsi utama untuk menjalankan program."""

  # Membuat objek Persegi
  persegi = Persegi(5, "Merah")

  # Menghitung dan menampilkan luas dan keliling persegi
  print(f"Luas persegi: {persegi.hitung_luas()}")
  print(f"Keliling persegi: {persegi.hitung_keliling()}")

  # Membuat objek Lingkaran
  lingkaran = Lingkaran(10, "Biru")

  # Menghitung dan menampilkan luas dan keliling lingkaran
  print(f"Luas lingkaran: {lingkaran.hitung_luas()}")
  print(f"Keliling lingkaran: {lingkaran.hitung_keliling()}")


if __name__ == "__main__":
  main()
