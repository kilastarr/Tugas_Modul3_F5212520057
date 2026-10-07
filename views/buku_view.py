import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Perpustakaan - Manajemen Data Buku")
        self.geometry("800x480")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Config Style Warna Biru saat Baris Dipilih
        style = ttk.Style()
        style.theme_use("clam")  # Menjamin warna highlight konsisten
        style.configure("Treeview", rowheight=28, font=("Arial", 10))
        style.map("Treeview", 
                  background=[("selected", "#1f538d")],  # Warna biru tebal
                  foreground=[("selected", "white")])    # Teks putih

        # FRAME KIRI: FORM INPUT BUKU
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

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

        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green", command=self.simpan_data)
        self.btn_simpan.pack(pady=5, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="#1f538d")
        self.btn_update.pack(pady=5, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="#c0392b")
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # FRAME KANAN: TABEL DAFTAR BUKU
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

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

        self.id_counter = 1

    def simpan_data(self):
        judul = self.entry_judul.get()
        penulis = self.entry_penulis.get()
        tahun = self.entry_tahun.get()

        if judul and penulis and tahun:
            item_id = self.tabel.insert("", "end", values=(self.id_counter, judul, penulis, tahun))
            self.id_counter += 1
            
            # Otomatis sorot biru tebal baris yang baru disimpan
            self.tabel.selection_set(item_id)
            self.tabel.focus(item_id)

            # Kosongkan form setelah simpan
            self.entry_judul.delete(0, "end")
            self.entry_penulis.delete(0, "end")
            self.entry_tahun.delete(0, "end")

if __name__ == "__main__":
    app = BukuView()
    app.mainloop()