
class Siswa():
    def __init__(self,curr,conn):
        self.conn = conn
        self.curr = curr
    def tambahDataSiswa(self,namaSiswa, kelasSiswa, nisSiswa, genderSiswa):
        sql = "INSERT INTO `data_siswa` (`nama`, `kelas`, `nis`, `gender`) VALUES (%s, %s, %s, %s)"
        self.curr.execute(sql, (namaSiswa, kelasSiswa, nisSiswa, genderSiswa))
        self.conn.commit()
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2,(nisSiswa))
        hasil = self.curr.fetchall()
        print(hasil)

    def __deleteDataSiswa(self,nisSiswa):
        sql = "DELETE FROM `data_siswa` WHERE `nis` = %s"
        self.curr.execute(sql, (nisSiswa))
        print("Data Telah Dihapus!")
        self.conn.commit()

    def showDataSiswa(self, nisSiswa):
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nisSiswa))
        result = self.curr.fetchall()
        print(result)

    def showDataSiswaAll(self):
        sql2 = "SELECT * FROM `data_siswa`"
        self.curr.execute(sql2)
        result = self.curr.fetchall()
        for row in result:
            print(row)


    def setNamaSiswa(self,namaSiswa,nisSiswa):
        sql = "UPDATE `data_siswa` SET `nama` = (%s) WHERE `nis` = (%s)"
        self.curr.execute(sql, (namaSiswa, nisSiswa))
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nisSiswa))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def setKelasSiswa(self,kelasSiswa,nisSiswa):
        kolom = input("")
        sql = "UPDATE `data_siswa` SET (%s) = (%s) WHERE `nis` = (%s)"
        self.curr.execute(sql, (kolom,kelasSiswa, nisSiswa))
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nisSiswa))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def setNISSiswa(self, nisLama, nisBaru):
        sql = "UPDATE `data_siswa` SET `nis` = (%s) WHERE `nis` = (%s)"
        self.curr.execute(sql, (nisBaru, nisLama))
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nisBaru))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def setGenderSiswa(self,genderSiswa,nisSiswa):
        sql = "UPDATE `data_siswa` SET `gender` = (%s) WHERE `nis` = (%s)"
        self.curr.execute(sql, (genderSiswa, nisSiswa))
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nisSiswa))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def updateSiswaOperation(self):
        while True:
            choose = str(input("""Pilih data yang ingin diupdate
            1. Nama Siswa
            2. Kelas Siswa
            3. NIS Siswa
            4. Gender Siswa
            5. Keluar
    Pilihan: """))
            if choose == "1":
                namaSiswa = input("Masukkan Nama Siswa yang Baru: ").title()
                nisSiswa = int(input("Masukkan NIS Siswa: "))
                self.setNamaSiswa(namaSiswa, nisSiswa)
            elif choose == "2":
                nisSiswa = int(input("Masukkan NIS Siswa: "))
                kelasSiswa = input("Masukkan Kelas Siswa yang Baru: ").upper()
                self.setKelasSiswa(kelasSiswa, nisSiswa)
            elif choose == "3":
                nisLama = int(input("Masukkan NIS Lama Siswa: "))
                nisBaru = int(input("Masukkan NIS Baru Siswa: "))
                self.setNISSiswa(nisLama, nisBaru)
            elif choose == "4":
                nisSiswa = int(input("Masukkan NIS Siswa: "))
                genderSiswa = input("Masukkan Gender Siswa yang Baru: ").title()
                self.setGenderSiswa(genderSiswa, nisSiswa)
            elif choose == "5":
                print("Keluar...")
                break
            else:
                print("Masukkan Pilihan Yang Benar!!!")
                __getKey()
                continue

    def showSiswaOperation(self):
        while True:
            choose = str(input("""Silahkan Pilih:
            1. Tampilkan data dengan NIS
            2. Tampilkan Semua Data
            3. Keluar
    Masukkan Pilihan: """))
            if choose == "1":
                nisSiswa = int(input("Masukkan NIS Siswa: "))
                self.showDataSiswa(nisSiswa)
            elif choose == "2":
                self.showDataSiswaAll()
            elif choose == "3":
                print("Keluar!")
                break
            else:
                print("Masukkan Pilihan Yang Benar!!")
                continue

    def siswaOperation(self):
        while True:
            pilihan = str(input("""Silahkan Pilih:
            1. Tambah Data Siswa Baru
            2. Update Data Siswa
            3. Show Data Siswa
            4. Delete Data Siswa
            5. Keluar
    Masukkan Pilihan ANGKA : """))
            if pilihan == "1":
                namaSiswa = input("Masukkan Nama Siswa: ").title()
                kelasSiswa = input("Masukkan Kelas Siswa: ").upper()
                nisSiswa = int(input("Masukkan NIS Siswa: "))
                genderSiswa = input("Masukkan Gender Siswa ").title()
                self.tambahDataSiswa(namaSiswa, kelasSiswa, nisSiswa, genderSiswa)
            elif pilihan == "2":
                self.updateSiswaOperation()
            elif pilihan == "3":
                self.showSiswaOperation()
            elif pilihan == "4":
                nisSiswa = int(input("Masukkan NIS Siswa yang ingin Data Dihapus: "))
                self.__deleteDataSiswa(nisSiswa)
            elif pilihan == "5":
                print("Keluar!!!")
                break
            else:
                print("Masukkan Pilihan Yang Benar!!!")
                continue