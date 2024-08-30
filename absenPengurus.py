import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ct
import pymysql
import statistics as st


class absenPengurus(ct.CTkFrame):
    def __init__(self, curr, conn,master):
        super().__init__(master)
        self.curr = curr
        self.conn = conn
        self.font = ct.CTkFont(family='montserrat', size=17)   
        # self.xonn = pymysql.connect(host='localhost', port=3306, user="root", password="", database="myschool",)
        self.xonn = pymysql.connect(host='db-myschool.cpsu4lo0ktjr.us-east-1.rds.amazonaws.com', port=3306, user="root", password="root12345", database="myschool",)
        self.showAbsensi = self.xonn.cursor()
        self.showAbsensi.execute("select * from absensi")
        
    def uiAbsenPengurus(self, masterss):

        self.nis_murid = ct.CTkLabel(master=masterss, text="NIS Murid", anchor="e", justify="right", width=100)
        self.font = ct.CTkFont(family='montserrat', size=15)
        self.nis_murid.configure(font=self.font)
        self.nama_siswa = ct.CTkLabel(master=masterss, text="Nama Murid", anchor="e", justify="right", width=100)
        self.font = ct.CTkFont(family='montserrat', size=15)
        self.nama_siswa.configure(font=self.font)
        self.kelas_siswa = ct.CTkLabel(master=masterss, text="Kelas Murid", anchor="e", justify="right", width=100)
        self.font = ct.CTkFont(family='montserrat', size=15)
        self.kelas_siswa.configure(font=self.font)
        self.mapel_siswa = ct.CTkLabel(master=masterss, text="Mata Pelajaran", anchor="e", justify="right", width=100)
        self.font = ct.CTkFont(family='montserrat', size=15)
        self.mapel_siswa.configure(font=self.font)
        self.status_kehadiran = ct.CTkLabel(master=masterss, text="status kehadiran", anchor="e", justify="right", width=100)
        self.font = ct.CTkFont(family='montserrat', size=15)
        self.status_kehadiran.configure(font=self.font)

        self.nis_murid.place(x=20, y=40)
        self.nama_siswa.place(x=20, y=70)
        self.kelas_siswa.place(x=20, y=100)
        self.mapel_siswa.place(x=20, y=130)
        self.status_kehadiran.place(x=20, y=160)

        self.nis_murid_var = tk.StringVar()
        self.nama_siswa_var = tk.StringVar()
        self.kelas_var = tk.StringVar()
        self.matkul_var = tk.StringVar()
        self.status_var = tk.StringVar()

        self.entry_nis_murid = ct.CTkEntry(master=masterss, font=self.font, textvariable=self.nis_murid_var, width=500)
        self.entry_nis_murid.place(x=130, y=40)
        self.entry_nama_siswa = ct.CTkEntry(master=masterss, font=self.font, textvariable=self.nama_siswa_var, width=500)
        self.entry_nama_siswa.place(x=130, y=70)
        self.entry_kelas = ct.CTkEntry(master=masterss, font=self.font, textvariable=self.kelas_var, width=500)
        self.entry_kelas.place(x=130, y=100)
        self.entry_matkul = ct.CTkEntry(master=masterss, font=self.font, textvariable=self.matkul_var, width=500)
        self.entry_matkul.place(x=130, y=130)
        self.entry_status = ct.CTkEntry(master=masterss, font=self.font, textvariable=self.status_var, width=500)
        self.entry_status.place(x=130, y=160)

        self.columns = ('NIS', 'nama', 'kelas', 'mapel', 'status')
        self.table = ttk.Treeview(master=masterss, columns=self.columns, show='headings', height=300)
        self.table.heading('NIS', text='Nomor Induk Siswa')
        self.table.column('NIS', minwidth=0, width=120, stretch=False)
        self.table.heading('nama', text='Nama Siswa')
        self.table.column('nama', minwidth=0, width=120, stretch=False)
        self.table.heading('kelas', text='Kelas')
        self.table.column('kelas', minwidth=0, width=120, stretch=False)
        self.table.heading('mapel', text='Mata Pelajaran')
        self.table.column('mapel', minwidth=0, width=120, stretch=False)
        self.table.heading('status', text='Status Kehadiran')
        self.table.column('status', minwidth=0, width=120, stretch=False)
        self.refreshTable()
        self.table.pack()
        
        self.table.bind("<ButtonRelease-1>", self.on_tree_select)

        self.table.place(relx=0.17, rely=0.4)

        self.buttonSave = ct.CTkButton(master=masterss, height=44, width=150, text='Save', fg_color='#ff5f00',
                                        font=('montserrat', 17), command=lambda : self.save())
        self.buttonEdit = ct.CTkButton(master=masterss, height=44, width=150, text='Edit', fg_color='#0060ff',
                                        font=('montserrat', 17), command=lambda: self.Edit())
        self.buttonDelete = ct.CTkButton(master=masterss, height=44, width=150, text='Delete', fg_color='#0060ff',
                                        font=('montserrat', 17), command=lambda: self.Delete())
        self.buttonSave.place(x=655, y=40)
        self.buttonEdit.place(x=655, y=90)
        self.buttonDelete.place(x=655, y=140)

    def refreshTable(self):
        i = 0
        for ro in self.showAbsensi:
            self.table.insert("", i,text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4],))
            i = i + 1

    def on_tree_select(self, event):
        selected_item = self.table.selection()
        if selected_item:
            self.item = self.table.item(selected_item)
            values = self.item["values"]
            self.entry_nis_murid.delete(0, tk.END)
            self.entry_nis_murid.insert(0, values[0])
            self.entry_nama_siswa.delete(0, tk.END)
            self.entry_nama_siswa.insert(0, values[1])
            self.entry_kelas.delete(0, tk.END)
            self.entry_kelas.insert(0, values[2])
            self.entry_matkul.delete(0, tk.END)
            self.entry_matkul.insert(0, values[3])
            self.entry_status.delete(0, tk.END)
            self.entry_status.insert(0, values[4])

    def save(self):
        nisSiswa = str(self.entry_nis_murid.get())
        namaSiswa = str(self.entry_nama_siswa.get())
        kelasSiswa = str(self.entry_kelas.get())
        mapelSiswa = str(self.entry_matkul.get())
        statusKehadiran = str(self.entry_status.get())
        if not (nisSiswa and nisSiswa.strip()) or not (namaSiswa and namaSiswa.strip()) or not (kelasSiswa and kelasSiswa.strip()) or not (
                mapelSiswa and mapelSiswa.strip()) or not (statusKehadiran and statusKehadiran.strip()):
            messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql = f"SELECT * FROM absensi WHERE 'nis_siswa'='{nisSiswa}' "
            self.curr.execute(sql, )
            checknis = self.curr.fetchall()
            if len(checknis) > 0:
                messagebox.showwarning("", "already use!")
                return
            if len(namaSiswa) < 5:
                messagebox.showwarning("", "Invalid Item Name")
            else:
                self.curr.connection.ping()
                sql = f"INSERT INTO absensi (nis_siswa, nama_siswa, kelas_siswa, mapel_siswa, status_kehadiran) values ('{nisSiswa}', '{namaSiswa}', '{kelasSiswa}', '{mapelSiswa}', '{statusKehadiran}')"
                self.curr.execute(sql)
                messagebox.showwarning("", "Input Success")
            self.conn.commit()
            self.conn.close()
        except:
            messagebox.showwarning("", "error while save")
            return

    def Edit(self):
            nisSiswa = str(self.entry_nis_murid.get())
            namaSiswa = str(self.entry_nama_siswa.get())
            kelasSiswa = str(self.entry_kelas.get())
            mapelSiswa = str(self.entry_matkul.get())
            statusKehadiran = str(self.entry_status.get())
            if not (nisSiswa and nisSiswa.strip()) or not (namaSiswa and namaSiswa.strip()) or not (kelasSiswa and kelasSiswa.strip()) or not (
                    mapelSiswa and mapelSiswa.strip()) or not (statusKehadiran and statusKehadiran.strip()):
                messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
                return
            try:
                self.curr.connection.ping()
                sql = f"SELECT * FROM absensi WHERE 'nis_siswa'='{nisSiswa}' "
                self.curr.execute(sql, )
                checknis = self.curr.fetchall()
                if len(checknis) > 0:
                    messagebox.showwarning("", "already use!")
                    return
                if len(namaSiswa) < 5:
                    messagebox.showwarning("", "Invalid Item Name")
                else:
                    self.curr.connection.ping()
                    sql = f"UPDATE absensi SET 'kelas_siswa' = '{kelasSiswa}', 'mapel_siswa' = '{mapelSiswa}', 'status_kehadiran' = '{statusKehadiran}' WHERE 'nis_siswa' = '{nisSiswa}'')"
                    self.curr.execute(sql, )
                    messagebox.showwarning("", "Input Success")
                self.conn.commit()
                self.conn.close()
            except:
                messagebox.showwarning("", "error while save")
                return
            
    def Delete(self):
            nisSiswa = str(self.entry_nis_murid.get())
            namaSiswa = str(self.entry_nama_siswa.get())
            kelasSiswa = str(self.entry_kelas.get())
            mapelSiswa = str(self.entry_matkul.get())
            statusKehadiran = str(self.entry_status.get())
            if not (nisSiswa and nisSiswa.strip()) or not (namaSiswa and namaSiswa.strip()) or not (kelasSiswa and kelasSiswa.strip()) or not (
                    mapelSiswa and mapelSiswa.strip()) or not (statusKehadiran and statusKehadiran.strip()):
                messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
                return
            try:
                self.curr.connection.ping()
                sql = f"SELECT * FROM absensi WHERE 'nis_siswa'='{nisSiswa}' "
                self.curr.execute(sql, )
                checknis = self.curr.fetchall()
                if len(checknis) > 0:
                    messagebox.showwarning("", "already use!")
                else:
                    self.curr.connection.ping()
                    sql = f"DELETE FROM `absensi` WHERE `nis_siswa` = '{nisSiswa}'"
                    self.curr.execute(sql, )
                    messagebox.showwarning("", "Input Success")
                self.conn.commit()
                self.conn.close()
            except:
                messagebox.showwarning("", "error while save")
                return