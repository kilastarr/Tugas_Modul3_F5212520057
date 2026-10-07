from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel

buku_model = BukuModel()
anggota_model = AnggotaModel()

print("=== PENGUJIAN BUKU MODEL ===")

# 1. Tambah buku dummy dan simpan ID-nya di variabel id_dummy
print("\n[+] Menambahkan data buku...")
id_dummy = buku_model.create_buku("Buku Uji Coba Hapus", "Penulis Test", 2024)

# 2. Update buku ID 7
print("[*] Mengubah data buku ID 7...")
buku_model.update_buku(7, "Pemrograman Python MVC (Edisi Revisi)", "Guido van Rossum", 2024)

# 3. Hapus buku dummy berdasarkan ID dinamis yang baru dibuat
print(f"[-] Menghapus data buku dummy (ID {id_dummy})...")
buku_model.delete_buku(id_dummy)

# 4. Tampilkan daftar buku terkini
print("\n=== Daftar Buku Terkini ===")
for buku in buku_model.get_all_buku():
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")


print("\n=== PENGUJIAN ANGGOTA MODEL ===")

# 1. Tambah data Nala Azura
print("\n[+] Menambahkan data anggota...")
anggota_model.create_anggota("Nalla Azzura", "Jl.Garuda")

# 2. Tampilkan daftar anggota terkini
print("\n=== Daftar Anggota Terkini ===")
for anggota in anggota_model.get_all_anggota():
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")