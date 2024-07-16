import tkinter as tk
from tkinter import messagebox,ttk
import customtkinter as ct
from main import *
import statistics as st

class absen (ct.CTk):
    def __init__(self,curr,conn):
        super().__init__()
        self.curr = curr
        self.conn = conn
    

    def ui (self,masterss):
        #self.frame_absen = ct.CTkFrame(master=self, fg_color='#ccffff')
        #self.frame_absen.pack(fill='both',expand=True,anchor="e")
        
        self.nis_murid = ct.CTkLabel(master=masterss, text="NIS Murid",anchor="e",justify = "right",width=100)
        self.font = ct.CTkFont(family='montserrat', size=15)
        self.nis_murid.configure(font=self.font)
        
        self.nis_murid.place(x=20, y=60)
        
        self.nis_murid_var = tk.StringVar()
        
        self.entry_nis_murid = ct.CTkEntry(master=masterss, font=self.font, textvariable=self.nis_murid_var, width = 500)
        self.entry_nis_murid.place(x=130, y=60)
        
        self.columns = ('NIS', 'nama', 'kelas', 'mapel', 'status')
        self.table = ttk.Treeview(master=masterss, columns=self.columns, show='headings', height=300)
        self.table.heading('NIS', text='Nomor Induk Siswa')
        self.table.column('NIS', minwidth=0, width=80, stretch=False)
        self.table.heading('nama', text='Nama Siswa')
        self.table.column('nama', minwidth=0, width=120, stretch=False)
        self.table.heading('kelas', text='Kelas')
        self.table.column('kelas', minwidth=0, width=60, stretch=False)
        self.table.heading('mapel', text='Mata Pelajaran')
        self.table.column('mapel', minwidth=0, width=120, stretch=False)
        self.table.heading('status', text='Status Kehadiran')
        self.table.column('status', minwidth=0, width=140, stretch=False)

        self.table.place(x=140,y=270)

        self.button_cari = ct.CTkButton(master= masterss, height=80, width=150, text='Cari',fg_color='#0060ff', font=('montserrat',17), command=lambda :self.execute_cari())
        self.button_ubah = ct.CTkButton(master= masterss, height=80, width=150, text='Simpan',fg_color='#ff5f00', font=('montserrat',17), command= lambda : self.update_absen())
        self.button_cari.place(x=655, y=60)
        self.button_ubah.place(x=655, y=150)

        self.var = tk.StringVar()

        self.radiobutton_hadir = ct.CTkRadioButton(master=masterss, text="Hadir", font=self.font, variable=self.var,
                                                   value='H')
        self.radiobutton_hadir.place(x=130, y=195)
        self.radiobutton_alpha = ct.CTkRadioButton(master=masterss, text="Alpha", font=self.font, variable=self.var,
                                                   value='A')
        self.radiobutton_alpha.place(x=250, y=195)
        self.radiobutton_ijin = ct.CTkRadioButton(master=masterss, text="Ijin", font=self.font, variable=self.var,
                                                  value='I')
        self.radiobutton_ijin.place(x=370, y=195)
        self.radiobutton_sakit = ct.CTkRadioButton(master=masterss, text="Sakit", font=self.font, variable=self.var,
                                                   value='S')
        self.radiobutton_sakit.place(x=490, y=195)


        self.cari_mapel = 'SELECT mataPelajaran FROM `mata_pelajaran`'
        self.curr.execute(self.cari_mapel)
        self.hasil_mapel = self.curr.fetchall()
        self.isi_mapel = [item[0] for item in self.hasil_mapel]

        self.cari_kelas = 'SELECT nama_kelas FROM `kelas`'
        self.curr.execute(self.cari_kelas)
        self.hasil_kelas = self.curr.fetchall()
        self.isi_kelas = [item[0] for item in self.hasil_kelas]

        self.var_kelas = tk.StringVar()
        self.var_matkul = tk.StringVar()


        self.combobox_kelas = ct.CTkComboBox(master=masterss, values=self.isi_kelas, width=225, font=self.font, variable=self.var_kelas)
        self.combobox_matkul = ct.CTkComboBox(master=masterss, values=self.isi_mapel, width=225, font=self.font, variable= self.var_matkul)
        self.combobox_kelas.set('pilih kelas')
        self.combobox_matkul.set('pilih mata pelajaran')
        self.combobox_kelas.place(x=130, y=110)
        self.combobox_matkul.place(x=380, y=110)

    def execute_cari(self):
        self.cari_murid = 'SELECT * FROM siswa.absensi WHERE siswa.absensi.nis_siswa = %s AND siswa.absensi.mapel_siswa = %s AND siswa.absensi.kelas_siswa = %s'
        self.curr.execute(self.cari_murid, args = (self.entry_nis_murid.get(), self.combobox_matkul.get(), self.combobox_kelas.get()))
        self.hasil_cari = self.curr.fetchall()
        print(self.hasil_cari)
        self.data_show(self.hasil_cari)

    def data_show(self,kasar):
        sample = kasar
        for lama in self.table.get_children():
            self.table.delete(lama)
        for isi in sample:
            self.table.insert('', tk.END, values=isi[0:])
        return sample

    def item_selected(event):
        for selected_item in self.table.selection():
            item = self.table.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

        self.table.bind('<<TreeviewSelect>>', item_selected)

    def update_absen(self):
        self.update_kehadiran = 'UPDATE siswa.absensi SET siswa.absensi.status_kehadiran = %s WHERE siswa.absensi.nis_siswa = %s AND siswa.absensi.kelas_siswa = %s AND siswa.absensi.mapel_siswa = %s'
        self.curr.execute(self.update_kehadiran, args = (self.var.get(), self.entry_nis_murid.get(), self.combobox_kelas.get(), self.combobox_matkul.get()))
        self.conn.commit()
        print(self.var.get())
        self.execute_cari()


        
    

    
