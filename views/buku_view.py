import customtkinter as ctk
from tkinter import ttk, messagebox

class BukuView(ctk.CTk):
    def __init__(self, controller=None, current_user=None):
        super().__init__()
        self.controller = controller
        # Default user fallback untuk testing jika dipanggil tanpa login
        self.current_user = current_user or {"username": "Guest", "role": "anggota"}

        self.title("Sistem Perpustakaan - Manajemen Data Buku")
        self.geometry("850x520")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        # ------------------- HEADER FRAME (USER & LOGOUT) -------------------
        self.frame_header = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_header.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="ew")

        self.user_label = ctk.CTkLabel(
            self.frame_header, 
            text=f"User: {self.current_user.get('username')} ({self.current_user.get('role', '').upper()})",
            font=("Arial", 12, "bold")
        )
        self.user_label.pack(side="left", padx=10)

        # Tombol Logout
        self.btn_logout = ctk.CTkButton(
            self.frame_header, 
            text="Logout", 
            fg_color="#c0392b", 
            hover_color="#962d22",
            width=80,
            command=self.on_logout
        )
        self.btn_logout.pack(side="right", padx=10)

        # Style Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=28, font=("Arial", 10))
        style.map("Treeview", 
                  background=[("selected", "#1f538d")], 
                  foreground=[("selected", "white")])

        # ------------------- FRAME KIRI: FORM INPUT BUKU -------------------
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Input Buku", font=("Arial", 16, "bold")).pack(pady=(15, 10))

        ctk.CTkLabel(self.frame_kiri, text="Judul Buku:", anchor="w").pack(fill="x", padx=15, pady=(5, 2))
        self.entry_judul = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Judul Buku")
        self.entry_judul.pack(pady=(0, 5), padx=15, fill="x")

        ctk.CTkLabel(self.frame_kiri, text="Penulis:", anchor="w").pack(fill="x", padx=15, pady=(5, 2))
        self.entry_penulis = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Penulis")
        self.entry_penulis.pack(pady=(0, 5), padx=15, fill="x")

        ctk.CTkLabel(self.frame_kiri, text="Tahun Terbit:", anchor="w").pack(fill="x", padx=15, pady=(5, 2))
        self.entry_tahun = ctk.CTkEntry(self.frame_kiri, placeholder_text="Contoh: 2024")
        self.entry_tahun.pack(pady=(0, 10), padx=15, fill="x")

        # Tombol Simpan
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri, text="Simpan Data", fg_color="green"
        )
        self.btn_simpan.pack(pady=5, padx=15, fill="x")

        # Tombol Update
        self.btn_update = ctk.CTkButton(
            self.frame_kiri, text="Perbarui Data (Update)", fg_color="#1f538d"
        )
        self.btn_update.pack(pady=5, padx=15, fill="x")

        # Tombol Delete
        self.btn_delete = ctk.CTkButton(
            self.frame_kiri, text="Hapus Data (Delete)", fg_color="#c0392b"
        )
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # ------------------- FRAME KANAN: TABEL DAFTAR BUKU -------------------
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Koleksi Buku", font=("Arial", 16, "bold")).pack(pady=15)

        kolom = ("id", "judul", "penulis", "tahun")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)

        self.tabel.heading("id", text="ID Buku")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun Terbit")

        self.tabel.column("id", width=60, anchor="center")
        self.tabel.column("judul", width=160)
        self.tabel.column("penulis", width=120)
        self.tabel.column("tahun", width=90, anchor="center")

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)

        # Jalankan Aturan Otorisasi (RBAC)
        self.apply_authorization()

    def apply_authorization(self):
        """Menonaktifkan input dan tombol manipulasi jika role adalah 'anggota'."""
        if self.current_user.get("role") == "anggota":
            self.entry_judul.configure(state="disabled")
            self.entry_penulis.configure(state="disabled")
            self.entry_tahun.configure(state="disabled")
            self.btn_simpan.configure(state="disabled")
            self.btn_update.configure(state="disabled")
            self.btn_delete.configure(state="disabled")

    def on_logout(self):
        """Menutup BukuView dan mengembalikan pengguna ke jendela LoginView."""
        if messagebox.askyesno("Konfirmasi Logout", "Apakah Anda yakin ingin keluar?"):
            self.destroy()
            if self.controller and hasattr(self.controller, 'show_login'):
                self.controller.show_login()

if __name__ == "__main__":
    app = BukuView()
    app.mainloop()