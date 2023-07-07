import os
import random
import sys
import time

from dict import *

total = []
harga = []
item = []
keranjang = []
kurir_reguler = []
kurir_hemat = []
metode_pembayaran = []
no_rekening_penjual = 1234567810


def welcome():
    """fungsi menampilkan halaman welcome toko"""
    os.system("cls")
    print(
        f"""
{"-"*50}
{"SELAMAT DATANG DI TOKO GROUP ONE": ^50}
{"-"*50}

toko ini menyediakan berbagai produk laptop lenovo 
dan mouse logitech yang hanya bisa dipesan secara online.

lokasi toko : Jakarta
  
              "selamat berbelanja"
              

ketik 1 untuk masuk ke menu toko
"""
    )
    masuk = int(input("= "))

    if masuk == 1:
        menu()
    else:
        exit1()


def menu():
    """fungsi menampilkan menu toko"""
    os.system("cls")
    print(
        f"""
{"menu toko" : ^30}
{"-"*30}
[1] Lihat semua produk
[2] Lihat keranjang
[3] Checkout
[4] Keluar toko

  """
    )
    print("cara memesan")
    print("-------------")
    print("beli produk dulu di menu 1")
    print("dan melihat produk yang sudah di beli di menu 2")
    print("lalu dapat mengcheckoutnya di menu 3")
    print()


def menampilkan_product():
    """fungsi menampilkan product yang dijual"""
    os.system("cls")
    print(f'|  kode      |{"Products": ^35}|         Harga       |')
    print("-" * 80)
    for p in products:
        print(f'kode : {p}\t{products[p]["brand"]}\t\t Rp.{products[p]["harga"]}')
    print()
    print("ketik 1 untuk membeli\nketik 2 untuk kembali ke menu")
    tanya = int(input("= "))
    if tanya == 1:
        pilih_produk()
    elif tanya == 2:
        menu()
    else:
        print("inputan tidak valid")
        time.sleep(1)
        menampilkan_product()


def pilih_produk():
    """fungsi pilih produk"""
    global banyak
    print()
    tanya = "y"
    while tanya == "y":
        choice = int(input("pilih kode product yang mau dibeli = "))
        banyak = int(input("berapa = "))
        item.append(banyak)
        keranjang.append(products[choice])
        harga.append(products[choice]["harga"])
        total.append(products[choice]["harga"] * banyak)
        print()
        tanya = input("ingin menambah produk? (y/n)= ")
    print()
    print("ketik 1 untuk kembali ke menu")
    ask = input("= ")
    if ask == "1":
        menu()
    else:
        menu()


def menampilkan_keranjang():
    """fungsi menampilkan keranjang"""
    os.system("cls")
    print(f'{"keranjang": ^40}')
    print("-" * 40)
    nomor = 1
    index = 0
    for produk in keranjang:
        print(
            f"""
[{nomor}] nama barang = {produk["brand"]}
    harga \t= Rp.{produk["harga"]}
    item \t= {item[index]}
    total\t= Rp.{produk["harga"]*item[index]}"""
        )
        nomor += 1
        index += 1
    print(
        f"""
  total harga = Rp.{sum(total)}
  """
    )
    print()
    print("ketik 1 untuk mengedit keranjang dan ketik 2 untuk kembali ke menu")
    choice = int(input("= "))
    if choice == 1:
        menu_keranjang()
    elif choice == 2:
        menu()
    else:
        print("inputan tidak valid,silahkan inputkan kembali")
        time.sleep(1)
        menampilkan_keranjang()


def menu_keranjang():
    """fungsi menampilkan menu keranjang"""
    os.system("cls")
    print(f'{"Edit Keranjang" : ^30}')
    print("-" * 30)
    print(
        """
[1] Bersihkan keranjang
[2] Hapus produk
[3] Keluar
"""
    )
    pilih_menu_keranjang = int(input("masukkan nomor menu = "))
    if pilih_menu_keranjang == 1:
        bersihkan_keranjang()
    elif pilih_menu_keranjang == 2:
        hapus_product()
    elif pilih_menu_keranjang == 3:
        menu()
    else:
        print("inputan tidak valid, silahkan inputkan kembali")
        time.sleep(1)
        menu_keranjang()


def hapus_product():
    """fungsi menghapus item pada keranjang"""
    os.system("cls")
    print(f'{"keranjang": ^40}')
    print("-" * 40)
    nomor = 1
    index = 0
    for produk in keranjang:
        print(
            f"""
[{nomor}] nama barang = {produk["brand"]}
    harga \t= Rp.{produk["harga"]}
    item \t= {item[index]}
    total\t= Rp.{produk["harga"]*item[index]}"""
        )
        nomor += 1
        index += 1
    print(f"total harga = Rp.{sum(total)}")
    print()
    hapus = int(input("masukkan kode barang yang ingin dihapus = "))
    keranjang.pop(hapus - 1)
    total.pop(hapus - 1)
    print("kembali ke menu untuk mengcheckout produk yang dibeli")
    time.sleep(1)
    menu()


def bersihkan_keranjang():
    """fungsi membersihkan seluruh item keranjang"""
    os.system("cls")
    print(f'{"keranjang": ^40}')
    print("-" * 40)
    nomor = 1
    index = 0
    for produk in keranjang:
        print(
            f"""
[{nomor}] nama barang = {produk["brand"]}
    harga \t= Rp.{produk["harga"]}
    item \t= {item[index]}
    total\t= Rp.{produk["harga"]*item[index]}"""
        )
        nomor += 1
        index += 1
    print(f"total harga = Rp.{sum(total)}")
    keranjang.clear()
    total.clear()
    print("kembali ke menu untuk mengcheckout produk yang dibeli")
    time.sleep(1)
    menu()


def checkout():
    """fungsi checkout keranjang"""
    formulir_pembeli()
    menampilkan_daftar_ekspedisi()


def formulir_pembeli():
    """fungsi formulir data pembeli"""
    os.system("cls")
    global nama, alamat, no
    print("silahkan isi formulir dibawah untuk mengcheckout barang")
    print("-" * 55)
    print()
    nama = input("nama penerima   = ")
    alamat = input("alamat penerima = ")
    try:
        no = int(input("nomor penerima  = "))
    except:
        print()
        print("nomor telepon harus berupa angka")
        time.sleep(2)
        formulir_pembeli()


def display_metode_pembayaran():
    """fungsi memilih metode pembayaran"""
    os.system("cls")
    global pilih_payment
    """fungsi menampilakn metode pembayaran"""
    print(f'{"metode pembayaran": ^20}')
    print("-" * 20)
    print()
    for i in payment_method:
        print(f"[{i}]  {payment_method[i]}  ")
    print()
    print("inputkan nomornya")
    pilih_payment = int(input("= "))
    metode_pembayaran.append(payment_method[pilih_payment])
    struk()


def kode_pembayaran(panjang: int):
    """fungsi menampulkan kode pambayaran"""
    data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSRUVW1234567890"
    token = []
    for i in range(panjang):
        acak = random.randint(0, 58)
        token.append(data[acak])
        x = "".join(token)
        return x


kodepembayaran = kode_pembayaran(12)


def menampilkan_daftar_ekspedisi():
    """fungsi menampilkan daftar ekspedisi"""
    os.system("cls")
    global pilih_ekspedisi
    """fungsi menampilkan opsi ekspedisi hemat dan reguler"""
    print(f'{"opsi ekspedisi": ^30}')
    print("-" * 30)
    print()
    print(f"[1] Hemat   = Rp. 24.000 estimasi ( 4 - 6 hari )")
    print(f"[2] Reguler = Rp. 23.000 estimasi ( 2 - 4 Hari )")
    print()

    pilih_ekspedisi = int(input("pilih ekspedisi = "))
    if pilih_ekspedisi == 1:
        display_ekspedisi_hemat()
    elif pilih_ekspedisi == 2:
        display_ekspedisi_reguler()
    else:
        print("inputan tidak valid, silahkan inputkan kembali")
        time.sleep(1)
        menampilkan_daftar_ekspedisi()


def display_ekspedisi_hemat():
    """fungsi memilih ekspedisi hemat"""
    os.system("cls")
    global pilih_hemat
    print(f'{"daftar ekspedisi hemat" : ^30}')
    print("-" * 30)
    print()
    for i in hemat:
        print(f"[{i}]  {hemat[i]} ")
    print()
    print("pilih ekspedisi")
    pilih_hemat = int(input("= "))
    kurir_hemat.append(hemat[pilih_hemat])
    display_metode_pembayaran()


def display_ekspedisi_reguler():
    """fungsi memilih ekspedisi reguler"""
    os.system("cls")
    global pilih_reguler
    print(f'{"daftar ekspedisi reguler" : ^30}')
    print("-" * 30)
    print()
    for i in reguler:
        print(f"[{i}]  {reguler[i]}")
    print()
    print("pilih ekspedisi")

    pilih_reguler = int(input("= "))
    kurir_reguler.append(reguler[pilih_reguler])
    display_metode_pembayaran()


def exit1():
    os.system("cls")
    """fungsi exit ketika user tidak membeli"""
    print(f"{'-' * 111}")
    print(f'{"TERIMAKASIH TELAH MELIHAT TOKO KAMI" : ^111}')
    print(f'{"JANGAN LUPA BERKUNJUNG KEMBALI" : ^111}')
    print(f'{"TETAP PATUHI+ PROTOKOL KESEHATAN DAN SEHAT SELALU": ^111}')
    print(f"{'-' * 111}")
    sys.exit()


def exit2():
    """fungsi exit ketika user membeli product"""
    print(f"{'-' * 111}")
    print(f'{"TERIMAKASIH TELAH BERBELANJA DI TOKO KAMI" : ^111}')
    print(f'{"JANGAN LUPA MEMBAYARNYA SESUAI METODE YANG DIGUNAKAN  " : ^111}')
    print(f'{"TETAP PATUHI PROTOKOL KESEHATAN DAN SEHAT SELALU": ^111}')
    print(f"{'-' * 111}")
    sys.exit()


def struk():
    """fungsi menampilkan struk"""
    os.system("cls")
    print(f'{"struk pembayaran": ^111}')
    print("-" * 111)
    print(f"nama penerima \t\t= {nama}")
    print(f"alamat penerima \t= {alamat}")
    print(f"momor penerima \t\t= {no}")
    if pilih_ekspedisi == 1:
        print(f"ekspedisi \t\t= {kurir_hemat[0]} - Rp. 14.0000 (4 - 6 hari)")
    elif pilih_ekspedisi == 2:
        print(f"ekspedisi \t\t= {kurir_reguler[0]} - Rp. 24.000 (2 - 4 hari)")
    print(f"metode pembayaran \t= {metode_pembayaran[0]}\n")
    print(f'{"produk yang dibeli" : ^25}')
    print("-" * 25)
    if pilih_ekspedisi == 1:
        nomor = 1
        index = 0
        for produk in keranjang:
            print(
                f"""
  [{nomor}] nama barang = {produk["brand"]}
      harga \t= Rp.{produk["harga"]}
      item \t= {item[index]}
      total\t= Rp.{produk["harga"]*item[index]}"""
            )
            nomor += 1
            index += 1
        print(
            f"\ntotal harga \t\t= Rp. {sum(total)} + 14.000 = Rp. {sum(total) + 14000}"
        )

    elif pilih_ekspedisi == 2:
        nomor = 1
        index = 0
        for produk in keranjang:
            print(
                f"""
  [{nomor}] nama barang = {produk["brand"]}
      harga \t= Rp.{produk["harga"]}
      item \t= {item[index]}
      total\t= Rp.{produk["harga"]*item[index]}"""
            )
            nomor += 1
            index += 1
        print(
            f"\ntotal harga \t\t= Rp. {sum(total)} + Rp. 24.000 = Rp. {sum(total) + 24000}  "
        )

    if pilih_payment == 1 or pilih_payment == 2:
        print(f"\nkode pembayaran  \t= {kodepembayaran}")
    elif pilih_payment == 3:
        print(f'\n{"silahkan tunggu hingga barang sampai"}')
    elif pilih_payment == 4:
        print(f"\nnomor rekekning pembayaran = {no_rekening_penjual}\n")
    exit2()


def main():
    """fungsi utama"""
    welcome()
    while True:
        pilih_menu = int(input("masukkan nomor menu = "))
        if pilih_menu == 1:
            menampilkan_product()
        elif pilih_menu == 2:
            menampilkan_keranjang()
        elif pilih_menu == 3:
            checkout()
        elif pilih_menu == 4:
            exit1()
        else:
            print("inputan tidak valid, silahkan inputkan kembali")
            time.sleep(1)
            menu()


main()
