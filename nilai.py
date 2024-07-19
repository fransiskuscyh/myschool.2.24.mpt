import tkinter as tk
from tkinter import messagebox,ttk
import customtkinter as ct

import statistics as st
#dbApp = mainDB()
#conn_dbApp, curr_dbApp = dbApp.connect()

class Nilai (ct.CTkFrame):
    def __init__(self,curr,conn,master):
        super().__init__(master)


        self.curr = curr
        self.conn = conn
        self.font = ct.CTkFont(family='montserrat', size=17)


    def setup_ui(self,masterss):

        self.nama = ct.CTkLabel(master=masterss, text="nama murid", anchor="e", justify="right", width=100)
        self.font_nilai = ct.CTkFont('montserrat', 15)
        self.nama.configure(font=self.font_nilai)
        self.id = ct.CTkLabel(master=masterss, text="id murid", anchor="e", justify="right", width=100,
                              font=self.font_nilai)
        self.id_kelas = ct.CTkLabel(master=masterss, text="kelas", anchor="e", justify="right", width=100,
                                    font=self.font_nilai)
        self.id_matkul = ct.CTkLabel(master=masterss, text="matkul", anchor="e", justify="right", width=100,
                                     font=self.font_nilai)
        self.nilai_tugas = ct.CTkLabel(master=masterss, text="nilai tugas", anchor="e", justify="right", width=100,
                                       font=self.font_nilai)
        self.nilai_ujian = ct.CTkLabel(master=masterss, text="nilai ujian", anchor="e", justify="right", width=100,
                                       font=self.font_nilai)

        self.nama.place(x=10, y=35)
        self.id.place(x=10, y=60)
        self.id_kelas.place(x=10, y=85)
        self.id_matkul.place(x=10, y=110)
        self.nilai_tugas.place(x=10, y=135)
        self.nilai_ujian.place(x=10, y=160)

        self.nama_var = tk.StringVar()
        self.id_var = tk.StringVar()
        self.id_kelas_var = tk.StringVar()
        self.id_matkul_var = tk.StringVar()
        self.nilai_tugas_var = tk.StringVar()
        self.nilai_ujian_var = tk.StringVar()

        self.entry_nama = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.nama_var, width=500)
        self.entry_nama.place(x=120, y=35)
        self.entry_id = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_var, width=500)
        self.entry_id.place(x=120, y=60)
        self.entry_id_kelas = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_kelas_var,
                                          width=500)
        self.entry_id_kelas.place(x=120, y=85)
        self.entry_id_matkul = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_matkul_var,
                                           width=500)
        self.entry_id_matkul.place(x=120, y=110)
        self.entry_nilai_tugas = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.nilai_tugas_var,
                                             width=500)
        self.entry_nilai_tugas.place(x=120, y=135)
        self.entry_nilai_ujian = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.nilai_ujian_var,
                                             width=500)
        self.entry_nilai_ujian.place(x=120, y=160)

        self.columns = ('id', 'nama', 'kelas', 'matkul', 'nilai tugas', 'nilai ujian', 'rata-rata')
        self.table = ttk.Treeview(master=masterss, columns=self.columns, show='headings', height=300)
        self.table.heading('id', text='ID')
        self.table.column('id', minwidth=0, width=60, stretch=False)
        self.table.heading('nama', text='Nama')
        self.table.column('nama', minwidth=0, width=140, stretch=False)
        self.table.heading('kelas', text='Kelas')
        self.table.column('kelas', minwidth=0, width=80, stretch=False)
        self.table.heading('matkul', text='Matkul')
        self.table.column('matkul', minwidth=0, width=140, stretch=False)
        self.table.heading('nilai tugas', text='Nilai Tugas')
        self.table.column('nilai tugas', minwidth=0, width=100, stretch=False)
        self.table.heading('nilai ujian', text='Nilai Ujian')
        self.table.column('nilai ujian', minwidth=0, width=100, stretch=False)
        self.table.heading('rata-rata', text='Rata-Rata')
        self.table.column('rata-rata', minwidth=0, width=100, stretch=False)

        # self.table.place(x=80, y=280)
        self.table.place(relx=0.05, rely=0.35)

        self.button_cari = ct.CTkButton(master=masterss, height=40, width=150, text='cari', fg_color="#00df00",
                                        font=('montserrat', 17), command=lambda: self.pemastian_murid_nilai_cari())
        self.button_ubah_tugas = ct.CTkButton(master=masterss, height=40, width=150, text='ubah nilai tugas',
                                              text_color="black", fg_color="orange", font=('montserrat', 17),
                                              command=lambda: self.pemastian_murid_nilai_tugas())
        self.button_ubah_ujian = ct.CTkButton(master=masterss, height=40, width=150, text='ubah nilai ujian',
                                              text_color="black", fg_color="orange", font=('montserrat', 17),
                                              command=lambda: self.pemastian_murid_nilai_ujian())
        self.button_cari.place(x=640, y=35)
        self.button_ubah_tugas.place(x=640, y=80)
        self.button_ubah_ujian.place(x=640, y=125)

    def pilihan_matkul(self):
        self.cari_pilihan_matkul = 'SELECT DISTINCT mata_pelajaran.mataPelajaran FROM mata_pelajaran'
        self.curr.execute(self.cari_pilihan_matkul)
        self.hasil_cari_pilihan_matkul = self.curr.fetchall()
        self.isi_pilihan_matkul = [self.hasil_cari_pilihan_matkul]

    def pilihan_kelas(self):
        self.cari_pilihan_kelas = 'SELECT DISTINCT kelas.kelas FROM kelas'
        self.curr.execute(self.cari_pilihan_kelas)
        self.hasil_cari_pilihan_kelas = self.curr.fetchall()
        self.isi_pilihan_kelas = [self.hasil_cari_pilihan_kelas]

    def konfirmasi_murid(self):
        self.apakah_ada = 'SELECT siswa.data_siswa.nis FROM siswa.data_siswa WHERE siswa.data_siswa.nis = %s'
        self.curr.execute(self.apakah_ada, (self.entry_id.get()))
        self.belum = self.curr.fetchall()
        try:
            for belum in self.belum:
                if self.entry_id.get() == belum:
                    self.nambah_data()
        except TypeError:
            self.murid_tidak_ada = messagebox.showerror("error", "Murid Tidak Ada")

    def pemastian_murid(self):
        self.cari_murid_nilai = 'SELECT * FROM siswa.nilai WHERE siswa.nilai.nis = %s AND siswa.nilai.matkul = %s AND siswa.nilai.kelas = %s'
        self.curr.execute(self.cari_murid_nilai,
                          args=(self.entry_id.get(), self.entry_id_matkul.get(), format(self.entry_id_kelas.get())))
        self.hasil_cari_murid_nilai = self.curr.fetchall()
        self.panjang_nilai_tugas = len(self.hasil_cari_murid_nilai)

    def execute_cari(self):
        self.cari_murid_nilai = 'SELECT * FROM siswa.nilai WHERE siswa.nilai.nis = %s AND siswa.nilai.matkul = %s AND siswa.nilai.kelas = %s'
        self.curr.execute(self.cari_murid_nilai,
                          args=(self.entry_id.get(), self.entry_id_matkul.get(), self.entry_id_kelas.get()))
        self.hasil_cari_murid_nilai = self.curr.fetchall()
        self.data_show(self.hasil_cari_murid_nilai)

    def ubah_nilai_tugas(self):
        self.cari_ubah_nilai_tugas = 'UPDATE siswa.nilai SET siswa.nilai.nilai_tugas = %s WHERE siswa.nilai.nis = %s AND siswa.nilai.matkul = %s AND siswa.nilai.kelas = %s'
        self.curr.execute(self.cari_ubah_nilai_tugas, args=(
        int(self.entry_nilai_tugas.get()), self.entry_id.get(), self.entry_id_matkul.get(), self.entry_id_kelas.get()))
        self.conn.commit()
        # self.berhasil_nilai_tugas = messagebox('berhasil', 'nilai tugas berhasil diubah')

    def ubah_nilai_ujian(self):
        self.cari_ubah_nilai_ujian = 'UPDATE siswa.nilai SET siswa.nilai.nilai_ujian = %s WHERE siswa.nilai.nis = %s AND siswa.nilai.matkul = %s AND siswa.nilai.kelas = %s'
        self.curr.execute(self.cari_ubah_nilai_ujian, args=(
        int(self.entry_nilai_ujian.get()), self.entry_id.get(), self.entry_id_matkul.get(), self.entry_id_kelas.get()))
        self.conn.commit()
        # self.berhasil_nilai_ujian = messagebox('berhasil', 'nilai ujian berhasil diubah')

    def pemastian_murid_nilai_ujian(self):
        self.pemastian_murid()
        if self.panjang_nilai_tugas != 0:
            self.konfirmasi_murid()
        self.ubah_nilai_ujian()
        self.hitung_rata_rata()
        self.execute_cari()

    def pemastian_murid_nilai_tugas(self):
        self.pemastian_murid()
        if self.panjang_nilai_tugas != 0:
            self.konfirmasi_murid()
        self.ubah_nilai_tugas()
        self.hitung_rata_rata()
        self.execute_cari()

    def pemastian_murid_nilai_cari(self):
        self.pemastian_murid()
        if self.panjang_nilai_tugas != 0:
            self.konfirmasi_murid()
        self.execute_cari()

    def nambah_data(self):
        self.cari_nama_murid = 'SELECT siswa.data_siswa.nama FROM siswa.data_siswa WHERE siswa.data_siswa.nis = %s'
        self.curr.execute(self.cari_nama_murid, args=(self.entry_id.get()))
        self.nama_murid_kasar = self.curr.fetchall()
        self.nama_murid = self.nama_murid_kasar[0]
        print(self.nama_murid)
        self.nambah_data_murid = 'INSERT INTO siswa.nilai (nis, nama, kelas, matkul, nilai_tugas, nilai_ujian, nilai_rata_rata) VALUES (%s,%s,%s,%s,0,0,0) '
        self.curr.execute(self.nambah_data_murid, args=(
        self.entry_id.get(), self.nama_murid, self.entry_id_kelas.get(), self.entry_id_matkul.get()))
        self.conn.commit()
        self.data_show()

    def hitung_rata_rata(self):
        try:
            self.nangkap_nilai_tugas = 'SELECT siswa.nilai.nilai_tugas,siswa.nilai.nilai_ujian FROM siswa.nilai WHERE siswa.nilai.nis = %s AND siswa.nilai.matkul = %s AND siswa.nilai.kelas = %s '
            self.curr.execute(self.nangkap_nilai_tugas,
                              args=(self.entry_id.get(), self.entry_id_matkul.get(), self.entry_id_kelas.get()))
            self.nilai_kasar = self.curr.fetchone()
            self.nilai_sekarang = self.nilai_kasar[0:]
            self.rata_rata_baru = st.mean(self.nilai_sekarang)
            self.update_rata_rata = 'UPDATE siswa.nilai SET siswa.nilai.nilai_rata_rata = %s WHERE siswa.nilai.nis = %s AND siswa.nilai.matkul = %s AND siswa.nilai.kelas = %s'
            self.curr.execute(self.update_rata_rata, args=(
                self.rata_rata_baru, self.entry_id.get(), self.entry_id_matkul.get(), self.entry_id_kelas.get()))
            self.conn.commit()
        except TypeError:
            self.tkinter.messagebox.showerror('Error','Data Tidak Ditemukan!!')

    def data_show(self, kasar):
        sample = kasar
        for lama in self.table.get_children():
            self.table.delete(lama)
        for isi in sample:
            self.table.insert('', self.tkinter.END, values=isi[0:])
        return sample

    def item_selected(event, self):
        for selected_item in self.table.selection():
            item = self.table.item(selected_item)
            record = item['values']
            # show a message
            self.showinfo(title='Information', message=','.join(record))

        self.table.bind('<<TreeviewSelect>>', self.item_selected)
    
