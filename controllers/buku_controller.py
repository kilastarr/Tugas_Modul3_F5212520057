from tkinter import messagebox

class BukuController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # Mengikat (binding) tombol GUI dengan fungsi controller
        self.view.btn_simpan.configure(command=self.simpan_buku)
        self.view.btn_update.configure(command=self.update_buku)
        self.view.btn_delete.configure(command=self.hapus_buku)

        # Mengikat event klik baris tabel untuk menampilkan data ke form input
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris_tabel)

        # Tampilkan data awal saat aplikasi dijalankan
        self.tampilkan_semua_buku()

    def tampilkan_semua_buku(self):
        # Bersihkan tabel sebelum memuat data baru
        for row in self.view.tabel.get_children():
            self.view.tabel.delete(row)

        buku_list = self.model.get_all_buku()
        for buku in buku_list:
            # Karena get_all_buku() dictionary=True, akses dengan kunci kolom database
            self.view.tabel.insert("", "end", values=(
                buku['id_buku'], 
                buku['judul'], 
                buku['penulis'], 
                buku['tahun_terbit']
            ))

    def simpan_buku(self):
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if judul and penulis and tahun:
            try:
                # Memanggil create_buku sesuai nama fungsi di BukuModel
                self.model.create_buku(judul, penulis, tahun)
                self.tampilkan_semua_buku()
                self.kosongkan_form()
                messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menyimpan data: {e}")
        else:
            messagebox.showwarning("Peringatan", "Semua kolom wajib diisi!")

    def pilih_baris_tabel(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_data = self.view.tabel.item(selected_item[0])["values"]
            
            # Masukkan data dari tabel ke form input
            self.view.entry_judul.delete(0, "end")
            self.view.entry_judul.insert(0, item_data[1])

            self.view.entry_penulis.delete(0, "end")
            self.view.entry_penulis.insert(0, item_data[2])

            self.view.entry_tahun.delete(0, "end")
            self.view.entry_tahun.insert(0, item_data[3])

    def update_buku(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris data buku pada tabel yang ingin diperbarui!")
            return

        id_buku = self.view.tabel.item(selected_item[0])["values"][0]
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if judul and penulis and tahun:
            try:
                # Memanggil update_buku di BukuModel
                self.model.update_buku(id_buku, judul, penulis, tahun)
                self.tampilkan_semua_buku()
                self.kosongkan_form()
                messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memperbarui data: {e}")
        else:
            messagebox.showwarning("Peringatan", "Semua kolom wajib diisi!")

    def hapus_buku(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris data buku pada tabel yang ingin dihapus!")
            return

        id_buku = self.view.tabel.item(selected_item[0])["values"][0]

        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data buku ini?"):
            try:
                # Memanggil delete_buku sesuai nama fungsi di BukuModel
                self.model.delete_buku(id_buku)
                self.tampilkan_semua_buku()
                self.kosongkan_form()
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menghapus data: {e}")

    def kosongkan_form(self):
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")