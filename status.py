from utils import garis
from storage import muat_tiket


def cetak_tiket(t):
    garis(f"TIKET {t['id']}")
    print(f"Nama     : {t['nama']} ({t['nim']})")
    print(f"Prodi    : {t['prodi'] or '-'}")
    print(f"Email    : {t['email']}")
    print(f"Kategori : {t['kategori']}")
    print(f"Status   : {t['status']}")
    print(f"Dibuat   : {t['dibuat']}")
    print(f"Keluhan  : {t['deskripsi']}")
    if t["balasan"]:
        print("\nBalasan Staf:")
        for b in t["balasan"]:
            print(f"  [{b['waktu']}] {b['staf']}: {b['pesan']}")
    else:
        print("\nBelum ada balasan dari staf.")


def cek_status():
    garis("CEK STATUS TIKET")
    kunci = input("Masukkan ID tiket / NIM: ").strip().upper()
    ditemukan = [t for t in muat_tiket()
                 if t["id"].upper() == kunci or t["nim"].upper() == kunci]
    if not ditemukan:
        print("Tiket tidak ditemukan.")
        return
    for t in ditemukan:
        cetak_tiket(t)