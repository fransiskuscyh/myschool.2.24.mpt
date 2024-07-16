import tkinter
from tkinter import messagebox
import customtkinter as ct
from PIL import ImageTk, Image
from main import *
dbApp = mainDB()
conn_dbApp, curr_dbApp = dbApp.connect()

class LoginPageApp(ct.CTkFrame):
    def __init__(self,master, controller):
        ct.CTkFrame.__init__(self,master)
        self.controller = controller

        self.master = master
        self.curry = curr_dbApp
        self.conn = conn_dbApp
        #self.frames = master
        self.setup_ui()

    def setup_ui(self):


        self.create_background()
        self.create_self_login_frame()

    def create_background(self):
        self.backframez = ct.CTkFrame(master=self, width=2600, height=1920, fg_color='orange')

        img = Image.open('siswa_art.png')
        new_size = (1100, 1100)
        img_resized = img.resize(new_size)
        img_tk = ImageTk.PhotoImage(img_resized)
        self.background_label = ct.CTkLabel(master=self, image=img_tk, text="")
        self.background_label.place(relx=0.5, rely=0.4, anchor=tkinter.E)

    def create_self_login_frame(self):
        font1 = ct.CTkFont(family='montserrat', size=17)

        self.backframe = ct.CTkFrame(master=self, width=650, height=1080, fg_color='orange')
        self.backframe.place(relx=0.63, rely=0.5, anchor=tkinter.W)

        self.login_frame = ct.CTkFrame(master=self,width=400, height=720, corner_radius=35, fg_color='blue',
                               bg_color=self.backframe._fg_color)
        self.login_frame.place(relx=0.7, rely=0.5, anchor=tkinter.W)

        self.username_entry = ct.CTkEntry(master=self.login_frame, width=280, height=40, corner_radius=35, fg_color='white', text_color='black')
        self.username_entry.place(relx=0.5, rely=0.39, anchor=tkinter.CENTER)

        self.username_label = ct.CTkLabel(master=self.login_frame, text='Username', font=font1, text_color='white')
        self.username_label.place(relx=0.273, rely=0.338, anchor=tkinter.CENTER)

        self.password_label = ct.CTkLabel(master=self.login_frame, text='Password', font=font1, text_color='white')
        self.password_label.place(relx=0.273, rely=0.458, anchor=tkinter.CENTER)

        self.password_entry = ct.CTkEntry(master=self.login_frame, width=280, height=40, corner_radius=35, fg_color='white', text_color='black', show="*")
        self.password_entry.place(relx=0.5, rely=0.51, anchor=tkinter.CENTER)

        self.login_logo = Image.open('Desain tanpa judul.png')
        new_size = (450, 270)
        self.login_logo_resized = self.login_logo.resize(new_size)
        self.login_logo_tk = ImageTk.PhotoImage(self.login_logo_resized)
        self.login_logo_label = ct.CTkLabel(master=self.login_frame, image=self.login_logo_tk, text='')
        self.login_logo_label.place(relx=0.5, rely=0.18, anchor=tkinter.CENTER)

        self.login_button = ct.CTkButton(master=self.login_frame, width=150, height=30, corner_radius=15, fg_color='brown', text='Login', font=font1, command=lambda: self.login(self.username_entry.get(),self.password_entry.get()))
        self.login_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def hello(self):
        self.helloword = ct.CTkLabel(master=self.login_frame, text="Hellow World")
        self.helloword.pack()

    def login(self, user, password):

        entered_username = user
        entered_password = password
        sql_user = "SELECT `username` FROM `user_account` WHERE `username` = (%s)"
        self.curry.execute(sql_user, entered_username)
        user_pop = self.curry.fetchone()
        for x in user_pop:
            userzz = x

        sql_password = "SELECT `user_password` FROM `user_account` WHERE `username` = (%s)"
        self.curry.execute(sql_password, entered_username)
        password_pop = self.curry.fetchone()
        for x in password_pop:
            passwordzz = x

        # Check if the username and password are correct (you would replace this with your own authentication logic)

        if entered_username == userzz and entered_password == passwordzz:
            tkinter.messagebox.showinfo("Login", "Login successful!")
            self.controller.show_frame(dashboardPage)
        elif entered_username != userzz and entered_password != passwordzz:
            tkinter.messagebox.showerror("Login Error", "Invalid username or password")

class dashboardPage(ct.CTkFrame):
    def __init__(self,master, controller):
        ct.CTkFrame.__init__(self, master)
        self.controller = controller

        self.master = master
        self.curr = curr_dbApp
        self.conn = conn_dbApp
        self.font = ct.CTkFont(family='montserrat', size=17)
        self.dash_frames = {}
        self.frames_dash()

        self.setup_ui()

    def setup_ui(self):
        self.dashGui()

    def dashGui(self):
        self.side_panel_width = 200
        self.side_panel_state = False
        self.headframe = ct.CTkFrame(master=self, height=70, width=1920, fg_color='blue', corner_radius=0)
        self.headframe.pack(side="top", fill="x",expand=True, anchor=tkinter.N)

        self.sidePanel = ct.CTkFrame(master=self, height= 1080, width=self.side_panel_width, fg_color='blue')
        self.sidePanel.place(x=-self.side_panel_width, y=0, relheight=1)

        self.toggle_menu = ToggleButton(self)
        self.toggle_menu.set_button_callback(self.__button_toggle_handler)

        self.panelToggleButton = ct.CTkButton(master=self.headframe, text='Menu', command=self.__button_toggle_handler, width=50,
                                              fg_color='orange', border_color='black', border_width=2,
                                              text_color='black')
        self.panelToggleButton.pack(padx=10, pady=10, anchor=tkinter.W)

        self.change_dashFrame(Profile)

        self.profile_button = ct.CTkButton(master=self.toggle_menu, text="Profile",
                                           command=lambda: self.change_dashPageProfile())
        self.toggle_menu.create_window(130, 180, window=self.profile_button, anchor=tkinter.CENTER)
        self.nilai_button = ct.CTkButton(master=self.toggle_menu, text="Nilai",
                                         command=lambda: self.change_dashPageNilai())
        self.toggle_menu.create_window(130, 240, window=self.nilai_button, anchor=tkinter.CENTER)
        self.kelas_button = ct.CTkButton(master=self.toggle_menu, text="Kelas",
                                         command=lambda: self.change_dashPageKelas())
        self.toggle_menu.create_window(130, 300, window=self.kelas_button, anchor=tkinter.CENTER)

    def __button_toggle_handler(self):
        if self.side_panel_state:
            self.toggle_menu.stop_ui()
            self.side_panel_state = False
        else:
            self.toggle_menu.setup_ui()
            self.side_panel_state = True

    def __toggle_callback(self):
        print("berhasil")
        pass

    def frames_dash(self):
        profile_frame = Profile(self,self.controller)
        nilai_frame = Nilai(self,self.controller)
        kelas_frame = Kelas(self,self.controller)
        self.dash_frames[Profile] = profile_frame
        self.dash_frames[Nilai] = nilai_frame
        self.dash_frames[Kelas] = kelas_frame

    def change_dashFrame(self,frame_name):
        for frame in self.dash_frames.values():
            frame.place_forget()

        if frame_name is not None:
            new_frame = self.dash_frames[frame_name]
            new_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def change_dashPageNilai(self):
        self.change_dashFrame(Nilai)

    def change_dashPageProfile(self):
        self.change_dashFrame(Profile)
    
    def change_dashPageKelas(self):
        self.change_dashFrame(Kelas)

class ToggleButton(ct.CTkCanvas):
    def __init__(self,parent):
        super().__init__(parent, width=280, height=2000, bg='blue', bd=0)
        self.button_callback = None
        self.menu_logo = Image.open('Desain tanpa judul.png')
        new_size = (150, 75)
        self.menu_logo_resized = self.menu_logo.resize(new_size)
        self.menu_logo_tk = ImageTk.PhotoImage(self.menu_logo_resized)
        self.create_image(130,55, image=self.menu_logo_tk, anchor=tkinter.CENTER)
        self.menu_button = ct.CTkButton(self, text="MySchool Menu", command=lambda : self.button_callback())
        self.create_window(130,120, window=self.menu_button, anchor=tkinter.CENTER)

    def set_button_callback(self, callback):
        self.button_callback = callback

    def setup_ui(self):
        self.place(x=0,y=0)

    def stop_ui(self):
        self.place_forget()

class Profile(ct.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.master = master
        self.curr = curr_dbApp
        self.conn = conn_dbApp
        self.font = ct.CTkFont(family='montserrat', size=17)
        self.setup_ui()

    def setup_ui(self):
        self.profileFrame = ct.CTkFrame(master=self, fg_color='#ccffff')
        self.profileFrame.pack(fill='both',expand=True,anchor=tkinter.CENTER)

        self.testLabel = ct.CTkLabel(master=self.profileFrame, text="test Profile Page", font=self.font, text_color='black')
        self.testLabel.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

class Nilai(ct.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.master = master
        self.curr = curr_dbApp
        self.conn = conn_dbApp
        self.font = ct.CTkFont(family='montserrat', size=17)
        self.setup_ui()

    def setup_ui(self):
        self.NilaiFrame = ct.CTkFrame(master=self, fg_color='#ccffff')
        self.NilaiFrame.pack(fill='both',expand=True,anchor=tkinter.CENTER)

        self.testLabel = ct.CTkLabel(master=self.NilaiFrame, text="Nilai Page", font=self.font, text_color='black')
        self.testLabel.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

class Kelas(ct.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.master = master
        self.curr = curr_dbApp
        self.conn = conn_dbApp
        self.font = ct.CTkFont(family='montserrat', size=17)
        self.setup_ui()

    def setup_ui(self):
        self.KelasFrame = ct.CTkFrame(master=self, fg_color='#ccffff')
        self.KelasFrame.pack(fill='both',expand=True,anchor=tkinter.CENTER)

        self.testLabel = ct.CTkLabel(master=self.KelasFrame, text="KELASSS Page", font=self.font, text_color='black')
        self.testLabel.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

class MainApp(ct.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ct.set_appearance_mode('light')
        ct.set_default_color_theme('dark-blue')
        #self.set_default_color_theme("dark-blue")
        self.title("My School App")
        self.geometry('1920x1080')
        # self.resizable(0,0)
        self.state('zoomed')
        self.curr = curr_dbApp
        self.conn = conn_dbApp

        self.frames = {}
        self.create_frames()

        self.show_frame(LoginPageApp)
    def create_frames(self):
        login_frame = LoginPageApp(self, self)
        dashboard_frame = dashboardPage(self, self)

        self.frames[LoginPageApp]= login_frame
        self.frames[dashboardPage]= dashboard_frame

    def show_frame(self, frame_class):
        for frame in self.frames.values():
            frame.place_forget()

        if frame_class is not None:
            new_frame = self.frames[frame_class]
            new_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
