class Pengurus:
    def __init__(self, conn, cursor):
        self.curr = cursor
        self.conn = conn
    def show_pengurus(self):
        search = input("Input NUPTK Pengurus yang ingin datanya dicari?")
        self.curr.execute('SELECT * FROM pengurus WHERE NUPTK_Pengurus =' + search)
        result = self.curr.fetchall()
        print(result)
    def show_pengurusall(self):
        self.curr.execute ('SELECT * FROM pengurus')
        result = self.curr.fetchall()
        print(result)
    def tambahpengurus (self):
        Nama_Pengurus = input("Nama Pengurus yang mau dimasukkan :")
        Jabatan_Pengurus = input("Jabatan Pengurus yang mau dimasukkan :")
        NUPTK_Pengurus = input("NUPTK Pengurus yang mau dimasukkan :")
        MataPelajaran_Pengurus = input("Mata Pelajaran Pengurus yang mau dimasukkan :")
        TTL_Pengurus = input("Input TTL Pengurus yang mau dimasukkan :")
        print('Menambahkan data pengurus...')
        query = 'INSERT INTO pengurus (Nama_Pengurus, Jabatan_Pengurus, NUPTK_Pengurus, MataPelajaran_Pengurus, TTL_Pengurus) VALUES ("' + Nama_Pengurus +'","'+ Jabatan_Pengurus + '","'+ NUPTK_Pengurus + '","' + MataPelajaran_Pengurus + '","' + TTL_Pengurus + '")'
        self.curr.execute(query)
        self.conn.commit()
        print('Proses penambahan selesai')
    def updatedatapengurus (self, NUPTK_Pengurus):
        while True:
            pilih = input("""Silahkan pilih mau mengubah antara (Number Only) 
                          1. Jabatan Pengurus 
                          2. Mata Pelajaran Pengurus 
                          3. Nama Pengurus 
                          4. NUPTK Pengurus
                          5. TTL Pengurus
                          6. Keluar
Masukkan Pilihan: """).title()
            if pilih == "1":
                Jabatan_Pengurus = input("Silahkan input jabatan guru yang ingin diubah :").title()
                print("Mengubah Jabatan pengurus....")
                query = 'UPDATE `pengurus` SET `Jabatan_Pengurus`= "' + Jabatan_Pengurus + '"' + 'WHERE NUPTK_Pengurus ="' + NUPTK_Pengurus + '"';
                self.curr.execute(query)
                self.conn.commit()
                print("Jabatan Pengurus berhasil diubah....")
            elif pilih == "2":
                MataPelajaran_Pengurus = input("Silahkan input mata pelajaran guru yang ingin diubah :").title()
                print("Mengubah Mata Pelajaran pengurus....")
                query = 'UPDATE `pengurus` SET `MataPelajaran_Pengurus`="' + MataPelajaran_Pengurus + '"' + 'WHERE NUPTK_Pengurus ="' + NUPTK_Pengurus + '"';
                self.curr.execute(query)
                self.conn.commit()
                print("Mata Pelajaran Pengurus berhasil diubah....")
            elif pilih == "3":
                Nama_Pengurus = input("Silahkan input Nama pengurus guru yang ingin diubah :").title()
                print("Mengubah Nama Pengurus....")
                query = 'UPDATE `pengurus` SET `Nama_Pengurus`="' + Nama_Pengurus + '"' + 'WHERE NUPTK_Pengurus ="' + NUPTK_Pengurus + '"';
                self.curr.execute(query)
                self.conn.commit()
                print("Nama Pengurus berhasil diubah....")
            elif pilih == "4":
                NUPTK_Pengurus_baru = input("Silahkan input NUPTK pengurus guru yang ingin diubah (6 Digit) :").title()
                print("Mengubah NUPTK Pengurus....")
                query = 'UPDATE `pengurus` SET `NUPTK_Pengurus`="' + NUPTK_Pengurus_baru + '"' + 'WHERE NUPTK_Pengurus ="' + NUPTK_Pengurus + '"';
                self.curr.execute(query)
                self.conn.commit()
                print("NUPTK Pengurus berhasil diubah....")
            elif pilih == "5":
                TTL_Pengurus = input("Silahkan input TTL pengurus guru yang ingin diubah (Format : Tempat<space>Tanggal<space>Bulan<space>Tahun) :").title()
                print("Mengubah TTL Pengurus....")
                query = 'UPDATE `pengurus` SET `TTL_Pengurus`="' + TTL_Pengurus+ '"' + 'WHERE NUPTK_Pengurus ="' + NUPTK_Pengurus + '"';
                self.curr.execute(query)
                self.conn.commit()
                print("TTL Pengurus berhasil diubah....")
            elif pilih == "6":
                print("Keluar!!")
                break
            else:
                print("Silahkan memilih ulang sesuai menu yang tersedia")
                continue
    def __deletedatapengurus(self):
        pilih = input("Silahkan pilih mau menghapus data yang mana? (Input NUPTK)").title()
        print("Menghapus data pengurus....")
        query = 'DELETE FROM `pengurus` WHERE NUPTK_Pengurus = "' + pilih + '"';
        self.curr.execute(query)
        self.conn.commit()
        print("Data Pengurus dengan NUPTK", pilih, "berhasil dihapus....")





    def pengurusOperation(self):
        while True:
            pilihan = str(input("""Silahkan Pilih:
            1. Menampilkan Data Pengurus (BY NPM)
            2. Menampilkan Data Pengurus (ALL)
            3. Tambahkan Data Pengurus
            4. Update Data Pengurus
            5. Hapus Data Pengurus
            6. Keluar
    Masukkan Pilihan ANGKA : """))
            if pilihan == "1":
                self.show_pengurus()
            elif pilihan == "2":
                self.show_pengurusall()
            elif pilihan == "3":
                self.tambahpengurus()
            elif pilihan == "4":
                nuptk = input("Masukkan NUPTK: ")
                self.updatedatapengurus(nuptk)
            elif pilihan == "5":
                self.__deletedatapengurus()
            elif pilihan == "6":
                print("Keluar!!")
                break
            else:
                print("Masukkan Pilihan yang Benar!!!")
                continue
