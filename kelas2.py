
class kelas:
	def __init__(self, curr, conn):
		self.conn = conn
		self.curr = curr

	def selectDataKelas(self, nama_kelas):
		query = "SELECT * FROM `kelas` WHERE `nama_kelas` = (%s)"
		self.curr.execute(query, (nama_kelas, ))
		result = self.curr.fetchall()
		for row in result:
			print(row)

	def selectJoin(self):
		query = "SELECT "

	def selectDataAllKelas(self):
		query = "SELECT * FROM `kelas`"
		self.curr.execute(query)
		result = self.curr.fetchall()
		for row in result:
			print(row)

	def insertDataKelas(self, nama_kelas, tingkat_kelas, wali_kelas, ketua_kelas, jumlah):
		query = 'INSERT INTO `kelas` (nama_kelas, tingkat_kelas, wali_kelas, ketua_kelas, jumlah) VALUES ("' + nama_kelas +'","'+ tingkat_kelas + '","'+ wali_kelas + '","' + ketua_kelas + '","' + jumlah + '")'
		self.curr.execute(query, )
		self.conn.commit()
		print("insert berhasil")


	def __deleteDataKelas(self, nama_kelas):
		query = "DELETE FROM `kelas` WHERE `nama_kelas` = %s "
		self.curr.execute(query, (nama_kelas,))  # Note the comma to create a single-value tuple
		self.conn.commit()
		print("Data Berhasil Dihapus!")

	def updateDatanamaKelas(self, kelas, nama_kelas):
		query = "UPDATE `kelas` SET `nama_kelas` = (%s) WHERE `nama_kelas` = (%s)"
		self.curr.execute(query, (kelas, nama_kelas))
		query2 = "SELECT * FROM `kelas` WHERE `nama_kelas` = (%s)"
		self.curr.execute(query2, (nama_kelas,))
		result = self.curr.fetchone()
		print(result)
		self.conn.commit()

	def showKelasOperation(self):
		while True:
			choose = str(input("""Silahkan Pilih:
	        1. Tampilkan data dengan Nama Kelas
	        2. Tampilkan Semua Data
	        3. Keluar
Masukkan Pilihan: """))
			if choose == "1":
				nama_kelas = input("Masukkan Nama Kelas: ")
				self.selectDataKelas(nama_kelas)
			elif choose == "2":
				self.selectDataAllKelas()
			elif choose == "3":
				print("Keluar!")
				break
			else:
				print("Masukkan Pilihan Yang Benar!!")
				continue

	def updateDataKelas(self):
		while True:
			pilihData = str(input("""Pilih Data yang Ingin Diubah:
	        1. Tingkat Kelas
	        2. Wali Kelas
	        3. Ketua Kelas
	        4. Jumlah
	        5. Berhenti
Pilihan: """))
			if pilihData == "1":
				nama_kelas = input("Masukkan Nama Kelas: ")
				tingkat_kelas = input("Masukkan Tingkat: ")
				self.updateDataKelas(nama_kelas, tingkat_kelas)
			elif pilihData == "2":
				nama_kelas = input("Masukkan Nama kelas: ")
				wali_kelas = input("Masukkan Wali Kelas yang baru: ")
				self.updateDataKelas(nama_kelas, wali_kelas)
			elif pilihData == "3":
				nama_kelas = input("Masukkan Nama Kelas: ")
				ketua_kelas = input("Masukkan Ketua Kelas yang Baru: ")
				self.updateDataKelas(nama_kelas, ketua_kelas)
			elif pilihData == "4":
				nama_kelas = input("Masukkan Nama Kelas: ")
				jumlah = input("Masukkan Jumlah yang Baru: ")
				self.updateDataKelas(nama_kelas, jumlah)
			elif pilihData == "5":
				print("Berhenti")
				break
			else:
				print("Masukkan Pilihan yang Benar!!")
				continue

	def kelasOperation(self):
		while True:
			pilihan = str(input("""Silahkan Pilih:
	        1. Tambah Data Kelas
	        2. Update Data Kelas
	        3. Show Data Kelas
	        4. Delete Data Kelas
	        5. Keluar
Masukkan Pilihan: """))
			if pilihan == "1":
				nama_kelas = input("Masukkan Nama Kelas: ").upper()
				tingkat_kelas = input("Masukkan Tingkat Kelas: ")
				wali_kelas = input("Masukkan Wali Kelas: ").title()
				ketua_kelas = input("Masukkan Ketua Kelas: ").title()
				jumlah = input("Masukkan Jumlah: ")
				self.insertDataKelas(nama_kelas, tingkat_kelas, wali_kelas, ketua_kelas, jumlah)
			elif pilihan == "2":
				self.updateDataKelas()
			elif pilihan == "3":
				self.showKelasOperation()
			elif pilihan == "4":
				namakelas = input("Masukkan Kelas: ").upper()
				self.__deleteDataKelas(namakelas)
			elif pilihan == "5":
				print("Keluar!!")
				break
			else:
				print("Masukkan Pilihan yang Benar!!!")

				continue