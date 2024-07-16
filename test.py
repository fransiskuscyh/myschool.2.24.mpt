import tkinter as tk

def login():
    # Fungsi login akan dipanggil saat tombol login ditekan atau Enter ditekan

    # Gantilah dengan logika login sesuai kebutuhan Anda
    print("Login successful!")

def on_enter_pressed(event):
    # Fungsi ini akan dipanggil saat tombol Enter ditekan
    login()

# Membuat instance Tkinter
root = tk.Tk()
root.title("Login Form")

# Membuat entry untuk username
username_entry = tk.Entry(root)
username_entry.pack(pady=10)

# Membuat entry untuk password
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

# Membuat tombol login dan mengaitkannya dengan fungsi login
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Mengaitkan fungsi on_enter_pressed dengan event tombol Enter
root.bind('<Return>', on_enter_pressed)

# Menjalankan loop utama Tkinter
root.mainloop()
