import pytest
from models.buku_model import BukuModel

@pytest.fixture
def buku_model():
    # Instansiasi objek model
    return BukuModel()

def test_get_all_buku(buku_model):
    # Panggil fungsi yang diuji
    hasil = buku_model.get_all_buku()

    # Verifikasi hasil berupa tipe list
    assert isinstance(hasil, list), "Hasil pengembalian harus berupa list"

    # Verifikasi elemen dalam list berbentuk tuple/list data (jika ada data)
    if len(hasil) > 0:
        assert len(hasil[0]) == 4, "Setiap baris buku harus memiliki 4 kolom (id, judul, penulis, tahun)"