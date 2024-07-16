
class matapelajaran:
    def __init__(self,curr,conn):
        self.conn = conn
        self.curr = curr

    def select_data(self,id):
        query = "SELECT * FROM `mata_pelajaran` WHERE `id` = (%s)"
        self.curr.execute(query, (id, ))
        result = self.curr.fetchall()
        for row in result:
            print(row)

    def select_data_all(self): #ini buat show semua data
        query = "SELECT * FROM `mata_pelajaran`"
        self.curr.execute(query)
        result = self.curr.fetchall()
        for row in result:
            print(row)

    def insert_data(self,id, matapelajaran, pengajar):
        query = "INSERT INTO `mata_pelajaran` (id, mataPelajaran, pengajar) VALUES (%s, %s, %s)"
        self.curr.execute(query, (id, matapelajaran, pengajar))
        self.conn.commit()
        print("Penambahan selesai")

    def updateDataMapel (self, matapelajaranbaru, id):
        query = "UPDATE `mata_pelajaran` SET `matapelajaran` = (%s) WHERE `id` = (%s)"  # coba pakai id aja untuk WHEREnya
        self.curr.execute(query, (matapelajaranbaru, id))
        query2 = "SELECT * FROM `mata_pelajaran` WHERE `id` = (%s)"
        self.curr.execute(query2, (id))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def updateDataID (self, idlama, idbaru):
        query = "UPDATE `mata_pelajaran` SET `id` = (%s) WHERE `id` = (%s)"  # coba pakai id untuk WHERE
        self.curr.execute(query, (idbaru, idlama))
        query2 = "SELECT * FROM `mata_pelajaran` WHERE `id` = (%s)"
        self.curr.execute(query2, (idbaru))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def updateDataPengajar (self, id, pengajar):
        query = "UPDATE `mata_pelajaran` SET `pengajar` = (%s) WHERE `id` = (%s)"  # sama pakai id
        self.curr.execute(query, (pengajar, id))
        query2 = "SELECT * FROM `mata_pelajaran` WHERE `id` = (%s)"
        self.curr.execute(query2, (id))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def __delete_data(self,id):
        query = "DELETE FROM `mata_pelajaran` WHERE `id` = %s"
        self.curr.execute(query, (id))  # Note the comma to create a single-value tuple
        self.conn.commit()
        print("Data Telah Dihapus!")

    def updateDataMapel(self):
        while True:
            pilihData = str(input("""Pilih Data yang Ingin Diubah:
            1. Mata Pelajaran
            2. ID
            3. Pengajar
            4. Berhenti
Pilihan: """))
            if pilihData == "1":
                id = input("Masukkan ID: ").upper()
                matapelajaranbaru = input("Masukkan Matapelajaran yang baru: ").title()
                self.updateDataMapel(matapelajaranbaru, id)
            elif pilihData == "2":
                idLama = input("Masukkan ID yang Lama: ").upper()
                idBaru = input("Masukkan ID yang Baru: ").upper()
                self.updateDataID(idLama, idBaru)
            elif pilihData == "3":
                id = input("Masukkan ID: ").upper()
                pengajar = input("Masukkan Pengajar yang Baru: ").title()
                self.updateDataPengajar(id, pengajar)
            elif pilihData == "4":
                print("Berhenti")
                break
            else:
                print("Masukkan Pilihan yang Benar!!")
                continue

    def showMapelOperation(self):
        while True:
            choose = str(input("""Silahkan Pilih:
                1. Tampilkan data dengan ID
                2. Tampilkan Semua Data
                3. Keluar
Masukkan Pilihan: """))
            if choose == "1":
                id = input("Masukkan ID: ")
                self.select_data(id)
            elif choose == "2":
                self.select_data_all()
            elif choose == "3":
                print("Keluar!")
                break
            else:
                print("Masukkan Pilihan Yang Benar!!")
                continue

    def mapelOperation(self):
        while True:
            pilihan = str(input("""Silahkan Pilih:
            1. Tambah Data Mata Pelajaran
            2. Update Data Mata Pelajaran
            3. Show Data Mata Pelajaran
            4. Delete Data Mata Pelajaran
            5. Keluar
Masukkan Pilihan: """))
            if pilihan == "1":
                id = input("Masukkan ID: ").upper()
                matapelajaran = input("Masukkan Mata Pelajaran: ").title()
                pengajar = input("Masukkan Pengajar: ").title()
                self.insert_data(id, matapelajaran, pengajar)
            elif pilihan == "2":
                self.updateDataMapel()
            elif pilihan == "3":
                self.showMapelOperation()
            elif pilihan == "4":
                id = input("Masukkan ID: ").upper()
                self.__delete_data(id)
            elif pilihan == "5":
                print("Keluar!!")
                break
            else:
                print("Masukkan Pilihan yang Benar!!!")
                continue