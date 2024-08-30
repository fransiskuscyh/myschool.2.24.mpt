import tkinter as tk
import tkinter
from tkinter import messagebox, ttk
import customtkinter as ct
import pymysql
import statistics as st


class mataPelajaranPengurus(ct.CTkFrame):
    def __init__(self, curr, conn,master):
        super().__init__(master)
        self.curr = curr
        self.conn = conn
        self.font_mataPelajaran = ct.CTkFont(family='montserrat', size=17)
        # self.xonn = pymysql.connect(host='localhost', port=3306, user="root", password="", database="myschool",)
        self.xonn = pymysql.connect(host='db-myschool.cpsu4lo0ktjr.us-east-1.rds.amazonaws.com', port=3306, user="root", password="root12345", database="myschool",)
        self.showMapel = self.xonn.cursor()
        self.showMapel.execute("select * from mata_pelajaran")

    def setup_uimatapelajaranPengurus(self, masterss):

        self.id = ct.CTkLabel(master=masterss, text="Kode Kelas", anchor="e", justify="right", width=60,
                              font=self.font_mataPelajaran)
        self.mataPelajaran = ct.CTkLabel(master=masterss, text="Mata Pelajaran", anchor="e", justify="right", width=60,
                                         font=self.font_mataPelajaran)
        self.pengajar = ct.CTkLabel(master=masterss, text="Pengajar", anchor="e", justify="right", width=60,
                                    font=self.font_mataPelajaran)

        self.id.place(x=50, y=40)
        self.mataPelajaran.place(x=50, y=70)
        self.pengajar.place(x=50, y=100)

        self.id_var = tk.StringVar()
        self.mataPelajaran_var = tk.StringVar()
        self.pengajar_var = tk.StringVar()

        self.entry_id = ct.CTkEntry(master=masterss, font=self.font_mataPelajaran, textvariable=self.id_var, width=400)
        self.entry_id.place(x=200, y=40)
        self.entry_mataPelajaran = ct.CTkEntry(master=masterss, font=self.font_mataPelajaran,
                                               textvariable=self.mataPelajaran_var, width=400)
        self.entry_mataPelajaran.place(x=200, y=70)
        self.entry_pengajar = ct.CTkEntry(master=masterss, font=self.font_mataPelajaran, textvariable=self.pengajar_var,
                                          width=400)
        self.entry_pengajar.place(x=200, y=100)

        self.columns = ('id', 'mataPelajaran', 'pengajar')
        self.table = ttk.Treeview(master=masterss, columns=self.columns, show='headings', height=1000)
        self.table.heading('id', text='Kode Kelas')
        self.table.column('id', minwidth=0, width=150, stretch=False)
        self.table.heading('mataPelajaran', text='MataPelajaran')
        self.table.column('mataPelajaran', minwidth=0, width=250, stretch=False)
        self.table.heading('pengajar', text='Pengajar')
        self.table.column('pengajar', minwidth=0, width=250, stretch=False)
        self.refreshTable()

        self.table.pack()
        self.table.bind("<ButtonRelease-1>", self.on_tree_select)

        self.table.place(relx=0.1, rely=0.35, anchor = tkinter.NW)

        self.button_save = ct.CTkButton(master=masterss, height=42, width=144, text='Save', fg_color="orange",
                                        hover_color="blue", font=('montserrat', 17), command=self.save)
        self.button_edit = ct.CTkButton(master=masterss, height=42, width=144, text='Edit', fg_color="orange",
                                        hover_color="blue", font=('montserrat', 17), command=self.ubah_data)
        self.button_delete = ct.CTkButton(master=masterss, height=42, width=144, text='Delete', fg_color="orange",
                                          hover_color="blue", font=('montserrat', 17), command=self.delete_data)
        self.button_cariId = ct.CTkButton(master=masterss,height=42,width=144,text='Cari ID', fg_color='orange',hover_color='blue',font=('montserrat', 17), command=lambda: self.cari_data(self.entry_id.get()))
        self.button_save.place(x=50, y=150)
        self.button_edit.place(x=250, y=150)
        self.button_delete.place(x=450, y=150)
        self.button_cariId.place(x=650, y=150)

    def read(self):
        self.curr.connection.ping()
        sql = f"SELECT * FROM mata_pelajaran"
        self.curr.execute(sql)
        results = self.curr.fetchall()
        self.conn.commit()
        self.conn.close()
        return results
    
    def on_tree_select(self, event):
        selected_item = self.table.selection()
        if selected_item:
            item = self.table.item(selected_item)
            values = item["values"]
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_mataPelajaran.delete(0, tk.END) 
            self.entry_mataPelajaran.insert(0, values[1])
            self.entry_pengajar.delete(0, tk.END) 
            self.entry_pengajar.insert(0, values[2])
            
    def refreshTable(self,):
        for data in self.table.get_children():
            self.table.delete(data)
        for x in self.showMapel:
            self.table.insert('', tkinter.END, values=x[0:])

    def save(self):
        id = str(self.entry_id.get())
        matapelajaran = str(self.entry_mataPelajaran.get())
        pengajar = str(self.entry_pengajar.get())
        if not (id and id.strip()) or not (matapelajaran and matapelajaran.strip()) or not (
                pengajar and pengajar.strip()):
            messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql = f"SELECT * FROM mata_pelajaran WHERE 'id'='{id}' "
            self.curr.execute(sql, )
            checkid = self.curr.fetchall()
            if len(checkid) > 0:
                messagebox.showwarning("", "already use!")
                return
            if len(id) < 3:
                messagebox.showwarning("", "Invalid Item ID")
            else:
                self.curr.connection.ping()
                sql = f"INSERT INTO mata_pelajaran (`id`, `mataPelajaran`, `pengajar`) VALUES ('{id}','{matapelajaran}','{pengajar}')"
                self.curr.execute(sql, )
                messagebox.showwarning("", "Input Success!")
            self.conn.commit()
            self.conn.close()
        except:
            messagebox.showwarning("", "error while save")
            return

    def ubah_data(self):
        id = str(self.entry_id.get())
        matapelajaran = str(self.entry_mataPelajaran.get())
        pengajar = str(self.entry_pengajar.get())
        if not (id and id.strip()) or not (matapelajaran and matapelajaran.strip()) or not (
                pengajar and pengajar.strip()):
            messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql = f"SELECT * FROM mata_pelajaran 'id'='{id}' "
            self.curr.execute(sql, )
            checkNamaKelas = self.curr.fetchall()
            if len(checkNamaKelas) > 0:
                messagebox.showwarning("", "already use!")
                return
            if len(id) < 5:
                messagebox.showwarning("", "Invalid Item ID")
            else:
                self.curr.connection.ping()
                sql = f"UPDATE mata_pelajaran SET 'mataPelajaran' = '{matapelajaran}', 'pengajar' = '{pengajar}'')"
                self.curr.execute(sql, )
                messagebox.showwarning("", "Edit Success!")
            self.conn.commit()
            self.conn.close()
        except:
            messagebox.showwarning("", "error while save")
            return

    def delete_data(self):
        id = str(self.entry_id.get())
        matapelajaran = str(self.entry_mataPelajaran.get())
        pengajar = str(self.entry_pengajar.get())
        if not (id and id.strip()) or not (matapelajaran and matapelajaran.strip()) or not (
                pengajar and pengajar.strip()):
            messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql = f"SELECT * FROM mata_pelajaran WHERE 'id'='{id}' "
            self.curr.execute(sql, )
            checkNamaKelas = self.curr.fetchall()
            if len(checkNamaKelas) > 0:
                messagebox.showwarning("", "already use!")
                return
            if len(id) < 3:
                messagebox.showwarning("", "Invalid Item ID")
            else:
                self.curr.connection.ping()
                sql = f"DELETE FROM `mata_pelajaran` WHERE `id` = '{id}'"
                self.curr.execute(sql, )
                messagebox.showwarning("", "Delete Success!")
            self.conn.commit()
            self.conn.close()
        except:
            messagebox.showwarning("", "error while save")
            return

    def cari_data(self,ID):
        if ID != '':
            try:
                sql1 = 'SELECT * FROM `mata_pelajaran` WHERE `mata_pelajaran`.id = (%s)'
                self.curr.execute(sql1, ID)
                hasil = self.curr.fetchall()
                self.refreshTable(hasil)
            except TypeError:
                tkinter.messagebox.showerror('Error', 'Data Tidak Ditemukan!')
        else:
            tkinter.messagebox.showerror('Error', 'Masukkan Data Yang Benar!')

    def cari_dataMatPel(self,Matpel):

        if Matpel != '':
            data = Matpel.title()
            try:
                sql1 = 'SELECT * FROM `mata_pelajaran` WHERE `mata_pelajaran`.mataPelajaran = (%s)'
                self.curr.execute(sql1, data)
                hasil = self.curr.fetchall()
                self.refreshTable(hasil)
            except TypeError:
                tkinter.messagebox.showerror('Error', 'Data Tidak Ditemukan!')
        else:
            tkinter.messagebox.showerror('Error', 'Masukkan Data Yang Benar!')

