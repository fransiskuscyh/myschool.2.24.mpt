import tkinter
from tkinter import messagebox
from abc import ABC, abstractmethod
import customtkinter
import customtkinter as ct
from PIL import ImageTk, Image
from mataPel import *
from nilai import *
from kelasFix import *
from AbsenFix import *
from pengurus import *
from dbConnect import *
from testSiswa import *


class abstractLogin(ABC):
    @abstractmethod
    def loginin(self,username,password):
        pass

    @abstractmethod
    def resetPassword(self,username,password,passlama):
        pass

    @abstractmethod
    def pengurusLogin(self,username,password):
        pass
class Login(abstractLogin):
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
        try:
            entered_username = username
            entered_password = password
            sql_user = "SELECT `user_pengurus` FROM `pengurus_account` WHERE `user_pengurus` = (%s)"
            self.curr.execute(sql_user, entered_username)
            user_pop = self.curr.fetchone()
            for x in user_pop:
                self.userzz = x

            sql_password = "SELECT `pass_pengurus` FROM `pengurus_account` WHERE `user_pengurus` = (%s)"
            self.curr.execute(sql_password, entered_username)
            password_pop = self.curr.fetchone()
            for x in password_pop:
                passwordzz = x

            if entered_username == self.userzz and entered_password == passwordzz:
                tkinter.messagebox.showinfo("Login", "Login successful!")
                username_login = self.userzz
                root.menu_pengurus()


            elif entered_username != self.userzz and entered_password != passwordzz:
                tkinter.messagebox.showerror("Login Error", "Invalid username or password")
        except TypeError:
            tkinter.messagebox.showerror("Login Error", "Invalid username or password")

dbApp = mainDB()
conn_dbApp, curr_dbApp = dbApp.connect()
myschool_login = Login(curr_dbApp,conn_dbApp)


customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

class MySchoolApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.title("MySchool")
        self.geometry('1000x600')
       # self.resizable(0,0)


        self.background_GUI()

    def background_GUI(self):
        for i in self.winfo_children():
            i.destroy()
        self.frame1 = ct.CTkFrame(master=self, width=1000,height=600, fg_color='grey')
        self.frame1.place(rely=0.5,relx=0.5,anchor=tkinter.CENTER)
        self.backframez = ct.CTkFrame(master=self.frame1, width=400, height=600, fg_color='orange', corner_radius=0)
        self.backframez.place(rely=0,relx=1,anchor=tkinter.NE)

        img = Image.open('siswa_art.png')
        new_size = (605, 715)
        img_resized = img.resize(new_size)
        img_tk = ImageTk.PhotoImage(img_resized)
        self.background_label = ct.CTkLabel(master=self.frame1, image=img_tk, text="")
        self.background_label.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)
        self.loginFrame()

    def loginFrame(self):
        self.loginzframe = ct.CTkFrame(master=self.backframez, width=300, height=500, fg_color='blue', corner_radius=15)
        self.loginzframe.place(rely=0.5,relx=0.5, anchor=tkinter.CENTER)
        
        # imagess = Image.open('Black & White Minimalist Business Logo.png')
        imagess = Image.open('Iconmyschool.png')
        new_sizess = (300,300)
        image_resized = imagess.resize(new_sizess)
        image_tk = ImageTk.PhotoImage(image_resized)
        self.logoApp = ct.CTkLabel(master=self.loginzframe, image=image_tk, text="")
        self.logoApp.place(relx=0.5,rely=0.14,anchor=tkinter.CENTER)

        self.username_entry = ct.CTkEntry(master=self.loginzframe, width=200, height=30, fg_color='white', text_color='black')
        self.username_entry.place(relx=0.5, rely=0.31, anchor = tkinter.CENTER)

        self.username_label =ct.CTkLabel(master=self.loginzframe, text_color='white', text='Username')
        self.username_label.place(relx=0.17, rely=0.25, anchor = tkinter.W)

        self.password_label = ct.CTkLabel(master=self.loginzframe, text_color='white', text='Password')
        self.password_label.place(relx=0.17, rely=0.375, anchor=tkinter.W)

        self.password_entry = ct.CTkEntry(master=self.loginzframe, width=200, height=30, fg_color='white',
                                          text_color='black', show='*')
        self.password_entry.place(relx=0.5, rely=0.435, anchor=tkinter.CENTER)

        self.login_button = ct.CTkButton(master=self.loginzframe, width=75, height=30, fg_color='brown', text='Login Siswa', command=lambda : myschool_login.loginin(self.username_entry.get(),self.password_entry.get()))
        self.login_button.place(relx=0.5, rely=0.55, anchor = tkinter.CENTER)
        self.loginPengurus_button = ct.CTkButton(master=self.loginzframe, width=75, height=30, fg_color='brown', text='Login Pengurus', command=lambda : myschool_login.pengurusLogin(self.username_entry.get(),self.password_entry.get()))
        self.loginPengurus_button.place(relx=0.5, rely=0.64, anchor = tkinter.CENTER)


    def menu_pengurus(self):
        self.frame1.destroy()
        self.listMenuPengurus()
        self.profile_pengurus()
    def listMenuPengurus(self):
        self.menu_pengurusFrame = ct.CTkFrame(master=self, width=170, height=1080, corner_radius=0, fg_color='blue')
        self.menu_pengurusFrame.pack(padx=0, pady=0, anchor=tkinter.W)
        self.profileButton = ct.CTkButton(master=self.menu_pengurusFrame, width=120, height=30, corner_radius=10,
                                          fg_color='orange', text_color='black', text="Profile",
                                          command=self.profile_pengurus)
        self.profileButton.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        self.matpelButton = ct.CTkButton(master=self.menu_pengurusFrame, width=120, height=30, corner_radius=10,
                                         fg_color='orange', text_color='black', text="Mata Pelajaran",
                                         command=self.mataPelajaranPengurus)
        self.matpelButton.place(relx=0.5, rely=0.275, anchor=tkinter.CENTER)
        self.nilaiButton = ct.CTkButton(master=self.menu_pengurusFrame, width=120, height=30, corner_radius=10,
                                        fg_color='orange', text_color='black', text="Nilai",
                                        command=self.nilaiPengurus)
        self.nilaiButton.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
        self.absensiButton = ct.CTkButton(master=self.menu_pengurusFrame, width=120, height=30, corner_radius=10,
                                          fg_color='orange', text_color='black', text="Absensi",
                                          command=self.absensiPengurus)
        self.absensiButton.place(relx=0.5, rely=0.425, anchor=tkinter.CENTER)
        self.kelasButton = ct.CTkButton(master=self.menu_pengurusFrame, width=120, height=30, corner_radius=10,
                                        fg_color='orange', text_color='black', text="Kelas",
                                        command=self.kelasPengurus)
        self.kelasButton.place(relx=0.5, rely=0.500, anchor=tkinter.CENTER)
        self.logoutButton = ct.CTkButton(master=self.menu_pengurusFrame, width=120, height=30, corner_radius=10,
                                         fg_color='orange', text_color='black', text="Log Out",
                                         command=self.logout)
        self.logoutButton.place(relx=0.5, rely=0.925, anchor=tkinter.CENTER)

    def profile_pengurus(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuPengurus()
        self.profileFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.profileFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        font1 = ct.CTkFont(family='montserrat', size=24)
        self.profileLabel = ct.CTkLabel(master=self.profileFrame, text='Profile', font=font1)
        self.profileLabel.place(relx=0.02, rely=0.02, anchor=tkinter.NW)
        myschool_pengurus = Pengurus(conn_dbApp,curr_dbApp,self)
        myschool_pengurus.valueProfilePengurus('Nama_Pengurus',myschool_login.userzz,0.02,0.18,0.02,0.12,'Nama',self.profileFrame)
        myschool_pengurus.valueProfilePengurus('Jabatan_Pengurus', myschool_login.userzz, 0.02, 0.32, 0.02, 0.26, "Posisi",self.profileFrame)
        myschool_pengurus.valueProfilePengurus('NUPTK_Pengurus', myschool_login.userzz, 0.02, 0.46, 0.02, 0.40, "NUPTK",self.profileFrame)
        myschool_pengurus.valueProfilePengurus('MataPelajaran_Pengurus', myschool_login.userzz, 0.02, 0.60, 0.02, 0.54, "Mata Pelajaran",self.profileFrame)
        myschool_pengurus.valueProfilePengurus('TTL_Pengurus', myschool_login.userzz, 0.02, 0.74, 0.02, 0.68, "Tempat & Tanggal Lahir",self.profileFrame)

    def kelasPengurus(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuPengurus()
        self.kelasFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.kelasFrame.place(relx=0.17, rely=0.5, anchor=tkinter.W)
        myschool_kelas = Kelas(curr_dbApp, conn_dbApp, self)
        myschool_kelas.setup_uiKelas(self.kelasFrame)

    def nilaiPengurus(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuPengurus()
        self.nilaiFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.nilaiFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        myschool_nilai = Nilai(curr_dbApp, conn_dbApp,self)
        myschool_nilai.setup_ui(self.nilaiFrame)

    def absensiPengurus(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuPengurus()
        self.absensiFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.absensiFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        myschool_absen = absen(curr_dbApp,conn_dbApp,self)
        myschool_absen.ui(self.absensiFrame)

    def menu_siswa(self):
        self.frame1.destroy()
        self.listMenuSiswa()
        self.profileSiswa()

    def listMenuSiswa(self):
        self.menu_siswaFrame = ct.CTkFrame(master=self, width=170, height=1080, corner_radius=0, fg_color='blue')
        self.menu_siswaFrame.pack(padx=0, pady=0, anchor=tkinter.W)
        self.profileButton = ct.CTkButton(master=self.menu_siswaFrame, width=120, height=30, corner_radius=10,
                                          fg_color='orange', text_color='black', text="Profile",
                                          command=self.profileSiswa)
        self.profileButton.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        self.matpelButton = ct.CTkButton(master=self.menu_siswaFrame, width=120, height=30, corner_radius=10,
                                         fg_color='orange', text_color='black', text="Mata Pelajaran",
                                         command=self.__mataPelajaranSiswa)
        self.matpelButton.place(relx=0.5, rely=0.275, anchor=tkinter.CENTER)
        self.nilaiButton = ct.CTkButton(master=self.menu_siswaFrame, width=120, height=30, corner_radius=10,
                                         fg_color='orange', text_color='black', text="Nilai",
                                         command=self.nilaiSiswa)
        self.nilaiButton.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
        self.absensiButton = ct.CTkButton(master=self.menu_siswaFrame, width=120, height=30, corner_radius=10,
                                         fg_color='orange', text_color='black', text="Absensi",
                                         command=self.absensiSiswa)
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
        myschool_siswa = Siswa(curr_dbApp,conn_dbApp,self)
        myschool_siswa.valueProfile('nama',myschool_login.userzz,0.02,0.18,0.02,0.12,self.profileFrame)
        myschool_siswa.valueProfile('kelas', myschool_login.userzz, 0.02, 0.32, 0.02, 0.26,self.profileFrame)
        myschool_siswa.valueProfile('nis', myschool_login.userzz, 0.02, 0.46, 0.02, 0.40,self.profileFrame)
        myschool_siswa.valueProfile('gender', myschool_login.userzz, 0.02, 0.60, 0.02, 0.54,self.profileFrame)
        myschool_siswa.valueProfile('agama', myschool_login.userzz, 0.02, 0.74, 0.02, 0.68,self.profileFrame)

    def mataPelajaranPengurus(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuPengurus()
        self.matpelFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.matpelFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        myschool_matpel = mataPelajaran(curr_dbApp,conn_dbApp,self)
        myschool_matpel.setup_uimatapelajaranPengurus(self.matpelFrame)


    def nilaiSiswa(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuSiswa()
        self.nilaiFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.nilaiFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        myschool_nilai = Nilai(curr_dbApp, conn_dbApp,self)
        myschool_nilai.setup_ui(self.nilaiFrame)

    def logout(self):
        for x in self.winfo_children():
            x.destroy()
        tkinter.messagebox.showinfo('Logged Out', 'Berhasil Log Out')
        self.background_GUI()

    def absensiSiswa(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuSiswa()
        self.absensiFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.absensiFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        myschool_absen = absen(curr_dbApp,conn_dbApp,self)
        myschool_absen.ui(self.absensiFrame)

    def kelasPengurus(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuPengurus()
        self.kelasFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.kelasFrame.place(relx=0.17, rely=0.5, anchor=tkinter.W)
        myschool_kelas = Kelas(curr_dbApp,conn_dbApp,self)
        myschool_kelas.setup_uiKelas(self.kelasFrame)

    def kelasSiswa(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuSiswa()
        self.kelasFrame = ct.CTkFrame(master=self, width=830, height=760, fg_color='grey93', corner_radius=0)
        self.kelasFrame.place(relx=0.17, rely=0.5, anchor=tkinter.W)
        self.myschool_kelas = Kelas(curr_dbApp, conn_dbApp, self)

        self.valueProfileKelas('nama_kelas',myschool_login.userzz,0.02,0.18,0.02,0.12,'Kelas')
        self.valueProfileKelas('wali_kelas',myschool_login.userzz,0.51,0.18,0.51,0.12,'Wali Kelas')
        self.jadwalLabel = ct.CTkLabel(master=self.kelasFrame,text_color='black', text='Jadwal Pelajaran', font=('montserrat',17))
        self.jadwalLabel.place(relx=0.02,rely=0.27,anchor=tkinter.NW)
        self.myschool_kelas.setupuijadwalSiswa()

    def valueProfileKelas(self,column,username,xframe,yframe,xlabel,ylabel,label):
        sql1 = 'select `kelas`.{} from `kelas` inner join `data_siswa` on `kelas`.nama_kelas=`data_siswa`.kelas inner join `user_account` on `data_siswa`.nis = `user_account`.nis where `user_account`.username = (%s);'.format(
            column)
        myschool_login.curr.execute(sql1, (username))
        result = myschool_login.curr.fetchone()
        for x in result:
            self.hasil = x

        self.frameKelas(self.hasil, xframe, yframe)
        self.labelBioKelas(label, xlabel, ylabel)

    def frameKelas(self,text,xframe,yframe):
        self.kelasBioFrame = ct.CTkFrame(master=self.kelasFrame, width=385, height=40,fg_color='#f2f2f2', corner_radius=15 )
        self.kelasBioFrame.place(relx=xframe, rely=yframe, anchor=tkinter.NW)
        self.kelasLabel = ct.CTkLabel(master=self.kelasBioFrame, text_color='black', text=text)
        self.kelasLabel.place(relx=0.05,rely=0.5, anchor=tkinter.W)

    def labelBioKelas(self,text,relx,rely):
        font2 = ct.CTkFont(family='montserrat', size=18)
        self.LabelatasBio = ct.CTkLabel(master=self.kelasFrame, text=text,font=font2, text_color='black')
        self.LabelatasBio.place(relx=relx,rely=rely,anchor=tkinter.NW)

    def __mataPelajaranSiswa(self):
        for x in self.winfo_children():
            x.destroy()
        self.listMenuSiswa()
        self.matpelFrame = ct.CTkFrame(master=self, width=830, height=600, fg_color='white', corner_radius=0)
        self.matpelFrame.place(relx=0.17,rely=0.5,anchor=tkinter.W)
        myschool_matpel = mataPelajaran(curr_dbApp,conn_dbApp,self)
        myschool_matpel.setup_uimatapelajaranSiswa(self.matpelFrame)

if __name__ == "__main__":
    root = MySchoolApp()
    root.mainloop()


