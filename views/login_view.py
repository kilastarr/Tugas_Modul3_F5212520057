import customtkinter as ctk

class LoginView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("Login - Sistem Perpustakaan")
        self.geometry("400x400")
        self.resizable(False, False)

        # Container Utama
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Judul
        self.lbl_title = ctk.CTkLabel(
            self.main_frame, 
            text="LOGIN SISTEM", 
            font=("Arial", 18, "bold")
        )
        self.lbl_title.pack(pady=(30, 20))

        # Input Username
        self.entry_username = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Username", 
            width=250, 
            height=40
        )
        self.entry_username.pack(pady=10)

        # Input Password
        self.entry_password = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Password", 
            show="*", 
            width=250, 
            height=40
        )
        self.entry_password.pack(pady=10)

        # Label Error
        self.lbl_error = ctk.CTkLabel(
            self.main_frame, 
            text="", 
            text_color="red", 
            font=("Arial", 11)
        )
        self.lbl_error.pack(pady=(5, 0))

        # Tombol Masuk
        self.btn_login = ctk.CTkButton(
            self.main_frame, 
            text="Masuk", 
            fg_color="blue", 
            hover_color="darkblue",
            width=250, 
            height=40,
            command=self.on_login_click
        )
        self.btn_login.pack(pady=(15, 20))

    def on_login_click(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.controller.login(username, password)

    def show_error(self, message):
        self.lbl_error.configure(text=message)