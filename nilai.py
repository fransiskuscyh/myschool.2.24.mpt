import tkinter as tk
from tkinter import messagebox,ttk
import customtkinter as ct
from main import *
import statistics as st
dbApp = mainDB()
conn_dbApp, curr_dbApp = dbApp.connect()

class Nilai (ct.CTk):
    def __init__(self,curr,conn):
        super().__init__()


        self.curr = curr
        self.conn = conn
        self.font = ct.CTkFont(family='montserrat', size=17)


    def setup_ui(self,masterss):


        self.nama = ct.CTkLabel(master=masterss,fg_color= '#ccffff', text="nama murid",anchor="e",justify = "right",width=60)
        self.font_nilai = ct.CTkFont('montserrat',15)
        self.nama.configure(font=self.font_nilai)
        self.id = ct.CTkLabel(master=masterss,fg_color= '#ccffff',text="id murid",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.id_kelas = ct.CTkLabel(master=masterss,fg_color= '#ccffff',text="id kelas",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.id_matkul = ct.CTkLabel(master=masterss,fg_color= '#ccffff',text="matkul",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.nilai_tugas = ct.CTkLabel(master=masterss,fg_color= '#ccffff',text="nilai tugas",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.nilai_ujian = ct.CTkLabel(master=masterss,fg_color= '#ccffff',text="nilai ujian",anchor="e",justify = "right",width=60,font=self.font_nilai)
        #self.nilai_rata_rata = ct.CTkLabel(master=self,fg_color= '#ccffff',text="rata-rata",anchor="e",justify = "right",width=110,font=('montserrat',17))
        
        self.nama.place(x=180, y=40)
        self.id.place(x=180, y=70)
        self.id_kelas.place(x=180, y=100)
        self.id_matkul.place(x=180, y=130)
        self.nilai_tugas.place(x=180, y=160)
        self.nilai_ujian.place(x=180, y=190)
        #self.nilai_rata_rata.place(x=285, y=340)

        self.nama_var = tk.StringVar()
        #self.nama_var.trace_add(self.create_message)
        self.id_var = tk.StringVar()
        self.id_kelas_var = tk.StringVar()
        self.id_matkul_var = tk.StringVar()
        self.nilai_tugas_var = tk.StringVar()
        self.nilai_ujian_var = tk.StringVar()

        self.entry_nama = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.nama_var, width = 400)
        self.entry_nama.place(x=250, y=40)
        #printing_nama = str(self.nama_var.get())
        #self.label_nama = ct.CTkLabel(master=self, text = printing_nama, font=('montserrat',17))
        #self.label_nama.place(x=405, y=130)
        self.entry_id = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_var, width = 400)
        self.entry_id.place(x=250, y=70)
        #printing_id = str(self.id_var.get())
        ##self.label_id = ct.CTkLabel(master=self, text = printing_id, font=('montserrat',17))
        #self.label_id.place(x=405, y=130)
        self.entry_id_kelas = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_kelas_var, width = 400)
        self.entry_id_kelas.place(x=250, y=100)
        self.entry_id_matkul = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_matkul_var, width = 400)
        self.entry_id_matkul.place(x=250, y=130)
        self.entry_nilai_tugas = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.nilai_tugas_var, width = 400)
        self.entry_nilai_tugas.place(x=250, y=160)
        self.entry_nilai_ujian = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.nilai_ujian_var, width = 400)
        self.entry_nilai_ujian.place(x=250, y=190)

        self.columns = ('id', 'nama', 'kelas', 'matkul', 'nilai tugas', 'nilai ujian', 'rata-rata')
        self.table = ttk.Treeview(master=masterss, columns=self.columns, show='headings', height=1000)
        self.table.heading('id', text='ID')
        self.table.column('id', minwidth=0, width=60, stretch=False)
        self.table.heading('nama', text='Nama')
        self.table.column('nama', minwidth=0, width=100, stretch=False)
        self.table.heading('kelas', text='Kelas')
        self.table.column('kelas', minwidth=0, width=60, stretch=False)
        self.table.heading('matkul', text='Matkul')
        self.table.column('matkul', minwidth=0, width=100, stretch=False)
        self.table.heading('nilai tugas', text='Nilai Tugas')
        self.table.column('nilai tugas', minwidth=0, width=80, stretch=False)
        self.table.heading('nilai ujian', text='Nilai Ujian')
        self.table.column('nilai ujian', minwidth=0, width=80, stretch=False)
        self.table.heading('rata-rata', text='Rata-Rata')
        self.table.column('rata-rata', minwidth=0, width=80, stretch=False)

        self.table.place(x=140,y=250)

        self.button_cari = ct.CTkButton(master= masterss, height=80, width=150, text='cari', fg_color="#00df00", font=('montserrat',17), command=lambda: self.konfirmasi_murid())
        self.button_ubah = ct.CTkButton(master= masterss, height=80, width=150, text='ubah', fg_color="#ff7500", font=('montserrat',17))
        self.button_cari.place(x=670, y=40)
        self.button_ubah.place(x=670, y=140)

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
        self.apakah_ada = 'SELECT data_siswa.nis FROM data_siswa WHERE data_siswa.nama = (%s)'
        self.curr.execute(self.apakah_ada, (self.entry_id.get()))
        self.belum = self.curr.fetchall()
        if self.entry_id.get() in self.belum:
            self.nambah_data()
        else:
            self.murid_tidak_ada = messagebox.showerror("error", "Murid Tidak Ada")

    def pemastian_murid (self):
        self.cari_murid_nilai = 'SELECT * FROM nilai WHERE nilai.nis = (%s) AND nilai.matkul = (%s) AND nilai.kelas = {}'.format(self.entry_id_kelas.get())
        self.curr.execute(self.cari_murid_nilai, args = (self.entry_id.get(), self.entry_id_matkul.get()))
        self.hasil_cari_murid_nilai = self.curr.fetchall()
        self.panjang_nilai_tugas = len(self.hasil_cari_murid_nilai)

    def execute_cari(self):
        self.execute_cari_id = 'SELECT DISTINCT data_siswa.nis, data_siswa.nama, data_siswa.kelas, mata_pelajaran.mataPelajaran FROM nilai LEFT JOIN data_siswa ON %s = data_siswa.nis LEFT JOIN mata_pelajaran ON %s = mata_pelajaran.mataPelajaran LEFT JOIN data_siswa ON %s = data_siswa.kelas'
        self.curr.execute(self.execute_cari_id, args=(self.entry_id.get(), self.entry_id_matkul.get(), self.entry_id_kelas.get()))
        self.kasar = self.curr.fetchall()
        self.data_show()

    def ubah_nilai_tugas(self):
        self.cari_ubah_nilai_tugas = 'UPDATE nilai SET nilai.nilai_tugas = %s WHERE nilai.nis = %s AND nilai.matkul = %s AND nilai.kelas = %s'
        self.curr.execute(self.cari_ubah_nilai_tugas, args = (int(self.entry_nilai_tugas.get()), self.entry_id.get(),self.entry_id_matkul.get(), self.entry_id_kelas.get()))
        self.conn.commit()
        self.berhasil_nilai_tugas = messagebox('berhasil', 'nilai tugas berhasil diubah')
    
    def ubah_nilai_ujian(self):
        self.cari_ubah_nilai_ujian = 'UPDATE nilai SET nilai.nilai_ujian = %s WHERE nilai.nis = %s AND nilai.matkul = %s AND nilai.kelas = %s'
        self.curr.execute(self.cari_ubah_nilai_ujian, args = (int(self.entry_nilai_ujian.get()), self.entry_id.get(),self.entry_id_matkul.get(), self.entry_id_kelas.get()))
        self.conn.commit()
        self.berhasil_nilai_ujian = messagebox('berhasil', 'nilai ujian berhasil diubah')

    def pemastian_murid_nilai_ujian (self):
        self.pemastian_murid()
        if self.panjang_nilai_tugas != 0:
            self.konfirmasi_murid()
        self.ubah_nilai_ujian()
        self.hitung_rata_rata()
        self.data_show()

    def pemastian_murid_nilai_tugas (self):
        self.pemastian_murid()
        if self.panjang_nilai_tugas != 0:
            self.konfirmasi_murid()
        self.ubah_nilai_tugas()
        self.hitung_rata_rata()
        self.data_show()
    
    def pemastian_murid_nilai_cari (self):
        self.pemastian_murid()        
        if self.panjang_nilai_tugas != 0:
            self.konfirmasi_murid()
        self.execute_cari()

    def nambah_data(self):
        self.execute_cari_id = 'SELECT DISTINCT data_siswa.nis, data_siswa.nama, data_siswa.kelas, mata_pelajaran.mataPelajaran FROM nilai LEFT JOIN data_siswa ON %s = data_siswa.nis LEFT JOIN mata_pelajaran ON %s = mata_pelajaran.mataPelajaran LEFT JOIN data_siswa ON %s = data_siswa.kelas'
        self.curr.execute(self.execute_cari_id, args=(self.entry_id.get(), self.entry_id_matkul.get(), self.entry_id_matkul.get()))
        self.kasar = self.curr.fetchall()
        self.nambah_data_murid = 'INSERT INTO nilai (nis, nama, kelas, matkul) VALUES %s '
        self.curr.execute(self.execute_cari_id, args=(self.kasar))
        self.conn.commit()
        self.data_show()

    def hitung_rata_rata(self):
        self.nangkap_nilai = 'SELECT nilai.nilai_tugas, nilai.nilai_ujian FROM nilai WHERE nilai.nis = %s AND nilai.matkul = %s AND nilai.kelas = %s '
        self.curr.execute(self.nangkap_nilai, args = (self.entry_id.get(), self.entry_id_matkul.get(), self.entry_id_kelas.get()))
        self.nilai_kasar = self.curr.fetchall()
        self.nilai_sekarang = self.nilai_kasar[0]
        self.rata_rata_baru = st.mean(self.nilai_sekarang)
        self.update_rata_rata = 'UPDATE nilai SET nilai.nilai_rata_rata = %s WHERE nilai.nis = %s AND nilai.matkul = %s AND nilai.kelas = %s'
        self.curr.execute(self.update_rata_rata, args = (self.rata_rata_baru,self.entry_id.get(), self.entry_id_matkul.get(), self.entry_id_kelas.get()))
        self.conn.commit()
        
    #def ubah_nilai_ujian(self):
        #self.mengubah_nilai = 'UPDATE nilai SET nilai_ujian = %s WHERE nilai.nis = %s'
        #self.curr.execute(self.mengubah_nilai, args=(self.entry_nilai_ujian.get(), self.entry_id.get()))

    #def murid_tidak_ada(self):


    def data_show(self):
        sample = self.kasar
        for lama in self.table.get_children():
            self.table.delete(lama)
        for isi in sample:
            self.table.insert('', tkinter.END, values=isi[0:])
        return sample,isi

    def item_selected(event):
        for selected_item in self.table.selection():
            item = self.table.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))


        self.table.bind('<<TreeviewSelect>>', item_selected)
    
