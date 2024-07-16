
import time

class absensi:

    def __init__(self,conn,curr):
        self.conn = conn
        self.curr = curr

    def tambahAbsensi(self):
        nomorSiswa = int(input("Nomor siswa: "))
        namaSiswa = input("Nama siswa: ")
        tipeAbsensi = input("Status? (A / I / S / H) : ").upper()
        sql = "INSERT INTO absensi (nis, nama_siswa, tanggal, keterangan) VALUES (%s, %s, CURRENT_TIMESTAMP, %s)"
        self.curr.execute(sql, (nomorSiswa, namaSiswa,  tipeAbsensi))
        print('Menambahan data siswa...')
        time.sleep(2)
        self.conn.commit()
        print('Proses penambahan selesai')

    def pilihAbsensi(self):
        nomorSiswa = int(input("Nomor siswa: "))
        sql2 = "SELECT * FROM `absensi` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nomorSiswa))
        result = self.curr.fetchone()
        print(result)


    def editAbsensi(self):
        nomorSiswa = int(input("Nomor siswa: "))
        apa = "SELECT * FROM `absensi` WHERE `nis` = (%s)"
        self.curr.execute(apa, args=(nomorSiswa))
        result = self.curr.fetchone()
        print(result)
        tanggalAbsensi = input("Tanggal & Waktu Absensi (yyyy-mm-dd HH:MM:SS): ")
        tipeAbsensi = input("Ganti status ke? (A / I / S / H) : ")
        sql3 = "UPDATE `absensi` SET `keterangan` = %s, `tanggal` = %s WHERE `nis` = %s"
        self.curr.execute(sql3, args=(tipeAbsensi, tanggalAbsensi, nomorSiswa))
        resultedit = self.curr.fetchone()
        print(resultedit)
        self.conn.commit()
        a = 0
        b = 0
        c = 0
        d = 0
        if tipeAbsensi == "Hadir":
            a = a + 1
        elif tipeAbsensi == "Sakit":
            b = b + 1
        elif tipeAbsensi == "Izin":
            c = c + 1
        elif tipeAbsensi == "Alpha":
            d = d + 1

    def __hapusAbsensi(self):
        nomorSiswa = int(input("Nomor siswa: "))
        sql2 = "DELETE FROM `absensi` WHERE `nis` = (%s)"

        self.curr.execute(sql2, (nomorSiswa))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def absensiOperation(self):
        while True:
            pilihan = str(input("""Silahkan Pilih:
                1. Tambah Data Absensi
                2. Update Data Absensi
                3. Show Data Absensi
                4. Delete Data Absensi
                5. Keluar
        Masukkan Pilihan ANGKA : """))
            if pilihan == "1":
                self.tambahAbsensi()
            elif pilihan == "2":
                self.editAbsensi()
            elif pilihan == "3":
                self.pilihAbsensi()
            elif pilihan == "4":
                nisSiswa = int(input("Masukkan NIS Siswa yang ingin Data Dihapus: "))
                self.__hapusAbsensi()
            elif pilihan == "5":
                print("Keluar!!!")
                break
            else:
                print("Masukkan Pilihan Yang Benar!!!")
                continue

