import tkinter as tk
from tkinter import messagebox,ttk
import tkinter
import customtkinter as ct
import pymysql
import statistics as st

class Nilai (ct.CTkFrame):
    def __init__(self,curr,conn,master):
        super().__init__(master)

        # self.conn = pymysql.connect(host='localhost', port=3306, user="root", password="", database="myschool",)
        self.conn = pymysql.connect(host='db-myschool.cpsu4lo0ktjr.us-east-1.rds.amazonaws.com', port=3306, user="root", password="root12345", database="myschool",)
        self.showNilai = self.conn.cursor()
        self.showNilai.execute("select * from nilai")
        self.curr = curr
        self.conn = conn
        self.font = ct.CTkFont(family='montserrat', size=17)


    def setup_ui(self,masterss):

        self.id = ct.CTkLabel(master=masterss, text="NIS murid", anchor="e", justify="right", width=100)
        self.font_nilai = ct.CTkFont('montserrat', 15)
        self.id.configure(font=self.font_nilai)
        self.nama = ct.CTkLabel(master=masterss, text="Nama murid", anchor="e", justify="right", width=100,
                              font=self.font_nilai)
        self.kelas = ct.CTkLabel(master=masterss, text="Kelas", anchor="e", justify="right", width=100,
                                    font=self.font_nilai)
        self.matkul = ct.CTkLabel(master=masterss, text="Matkul", anchor="e", justify="right", width=100,
                                     font=self.font_nilai)
        self.nilai_tugas = ct.CTkLabel(master=masterss, text="Nilai tugas", anchor="e", justify="right", width=100,
                                       font=self.font_nilai)
        self.nilai_ujian = ct.CTkLabel(master=masterss, text="Nilai ujian", anchor="e", justify="right", width=100,
                                       font=self.font_nilai)
        self.rata_rata = ct.CTkLabel(master=masterss, text="Nilai rata rata", anchor="e", justify="right", width=100,
                                       font=self.font_nilai)

        self.id.place(x=10, y=35)
        self.nama.place(x=10, y=60)
        self.kelas.place(x=10, y=85)
        self.matkul.place(x=10, y=110)
        self.nilai_tugas.place(x=10, y=135)
        self.nilai_ujian.place(x=10, y=160)
        self.rata_rata.place(x=10, y=185)

        self.id_var = tk.StringVar()
        self.nama_var = tk.StringVar()
        self.id_kelas_var = tk.StringVar()
        self.id_matkul_var = tk.StringVar()
        self.nilai_tugas_var = tk.StringVar()
        self.nilai_ujian_var = tk.StringVar()
        self.rata_rata_var = tk.StringVar()

        self.entry_id = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_var, width=500)
        self.entry_id.place(x=120, y=35)
        self.entry_nama = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.nama_var, width=500)
        self.entry_nama.place(x=120, y=60)
        self.entry_kelas = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_kelas_var,
                                          width=500)
        self.entry_kelas.place(x=120, y=85)
        self.entry_matkul = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_matkul_var,
                                           width=500)
        self.entry_matkul.place(x=120, y=110)
        self.entry_nilai_tugas = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.nilai_tugas_var,
                                             width=500)
        self.entry_nilai_tugas.place(x=120, y=135)
        self.entry_nilai_ujian = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.nilai_ujian_var,
                                             width=500)
        self.entry_nilai_ujian.place(x=120, y=160)
        self.entry_rata_rata = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.rata_rata_var,
                                             width=500)
        self.entry_rata_rata.place(x=120, y=185)

        self.columns = ('id', 'nama', 'kelas', 'matkul', 'nilai tugas', 'nilai ujian', 'rata rata')
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
        self.table.heading('rata rata', text='Rata Rata')
        self.table.column('rata rata', minwidth=0, width=100, stretch=False)
        self.refreshTable()
        self.table.bind("<ButtonRelease-1>", self.on_tree_select)

        # self.table.place(x=80, y=280)
        self.table.place(relx=0.05, rely=0.38)

        self.buttonSearch = ct.CTkButton(master=masterss, height=40, width=150, text='Search', fg_color="#00df00",
                                        font=('montserrat', 17), command=lambda: self.pemastian_murid_nilai_cari())
        self.buttonSave = ct.CTkButton(master=masterss, height=40, width=150, text='Save',
                                              text_color="black", fg_color="orange", font=('montserrat', 17),
                                              command=lambda: self.save())
        self.buttonEdit = ct.CTkButton(master=masterss, height=40, width=150, text='Edit',
                                              text_color="black", fg_color="orange", font=('montserrat', 17),
                                              command=lambda: self.edit())
        self.buttonDelete = ct.CTkButton(master=masterss, height=40, width=150, text='Delete',
                                              text_color="black", fg_color="orange", font=('montserrat', 17),
                                              command=lambda: self.delete())
        self.buttonSearch.place(x=640, y=35)
        self.buttonSave.place(x=640, y=80)
        self.buttonEdit.place(x=640, y=125)
        self.buttonDelete.place(x=640, y=170)

    def refreshTable(self,):
        for data in self.table.get_children():
            self.table.delete(data)
        for x in self.showNilai:
            self.table.insert('', tkinter.END, values=x[0:])
            
    def on_tree_select(self, event):
        selected_item = self.table.selection()
        if selected_item:
            item = self.table.item(selected_item)
            values = item["values"]
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_nama.delete(0, tk.END) 
            self.entry_nama.insert(0, values[1])
            self.entry_kelas.delete(0, tk.END) 
            self.entry_kelas.insert(0, values[2])
            self.entry_matkul.delete(0, tk.END) 
            self.entry_matkul.insert(0, values[3])
            self.entry_nilai_tugas.delete(0, tk.END) 
            self.entry_nilai_tugas.insert(0, values[4])
            self.entry_nilai_ujian.delete(0, tk.END) 
            self.entry_nilai_ujian.insert(0, values[5])
            self.entry_rata_rata.delete(0, tk.END) 
            self.entry_rata_rata.insert(0, values[6])

    def save(self):
            id = str(self.entry_id.get())
            nama = str(self.entry_nama.get())
            kelas = str(self.entry_kelas.get())
            matkul = str(self.entry_matkul.get())
            nilai_tugas = str(self.entry_nilai_tugas.get())
            nilai_ujian = str(self.entry_nilai_ujian.get())
            rata_rata = str(self.entry_rata_rata.get())
            if not (id and id.strip()) or not (nama and nama.strip()) or not (
                    kelas and kelas.strip()) or not (
                    matkul and matkul.strip()) or not (
                    nilai_tugas and nilai_tugas.strip()) or not (
                    nilai_ujian and nilai_ujian.strip()) or not (
                    rata_rata and rata_rata.strip()):
                messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
                return
            try:
                self.curr.connection.ping()
                sql = f"SELECT * FROM nilai WHERE 'nis'='{id}' "
                self.curr.execute(sql, )
                checkid = self.curr.fetchall()
                if len(checkid) > 0:
                    messagebox.showwarning("", "already use!")
                    return
                if len(id) < 5:
                    messagebox.showwarning("", "Invalid Item ID")
                else:
                    self.curr.connection.ping()
                    sql = f"INSERT INTO nilai (nis, nama, kelas, matkul, nilai_tugas, nilai_ujian, nilai_rata_rata) VALUES ('{id}', '{nama}', '{kelas}', '{matkul}', '{nilai_tugas}', '{nilai_ujian}', '{rata_rata}')"
                    self.curr.execute(sql, )
                    messagebox.showwarning("", "Input Success!")
                    self.conn.commit()
                    self.conn.close()
            except:
                messagebox.showwarning("", "error while save")
                return

    def edit(self):
        id = str(self.entry_id.get())
        nama = str(self.entry_nama.get())
        kelas = str(self.entry_kelas.get())
        matkul = str(self.entry_matkul.get())
        nilai_tugas = str(self.entry_nilai_tugas.get())
        nilai_ujian = str(self.entry_nilai_ujian.get())
        rata_rata = str(self.entry_rata_rata.get())
        if not (id and id.strip()) or not (nama and nama.strip()) or not (
                kelas and kelas.strip()) or not (
                matkul and matkul.strip()) or not (
                nilai_tugas and nilai_tugas.strip()) or not (
                nilai_ujian and nilai_ujian.strip()) or not (
                rata_rata and rata_rata.strip()):
            messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql = f"SELECT * FROM nilai 'nis'='{id}' "
            self.curr.execute(sql, )
            checknilaiId = self.curr.fetchall()
            if len(checknilaiId) > 0:
                messagebox.showwarning("", "already use!")
                return
            if len(id) < 5:
                messagebox.showwarning("", "Invalid Item ID")
            else:
                self.curr.connection.ping()
                sql = f"UPDATE nilai SET 'nilai_tugas' = '{nilai_tugas}', 'nilai_ujian' = '{nilai_ujian}'"
                self.curr.execute(sql, )
                messagebox.showwarning("", "Edit Success!")
            self.conn.commit()
            self.conn.close()
        except:
            messagebox.showwarning("", "error while save")
            return
        

    def delete(self):
        id = str(self.entry_id.get())
        nama = str(self.entry_nama.get())
        kelas = str(self.entry_kelas.get())
        matkul = str(self.entry_matkul.get())
        nilai_tugas = str(self.entry_nilai_tugas.get())
        nilai_ujian = str(self.entry_nilai_ujian.get())
        rata_rata = str(self.entry_rata_rata.get())
        if not (id and id.strip()) or not (nama and nama.strip()) or not (
                    kelas and kelas.strip()) or not (
                    matkul and matkul.strip()) or not (
                    nilai_tugas and nilai_tugas.strip()) or not (
                    nilai_ujian and nilai_ujian.strip()) or not (
                    rata_rata and rata_rata.strip()):
            messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql = f"SELECT * FROM nilai WHERE 'nis'='{id}' "
            self.curr.execute(sql, )
            checknilaiId = self.curr.fetchall()
            if len(checknilaiId) > 0:
                messagebox.showwarning("", "already use!")
                return
            if len(id) < 5:
                messagebox.showwarning("", "Invalid Item ID")
            else:
                self.curr.connection.ping()
                sql = f"DELETE FROM nilai WHERE `nis` = '{id}'"
                self.curr.execute(sql, )
                messagebox.showwarning("", "Delete Success!")
            self.conn.commit()
            self.conn.close()
        except:
            messagebox.showwarning("", "error while save")
            return