import customtkinter as ctk
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView
from controllers.anggota_controller import AnggotaController

if __name__ == "__main__":
    # 1. Inisialisasi Model dan View untuk Anggota
    model = AnggotaModel()
    view = AnggotaView()

    # 2. Hubungkan ke AnggotaController
    controller = AnggotaController(view, model)

    # 3. Jalankan Loop Utama GUI
    view.mainloop()