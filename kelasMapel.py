import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ct
import pymysql
import statistics as st


class kelasMapel(ct.CTkFrame):
    def __init__(self, curr, conn,master):
        super().__init__(master)
        self.curr = curr
        self.conn = conn
        self.font = ct.CTkFont(family='montserrat', size=17)
        # self.xonn = pymysql.connect(host='localhost', port=3306, user="root", password="", database="myschool",)
        self.xonn = pymysql.connect(host='db-myschool.cpsu4lo0ktjr.us-east-1.rds.amazonaws.com', port=3306, user="root", password="root12345", database="myschool",)
        self.showkelas = self.xonn.cursor()
        self.showkelas.execute("select * from kelas")
        self.showjadwal = self.xonn.cursor()
        self.showjadwal.execute("select * from jadwal")

    def uiKelasMapel(self, masterss):

        self.nama = ct.CTkLabel(master=masterss, text="nama Kelas", anchor="e", justify="right", width=60)
        self.font_kelas = ct.CTkFont('montserrat', 15)
        self.nama.configure(font=self.font_kelas)
        self.tingkat = ct.CTkLabel(master=masterss, text="tingkat kelas", anchor="e", justify="right", width=60,
                                   font=self.font_kelas)
        self.wali = ct.CTkLabel(master=masterss, text="wali kelas", anchor="e", justify="right", width=60,
                                font=self.font_kelas)
        self.ketua = ct.CTkLabel(master=masterss, text="ketua kelas", anchor="e", justify="right", width=60,
                                 font=self.font_kelas)
        self.jumlah = ct.CTkLabel(master=masterss, text="jumlah murid", anchor="e", justify="right", width=60,
                                  font=self.font_kelas)

        self.nama.place(x=50, y=40)
        self.tingkat.place(x=50, y=70)
        self.wali.place(x=50, y=100)
        self.ketua.place(x=50, y=130)
        self.jumlah.place(x=50, y=160)

        self.nama_var = tk.StringVar()
        self.tingkat_var = tk.StringVar()
        self.wali_var = tk.StringVar()
        self.ketua_var = tk.StringVar()
        self.jumlah_var = tk.StringVar()

        self.entry_nama = ct.CTkEntry(master=masterss, font=self.font_kelas, textvariable=self.nama_var, width=400)
        self.entry_nama.place(x=200, y=40)
        self.entry_tingkat = ct.CTkEntry(master=masterss, font=self.font_kelas, textvariable=self.tingkat_var,
                                         width=400)
        self.entry_tingkat.place(x=200, y=70)
        self.entry_wali = ct.CTkEntry(master=masterss, font=self.font_kelas, textvariable=self.wali_var, width=400)
        self.entry_wali.place(x=200, y=100)
        self.entry_ketua = ct.CTkEntry(master=masterss, font=self.font_kelas, textvariable=self.ketua_var, width=400)
        self.entry_ketua.place(x=200, y=130)
        self.entry_jumlah = ct.CTkEntry(master=masterss, font=self.font_kelas, textvariable=self.jumlah_var, width=400)
        self.entry_jumlah.place(x=200, y=160)

        self.columns = ('nama', 'tingkat', 'wali', 'ketua', 'jumlah')
        self.table = ttk.Treeview(master=masterss, columns=self.columns, show='headings', height=1000)
        self.table.heading('nama', text='nama kelas')
        self.table.column('nama', minwidth=0, width=150, stretch=False)
        self.table.heading('tingkat', text='tingkat kelas')
        self.table.column('tingkat', minwidth=0, width=120, stretch=False)
        self.table.heading('wali', text='wali kelas')
        self.table.column('wali', minwidth=0, width=150, stretch=False)
        self.table.heading('ketua', text='ketua kelas')
        self.table.column('ketua', minwidth=0, width=150, stretch=False)
        self.table.heading('jumlah', text='jumlah')
        self.table.column('jumlah', minwidth=0, width=160, stretch=False)
        
        self.refresh()

        self.table.pack()
        self.table.bind("<ButtonRelease-1>", self.on_tree_select)

        # self.table.place(x=70, y=350)
        self.table.place(relx=0.05, rely=0.4)

        self.button_save = ct.CTkButton(master=masterss, height=42, width=144, text='SAVE', fg_color="orange",
                                        hover_color="blue", font=('montserrat', 17), command=self.save)
        self.button_edit = ct.CTkButton(master=masterss, height=42, width=144, text='EDIT', fg_color="orange",
                                        hover_color="blue", font=('montserrat', 17), command=self.ubah_data)
        self.button_delete = ct.CTkButton(master=masterss, height=42, width=144, text='DELETE', fg_color="orange",
                                          hover_color="blue", font=('montserrat', 17), command=self.delete_data)
        self.button_save.place(x=655, y=40)
        self.button_edit.place(x=655, y=90)
        self.button_delete.place(x=655, y=140)


    def on_tree_select(self, event):
        selected_item = self.table.selection()
        if selected_item:
            item = self.table.item(selected_item)
            values = item["values"]
            self.entry_nama.delete(0, tk.END)
            self.entry_nama.insert(0, values[0])
            self.entry_tingkat.delete(0, tk.END) 
            self.entry_tingkat.insert(0, values[1])
            self.entry_wali.delete(0, tk.END)
            self.entry_wali.insert(0, values[2])
            self.entry_ketua.delete(0, tk.END)
            self.entry_ketua.insert(0, values[3])
            self.entry_jumlah.delete(0, tk.END)
            self.entry_jumlah.insert(0, values[4])

    def refresh(self):
        i = 0
        for ro in self.showkelas:
            self.table.insert("", i,text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4],))
            i = i + 1
    
    def read(self):
        self.curr.connection.ping()
        # sql = f"SELECT * FROM kelas ORDER BY 'nama_kelas' DESC"
        sql = f"SELECT * FROM kelas"
        self.curr.execute(sql)
        results = self.curr.fetchall()
        self.conn.commit()
        self.conn.close()
        return results

    def save(self):
        nama = str(self.entry_nama.get())
        tingkat = str(self.entry_tingkat.get())
        wali = str(self.entry_wali.get())
        ketua = str(self.entry_ketua.get())
        jumlah = str(self.entry_jumlah.get())
        if not (nama and nama.strip()) or not (tingkat and tingkat.strip()) or not (wali and wali.strip()) or not (
                ketua and ketua.strip()) or not (jumlah and jumlah.strip()):
            messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql = f"SELECT * FROM kelas WHERE 'nama_kelas'='{nama}' "
            self.curr.execute(sql, )
            checkNamaKelas = self.curr.fetchall()
            if len(checkNamaKelas) > 0:
                messagebox.showwarning("", "already use!")
                return
            if len(nama) < 5:
                messagebox.showwarning("", "Invalid Item Name")
            else:
                self.curr.connection.ping()
                sql = f"INSERT INTO kelas (`nama_kelas`, `tingkat_kelas`, `wali_kelas`, `ketua_kelas`, `jumlah`) VALUES ('{nama}','{tingkat}','{wali}','{ketua}','{jumlah}')"
                self.curr.execute(sql)
                messagebox.showwarning("", "Input Success")
            self.conn.commit()
            self.conn.close()
        except:
            messagebox.showwarning("", "error while save")
            return

    def ubah_data(self):
        nama = str(self.entry_nama.get())
        tingkat = str(self.entry_tingkat.get())
        wali = str(self.entry_wali.get())
        ketua = str(self.entry_ketua.get())
        jumlah = str(self.entry_jumlah.get())
        if not (nama and nama.strip()) or not (tingkat and tingkat.strip()) or not (wali and wali.strip()) or not (
                ketua and ketua.strip()) or not (jumlah and jumlah.strip()):
            messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql = f"SELECT * FROM kelas WHERE 'nama_kelas'='{nama}' "
            self.curr.execute(sql, )
            checkNamaKelas = self.curr.fetchall()
            if len(checkNamaKelas) > 0:
                messagebox.showwarning("", "already use!")
                return
            if len(nama) < 5:
                messagebox.showwarning("", "Invalid Item Name")
            else:
                self.curr.connection.ping()
                sql = f"UPDATE kelas SET 'tingkat_kelas' = '{tingkat}', 'wali_kelas' = '{wali}', 'ketua_kelas' = '{ketua}', 'jumlah' = '{jumlah}' WHERE 'nama_kelas' = '{nama}'')"
                self.curr.execute(sql, )
            self.conn.commit()
            self.conn.close()
        except:
            messagebox.showwarning("", "error while save")
            return

    def delete_data(self):
        nama = str(self.entry_nama.get())
        tingkat = str(self.entry_tingkat.get())
        wali = str(self.entry_wali.get())
        ketua = str(self.entry_ketua.get())
        jumlah = str(self.entry_jumlah.get())
        if not (nama and nama.strip()) or not (tingkat and tingkat.strip()) or not (wali and wali.strip()) or not (
                ketua and ketua.strip()) or not (jumlah and jumlah.strip()):
            messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql = f"SELECT * FROM kelas WHERE 'nama_kelas'='{nama}' "
            self.curr.execute(sql, )
            checkNamaKelas = self.curr.fetchall()
            if len(checkNamaKelas) > 0:
                messagebox.showwarning("", "already use!")
                return
            if len(nama) < 5:
                messagebox.showwarning("", "Invalid Item Name")
            else:
                self.curr.connection.ping()
                sql = f"DELETE FROM `kelas` WHERE `nama_kelas` = '{nama}'"
                self.curr.execute(sql, )
            self.conn.commit()
            self.conn.close()
        except:
            messagebox.showwarning("", "error while save")
            return