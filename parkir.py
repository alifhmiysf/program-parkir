def a():
    masuk=int(input("Masukkan Jam Masuk = "))
    keluar=int(input("Masukkan Jam Keluar ="))
    lama=keluar-masuk
    payment=3000
    
    print("======================================================================")
    print("====================Struk Pembayaran==================================")
    print("Lama Parkir = ", lama, "jam")
    if lama <=1:
        satu_jam_pertama=payment
        print("Biaya Parkir = Rp", satu_jam_pertama)
    elif lama <=10:
        biaya_selanjutnya = (lama-1)*1000+payment
        print("Biaya Parkir =  Rp", biaya_selanjutnya)
    elif lama >=10:
        biaya_selanjutnya = (lama-1)*1000+payment
        print("Biaya Parkir =  Rp", biaya_selanjutnya)
    else:
        print("nul")
    

def b():
    masuk=int(input("Masukkan Jam Masuk = "))
    keluar=int(input("Masukkan Jam Keluar ="))
    lama=keluar-masuk
    payment=5000
    
    print("======================================================================")
    print("====================Struk Pembayaran==================================")
    print("Lama Parkir = ", lama, "jam")
    if lama <=1:
        satu_jam_pertama=payment
        print("Biaya Parkir = Rp", satu_jam_pertama)
    elif lama <=10:
        biaya_selanjutnya = (lama-1)*1000+payment
        print("Biaya Parkir =  Rp", biaya_selanjutnya)
    elif lama >=10:
        biaya_selanjutnya = (lama-1)*1000+payment
        print("Biaya Parkir =  Rp", biaya_selanjutnya)
    else:
        print("nul")
        
def c():
    masuk=int(input("Masukkan Jam Masuk = "))
    keluar=int(input("Masukkan Jam Keluar ="))
    lama=keluar-masuk
    payment=2000
    
    print("======================================================================")
    print("====================Struk Pembayaran==================================")
    print("Lama Parkir = ", lama, "jam")
    if lama <=1:
        satu_jam_pertama=payment
        print("Biaya Parkir = Rp", satu_jam_pertama)
    elif lama <=10:
        biaya_selanjutnya = (lama-1)*1000+payment
        print("Biaya Parkir =  Rp", biaya_selanjutnya)
    elif lama >=10:
        biaya_selanjutnya = (lama-1)*1000+payment
        print("Biaya Parkir =  Rp", biaya_selanjutnya)
    else:
        print("nul")
    


while True:
    print("==================Selamat Datang Di Program Parkir====================")
    print("======================================================================")
    print("1.Parkir Motor")
    print("2.Parkir Mobil")
    print("3.Parkir Sepeda")
    print("4.Keluar Program")
    print("Pilih opsi :")
    print("======================================================================")
    pilih=int(input("Masukan pilihan :"))
    if pilih == 1:
        a()
    elif pilih == 2:
        b()
    elif pilih == 3:
        c()
    elif pilih == 4:
        print("Terimakasih telah Menggunakan program ini")
        break
    
    a=input("Anda Ingin Kembali Ke menu awal y/n")
    if a == "n":
        print("Terimakasih telah Menggunakan program ini")
        break