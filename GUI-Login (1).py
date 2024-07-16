import tkinter
from tkinter import messagebox

import customtkinter
import customtkinter as ct
from PIL import ImageTk, Image
from main import *
from nilai import *
from kelasv8 import *
from absen import *
from mataPel2 import * 


class Login():
    def __init__(self, curr, conn):
        self.curr = curr
        self.conn = conn

    def loginin(self, username, password):
        try:
            entered_username = username
            entered_password = password
            sql_user = "SELECT `username` FROM `user_account` WHERE `username` = (%s)"
            self.curr.execute(sql_user, username)
            user_pop = self.curr.fetchone()
            for x in user_pop:
                self.userzz = x

            sql_password = "SELECT `user_password` FROM `user_account` WHERE `username` = (%s)"
            self.curr.execute(sql_password, username)
            password_pop = self.curr.fetchone()
            for x in password_pop:
                passwordzz = x

            if username == self.userzz and password == passwordzz:
                tkinter.messagebox.showinfo("Login", "Login successful!")
                root.menu_siswa()


            elif entered_username != self.userzz and entered_password != passwordzz:
                tkinter.messagebox.showerror("Login Error", "Invalid username or password")
        except TypeError:
            tkinter.messagebox.showerror("Login Error", "Invalid username or password")

    def resetPassword(self,username,password,passlama):
        try:
            if password != '':
                entered_passlama = passlama
                entered_password = password
                sql_user = "SELECT `username` FROM `user_account` WHERE `username` = (%s)"
                self.curr.execute(sql_user, username)
                user_pop = self.curr.fetchone()
                for x in user_pop:
                    self.userzz = x

                sql_password = "SELECT `user_password` FROM `user_account` WHERE `username` = (%s)"
                self.curr.execute(sql_password, username)
                password_pop = self.curry.fetchone()
                for x in password_pop:
                    passwordzz = x

                if entered_password == passwordzz:
                    self.curr.execute('UPDATE `user_account` SET `user_password`=(%s) WHERE `username` = (%s)',
                                      (entered_passlama, username))
                    self.conn.commit()
                    tkinter.messagebox.showinfo("Berhasil", "Password Diganti!")

                elif entered_password != passwordzz:
                    tkinter.messagebox.showerror("Error", "Invalid Password")
            else:
                tkinter.messagebox.showerror("Error", "Tidak Bisa Kosong!")
        except TypeError:
            tkinter.messagebox.showerror("Error", "Invalid Password")

    def pengurusLogin(self,username,password):
        entered_username = username
        entered_password = password
        sql_user = "SELECT `username` FROM `user_account` WHERE `username` = (%s)"
        self.curr.execute(sql_user, entered_username)
        user_pop = self.curr.fetchone()
        for x in user_pop:
            self.userzz = x

        sql_password = "SELECT `user_password` FROM `user_account` WHERE `username` = (%s)"
        self.curr.execute(sql_password, entered_username)
        password_pop = self.curry.fetchone()
        for x in password_pop:
            passwordzz = x

        if entered_username == self.userzz and entered_password == passwordzz:
            tkinter.messagebox.showinfo("Login", "Login successful!")
            username_login = self.userzz
            root.menu_pengurus()


        elif entered_username != self.userzz and entered_password != passwordzz:
            tkinter.messagebox.showerror("Login Error", "Invalid username or password")

dbApp = mainDB()
conn_dbApp, curr_dbApp = dbApp.connect()
myschool_login = Login(curr_dbApp,conn_dbApp)
myschool_nilai = Nilai(curr_dbApp,conn_dbApp)
myschool_kelas = kelas(curr_dbApp,conn_dbApp)
myschool_absen = absen(curr_dbApp,conn_dbApp)
myschool_mapel = mataPelajaran(curr_dbApp,conn_dbApp)


customtkinter.set_appearance_mode('light')

class MySchoolApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.title("MySchool")
        self.geometry('1000x600')
        self.resizable(0,0)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3,4), weight=1)
        self.background_GUI()

    def background_GUI(self):
        for i in self.winfo_children():
            i.destroy()

        self.backframez = ct.CTkFrame(master=self, width=400, height=600, fg_color='orange', corner_radius=0)
        self.backframez.place(rely=0,relx=1,anchor=tkinter.NE)

        #img = Image.open('siswa_art.png')
       # new_size = (650, 650)
      #  img_resized = img.resize(new_size)
      #  img_tk = ImageTk.PhotoImage(img_resized)
     #   self.background_label = ct.CTkLabel(master=self, image=img_tk, text="")
     #   self.background_label.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)
        self.loginFrame()

    def loginFrame(self):
        self.loginzframe = ct.CTkFrame(master=self.backframez, width=300, height=500, fg_color='blue', corner_radius=15)
        self.loginzframe.place(rely=0.5,relx=0.5, anchor=tkinter.CENTER)

        self.username_entry = ct.CTkEntry(master=self.loginzframe, width=200, height=30, fg_color='white', text_color='black')
        self.username_entry.place(relx=0.5, rely=0.31, anchor = tkinter.CENTER)

        self.username_label =ct.CTkLabel(master=self.loginzframe, text_color='white', text='Username')
        self.username_label.place(relx=0.17, rely=0.25, anchor = tkinter.W)

        self.password_label = ct.CTkLabel(master=self.loginzframe, text_color='white', text='Password')
        self.password_label.place(relx=0.17, rely=0.375, anchor=tkinter.W)

        self.password_entry = ct.CTkEntry(master=self.loginzframe, width=200, height=30, fg_color='white',
                                          text_color='black', show='*')
        self.password_entry.place(relx=0.5, rely=0.435, anchor=tkinter.CENTER)

        self.login_button = ct.CTkButton(master=self.loginzframe, width=75, height=30, fg_color='brown', text='Login', command=lambda : myschool_login.loginin(self.username_entry.get(),self.password_entry.get()))
        self.login_button.place(relx=0.5, rely=0.55, anchor = tkinter.CENTER)

    def menu_siswa(self):
        self.backframez.destroy()
       # self.background_label.destroy()
        self.listMenuSiswa()
        self.profileSiswa()

    def listMenuSiswa(self):
        self.menu_siswaFrame = ct.CTkFrame(master=self, width=170, height=600, corner_radius=0, fg_color='blue')
        self.menu_siswaFrame.pack(padx=0, pady=0, anchor=tkinter.W)
        self.profileButton = ct.CTkButton(master=self.menu_siswaFrame, width=120, height=30, corner_radius=10,
                                          fg_color='orange', text_color='black', text="Profile",
                                          command=self.profileSiswa)
        self.profileButton.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        self.matpelButton = ct.CTkButton(master=self.menu_siswaFrame, width=120, height=30, corner_radius=10,
                                         fg_color='orange', text_color='black', text="Mata Pelajaran",
                                         command=self.mataPelajaranSiswa)
        self.matpelButton.place(relx=0.5, rely=0.275, anchor=tkinter.CENTER)
        self.nilaiButton = ct.CTkButton(master=self.menu_siswaFrame, width=120, height=30, corner_radius=10,
                                         fg_color='orange', text_color='black', text="Nilai",
                                         command=self.nilaiSiswa)
        self.nilaiButton.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
        self.absensiButton = ct.CTkButton(master=self.menu_siswaFrame, width=120, height=30, corner_radius=10,
                                         fg_color='orange', text_color='black', text="Absensi",
                                         command=self.absenSiswa)
        self.absensiButton.place(relx=0.5, rely=0.425, anchor=tkinter.CENTER)
        self.kelasButton = ct.CTkButton(master=self.menu_siswaFrame, width=120, height=30, corner_radius=10,
                                         fg_color='orange', text_color='black', text="Kelas",
                                         command=self.kelasSiswa)
        self.kelasButton.place(relx=0.5, rely=0.500, anchor=tkinter.CENTER)
        self.logoutButton = ct.CTkButton(master=self.menu_siswaFrame, width=120, height=30, corner_radius=10,
                                          fg_color='orange', text_color='black', text="Log Out",
                                          command=self.logout)
        self.logoutButton.place(relx=0.5, rely=0.925, anchor=tkinter.CENTER)
    def profileSiswa(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuSiswa()
        self.profileFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.profileFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        font1 = ct.CTkFont(family='montserrat', size=24)
        self.profileLabel = ct.CTkLabel(master=self.profileFrame, text='Profile', font=font1)
        self.profileLabel.place(relx=0.02, rely=0.02, anchor=tkinter.NW)
        self.valueProfile('nama',myschool_login.userzz,0.02,0.18,0.02,0.12)
        self.valueProfile('kelas', myschool_login.userzz, 0.02, 0.32, 0.02, 0.26)
        self.valueProfile('nis', myschool_login.userzz, 0.02, 0.46, 0.02, 0.40)
        self.valueProfile('gender', myschool_login.userzz, 0.02, 0.60, 0.02, 0.54)

    def valueProfile(self,column,username,xframe,yframe,xlabel,ylabel):
        sql1 = 'select `data_siswa`.{} from `data_siswa` inner join `user_account` on `data_siswa`.nis=`user_account`.nis where `user_account`.username = (%s);'.format(
            column)
        myschool_login.curr.execute(sql1, (username))
        result = myschool_login.curr.fetchone()
        for x in result:
            self.hasil = x

        self.frameBio(self.hasil,xframe,yframe)
        self.labelBio(column.upper(),xlabel,ylabel)

    def frameBio(self,text,xframe,yframe):
        self.bioFrame = ct.CTkFrame(master=self.profileFrame, width=385, height=40,fg_color='#f2f2f2', corner_radius=15 )
        self.bioFrame.place(relx=xframe, rely=yframe, anchor=tkinter.NW)
        self.bioLabel = ct.CTkLabel(master=self.bioFrame, text_color='black', text=text)
        self.bioLabel.place(relx=0.05,rely=0.5, anchor=tkinter.W)

    def labelBio(self,text,relx,rely):
        font2 = ct.CTkFont(family='montserrat', size=18)
        self.LabelatasBio = ct.CTkLabel(master=self.profileFrame, text=text,font=font2, text_color='black')
        self.LabelatasBio.place(relx=relx,rely=rely,anchor=tkinter.NW)


    def mataPelajaranSiswa(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuSiswa()
        self.matpelFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.matpelFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        myschool_mapel.setup_uimatapelajaran(self.matpelFrame)


    def nilaiSiswa(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuSiswa()
        self.nilaiFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.nilaiFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        myschool_nilai.setup_ui(self.nilaiFrame)

    def kelasSiswa(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuSiswa()
        self.kelasFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.kelasFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        myschool_kelas.setup_uiKelas(self.kelasFrame)

    def absenSiswa(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuSiswa()
        self.absenFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.absenFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        myschool_absen.ui(self.absenFrame)

    def logout(self):
        for x in self.winfo_children():
            x.destroy()
        tkinter.messagebox.showinfo('Logged Out', 'Berhasil Log Out')
        self.background_GUI()


if __name__ == "__main__":
    root = MySchoolApp()
    root.mainloop()





