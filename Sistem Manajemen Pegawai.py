class Pegawai:
    def __init__(self, id_pegawai, nama, gaji):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.gaji = gaji

    def tampilkan_pegawai(self):
        print("ID Pegawai  :", self.id_pegawai)
        print("Nama        :", self.nama)
        print("Gaji        : Rp", self.gaji)


class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek

    def tampilkan_proyek(self):
        print("Nama Proyek :", self.nama_proyek)


class ProjectManager(Pegawai, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        Pegawai.__init__(self, id_pegawai, nama, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

    def tampilkan_data(self):
        self.tampilkan_pegawai()
        self.tampilkan_proyek()


pm1 = ProjectManager(
    "PM001",
    "Andi Pratama Wijaya",
    8000000,
    "Sistem Informasi Akademik"
)

pm2 = ProjectManager(
    "PM002",
    "Budi Setiawan Nugraha",
    9000000,
    "Aplikasi E-Commerce"
)

pm3 = ProjectManager(
    "PM003",
    "Citra Lestari Maharani",
    8500000,
    "Sistem Manajemen Rumah Sakit"
)


print("DATA PROJECT MANAGER 1")
pm1.tampilkan_data()
print()

print("DATA PROJECT MANAGER 2")
pm2.tampilkan_data()
print()

print("DATA PROJECT MANAGER 3")
pm3.tampilkan_data()