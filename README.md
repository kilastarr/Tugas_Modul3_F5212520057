# Sistem Informasi Management Perpustakaan Desktop (MVC)

Aplikasi desktop manajemen data perpustakaan berbasis Python yang dibangun menggunakan **CustomTkinter** untuk antarmuka pengguna (GUI), arsitektur **Model-View-Controller (MVC)**, dan basis data **MySQL (Laragon)**. Aplikasi ini dilengkapi dengan pengamanan kata sandi menggunakan algoritma **SHA-256**, otorisasi berbasis peran (**Role-Based Access Control / RBAC**), serta pengujian otomatis melalui **CI/CD Pipeline (GitHub Actions)**.

---

## 📁 Struktur Direktori Proyek (MVC)

```text
Tugas_Modul3_F5212520057/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml      # Konfigurasi CI/CD Pipeline (GitHub Actions)
├── config/
│   └── database.py              # Koneksi Basis Data MySQL
├── controllers/
│   ├── auth_controller.py       # Logika Autentikasi & Navigasi View
│   ├── buku_controller.py       # Logika Operasi CRUD Data Buku
│   └── anggota_controller.py    # Logika Pengelolaan Data Anggota
├── models/
│   ├── user_model.py            # Model User (Hashing SHA-256 & Auth)
│   ├── buku_model.py            # Model Data Buku (Kueri MySQL)
│   └── anggota_model.py         # Model Data Anggota
├── views/
│   ├── login_view.py            # Form Login GUI (CustomTkinter)
│   ├── buku_view.py             # Form & Tabel Data Buku (GUI + RBAC)
│   └── anggota_view.py          # View Data Anggota
├── tests/
│   ├── test_model.py            # Skrip Pengujian Unit Test Model
│   └── test_buku.py             # Skrip Pengujian Unit Test Buku
├── dist/
│   └── AplikasiPerpustakaan.exe # Standalone Executable (PyInstaller)
├── main.py                      # File Titik Masuk (Entry Point) Aplikasi
├── requirements.txt             # Daftar Dependensi Library Python
└── README.md                    # Dokumentasi Teknis Proyek

