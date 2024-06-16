class manusia :
    def init(self,nama,nim,umur,hoby,berat_badan,tinggi_badan):
        self.nama = nama
        self.nim = nim
        self.umur = umur
        self.hoby = hoby
        self.berat_badan = berat_badan

    def sayhallo(self):
        print("hallo saya " + self.nama, "umur ", self.umur, "nim ", self.nim, "hoby", self.hoby, "berat_badan", self.berat_badan, "tinggi_badan", self.tinggi_badan)

nama = input("masukan nama: ")
umur = input("masukan umur: ")
nim = input("masukan nim: ")
hoby = input("masukan hoby: ")
berat_badan = input("masukan berat_badan: ")
tinggi_badan = input("masukan tinggi_badan: ")
