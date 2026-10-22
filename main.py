from utils import garis
from faq import tampilkan_faq


def main():
    menu = {
        "1": ("Pusat Bantuan (FAQ)", tampilkan_faq),
    }
    while True:
        garis("HELPDESK KAMPUS")
        for k, (nama, _) in menu.items():
            print(f"{k}. {nama}")
        print("0. Keluar")
        pilih = input("\nPilih menu: ").strip()
        if pilih == "0":
            print("Terima kasih sudah menghubungi Helpdesk Kampus!")
            break
        if pilih in menu:
            menu[pilih][1]()
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()