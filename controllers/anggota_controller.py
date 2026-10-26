from tkinter import messagebox

class AnggotaController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # Mengikat (binding) tombol GUI dengan fungsi controller
        btn_simpan = getattr(self.view, 'btn_simpan', getattr(self.view, 'button_simpan', None))
        btn_update = getattr(self.view, 'btn_update', getattr(self.view, 'button_update', None))
        btn_delete = getattr(self.view, 'btn_delete', getattr(self.view, 'button_delete', None))

        if btn_simpan:
            btn_simpan.configure(command=self.simpan_anggota)
        if btn_update:
            btn_update.configure(command=self.update_anggota)
        if btn_delete:
            btn_delete.configure(command=self.hapus_anggota)

        # Mengikat event klik baris tabel untuk mengisi form
        if hasattr(self.view, 'tabel'):
            self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris_tabel)

        # Tampilkan data awal saat aplikasi dijalankan
        self.tampilkan_semua_anggota()

    def tampilkan_semua_anggota(self):
        # Bersihkan tabel sebelum memuat data baru
        for row in self.view.tabel.get_children():
            self.view.tabel.delete(row)

        anggota_list = self.model.get_all_anggota()
        for anggota in anggota_list:
            # Pengecekan aman untuk format dictionary maupun tuple
            if isinstance(anggota, dict):
                id_val = anggota.get('id_anggota') or anggota.get('id')
                nama_val = anggota.get('nama')
                alamat_val = anggota.get('alamat')
            else:
                id_val = anggota[0]
                nama_val = anggota[1]
                alamat_val = anggota[2]

            self.view.tabel.insert("", "end", values=(id_val, nama_val, alamat_val))

    def simpan_anggota(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.txt_alamat.get("1.0", "end-1c") if hasattr(self.view, 'txt_alamat') else self.view.entry_alamat.get()

        if nama and alamat.strip():
            try:
                if hasattr(self.model, 'create_anggota'):
                    self.model.create_anggota(nama, alamat)
                else:
                    self.model.tambah_anggota(nama, alamat)

                self.tampilkan_semua_anggota()
                self.kosongkan_form()
                messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menyimpan data anggota: {e}")
        else:
            messagebox.showwarning("Peringatan", "Semua kolom wajib diisi!")

    def pilih_baris_tabel(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_data = self.view.tabel.item(selected_item[0])["values"]

            self.view.entry_nama.delete(0, "end")
            self.view.entry_nama.insert(0, item_data[1])

            if hasattr(self.view, 'txt_alamat'):
                self.view.txt_alamat.delete("1.0", "end")
                self.view.txt_alamat.insert("1.0", item_data[2])
            elif hasattr(self.view, 'entry_alamat'):
                self.view.entry_alamat.delete(0, "end")
                self.view.entry_alamat.insert(0, item_data[2])

    def update_anggota(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris anggota pada tabel yang ingin diperbarui!")
            return

        id_anggota = self.view.tabel.item(selected_item[0])["values"][0]
        nama = self.view.entry_nama.get()
        alamat = self.view.txt_alamat.get("1.0", "end-1c") if hasattr(self.view, 'txt_alamat') else self.view.entry_alamat.get()

        if nama and alamat.strip():
            try:
                self.model.update_anggota(id_anggota, nama, alamat)
                self.tampilkan_semua_anggota()
                self.kosongkan_form()
                messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memperbarui data: {e}")
        else:
            messagebox.showwarning("Peringatan", "Semua kolom wajib diisi!")

    def hapus_anggota(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris anggota pada tabel yang ingin dihapus!")
            return

        id_anggota = self.view.tabel.item(selected_item[0])["values"][0]

        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data anggota ini?"):
            try:
                if hasattr(self.model, 'delete_anggota'):
                    self.model.delete_anggota(id_anggota)
                else:
                    self.model.hapus_anggota(id_anggota)

                self.tampilkan_semua_anggota()
                self.kosongkan_form()
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menghapus data: {e}")

    def kosongkan_form(self):
        self.view.entry_nama.delete(0, "end")
        if hasattr(self.view, 'txt_alamat'):
            self.view.txt_alamat.delete("1.0", "end")
        elif hasattr(self.view, 'entry_alamat'):
            self.view.entry_alamat.delete(0, "end")