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

        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green", command=self.simpan_data)
        self.btn_simpan.pack(pady=10, padx=15, fill="x")

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

        self.id_counter = 1

    def simpan_data(self):
        nama = self.entry_nama.get()
        alamat = self.txt_alamat.get("1.0", "end-1c")

        if nama and alamat.strip():
            item_id = self.tabel.insert("", "end", values=(self.id_counter, nama, alamat))
            self.id_counter += 1

            # Otomatis sorot biru tebal baris yang baru disimpan
            self.tabel.selection_set(item_id)
            self.tabel.focus(item_id)

            # Kosongkan form setelah simpan
            self.entry_nama.delete(0, "end")
            self.txt_alamat.delete("1.0", "end")

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()