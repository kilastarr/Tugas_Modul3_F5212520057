from views.login_view import LoginView
from views.buku_view import BukuView
from controllers.buku_controller import BukuController
from models.buku_model import BukuModel
from models.user_model import UserModel
from tkinter import messagebox

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.login_view = None
        self.buku_view = None

    def show_login(self):
        self.login_view = LoginView(self)
        self.login_view.mainloop()

    def login(self, username, password):
        user = self.model.autentikasi(username, password)
        if user:
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {user['username']}! (Role: {user['role']})")
            
            if self.login_view:
                self.login_view.destroy()

            # 1. Inisialisasi BukuView dengan data pengguna yang login
            self.buku_view = BukuView(controller=self, current_user=user)
            
            # 2. Inisialisasi BukuModel
            buku_model = BukuModel()

            # 3. Hubungkan BukuController dengan BukuView dan BukuModel
            # Ini akan otomatis menjalankan self.tampilkan_semua_buku() & binding tombol dari BukuController
            self.buku_controller = BukuController(view=self.buku_view, model=buku_model)

            self.buku_view.mainloop()
        else:
            if self.login_view:
                self.login_view.show_error("Username atau Password salah!")