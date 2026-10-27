import customtkinter as ctk
from tkinter import ttk

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Perpustakaan - Manajemen Data Anggota")
        self.geometry("800x480")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Config Style Warna Biru saat Baris Dipilih
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=28, font=("Arial", 10))
        style.map("Treeview", 
                  background=[("selected", "#1f538d")], 
                  foreground=[("selected", "white")])

        # FRAME KIRI: FORM DATA ANGGOTA
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota", font=("Arial", 16, "bold")).pack(pady=(15, 10))

        ctk.CTkLabel(self.frame_kiri, text="Nama Anggota:", anchor="w").pack(fill="x", padx=15, pady=(5, 2))
        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Lengkap")
        self.entry_nama.pack(pady=(0, 5), padx=15, fill="x")

        ctk.CTkLabel(self.frame_kiri, text="Alamat:", anchor="w").pack(fill="x", padx=15, pady=(5, 2))
        self.txt_alamat = ctk.CTkTextbox(self.frame_kiri, height=100)
        self.txt_alamat.pack(pady=(0, 10), padx=15, fill="x")

        # Tombol CRUD
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=5, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data", fg_color="#1f538d")
        self.btn_update.pack(pady=5, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data", fg_color="red")
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # FRAME KANAN: TABEL DAFTAR ANGGOTA
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota Perpustakaan", font=("Arial", 16, "bold")).pack(pady=15)

        kolom = ("id", "nama", "alamat")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)

        self.tabel.heading("id", text="ID Anggota")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        self.tabel.column("id", width=80, anchor="center")
        self.tabel.column("nama", width=140)
        self.tabel.column("alamat", width=200)

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)