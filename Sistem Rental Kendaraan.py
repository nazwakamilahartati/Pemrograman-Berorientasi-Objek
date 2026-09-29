class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def tampilkan_data(self):
        print("Nama       :", self.nama)
        print("Merk       :", self.merk)
        print("Tahun      :", self.tahun)
        print("Kecepatan  :", self.kecepatan, "km/jam")


class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jumlah Kursi :", self.jumlah_kursi)


class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Tipe Motor :", self.tipe_motor)

mobil1 = Mobil("Avanza", "Toyota", 2022, 180, 7)
mobil2 = Mobil("Civic", "Honda", 2023, 200, 5)
mobil3 = Mobil("Xpander", "Mitsubishi", 2021, 170, 7)

motor1 = Motor("NMAX", "Yamaha", 2023, 150, "Matic")
motor2 = Motor("CBR 150R", "Honda", 2022, 160, "Sport")
motor3 = Motor("Vespa Sprint", "Vespa", 2023, 120, "Matic")

print("DATA MOBIL 1" )
mobil1.tampilkan_data()
print()
print("DATA MOBIL 2")
mobil2.tampilkan_data()
print()
print("DATA MOBIL 3")
mobil3.tampilkan_data()
print()

print("DATA MOTOR 1")
motor1.tampilkan_data()
print()
print("DATA MOTOR 2")
motor2.tampilkan_data()
print()
print("DATA MOTOR 3")
motor3.tampilkan_data()
print()