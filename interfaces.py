from abc import ABC, abstractmethod

class poligon(ABC):
  @abstractmethod
  def jumlah_sisi(self):
    pass


class segitiga (poligon):
  def jumlah_sisi(self):
    print('saya memiliki 3 sisi')

class segiempat (poligon):
  def jumlah_sisi(self):
    print('saya memiliki 4 sisi')

class segilima (poligon):
  def jumlah_sisi(self):
    print('saya memiliki 5 sisi')

r = segitiga()
r.jumlah_sisi()

k = segiempat()
k.jumlah_sisi()

r = segilima()
r.jumlah_sisi()