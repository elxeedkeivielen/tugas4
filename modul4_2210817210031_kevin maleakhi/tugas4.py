while True:
    print("Pilih Program")
    print("1. Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\n5.Exit")
    choice=int(input("Masukkan Pilihan : "))
    if choice==1:
        n1=int(input("Masukkan Nilai Pertama : "))
        n2=int(input("Masukkan Nilai Kedua : "))
        tambah=n1+n2
        print('Hasil Penjumlahan antara','%.2f' %n1 ,'dengan','%.2f' %n2 ,'adalah :','%.2f '%tambah)

    elif choice==2:
        n1=int(input("Masukkan Nilai Pertama : "))
        n2=int(input("Masukkan Nilai Kedua : "))
        kurang=n1-n2
        print('Hasil Pengurangan antara','%.2f' %n1 ,'dengan','%.2f' %n2 ,'adalah :','%.2f '%kurang)
    
    elif choice==3:
        n1=int(input("Masukkan Nilai Pertama : "))
        n2=int(input("Masukkan Nilai Kedua : "))
        kali=n1*n2
        print('Hasil Perkalian antara','%.2f' %n1 ,'dengan','%.2f' %n2 ,'adalah :','%.2f '%kali)
    
    elif choice==4:
        n1=int(input("Masukkan Nilai Pertama : "))
        n2=int(input("Masukkan Nilai Kedua : "))
        bagi=n1/n2
        print('Hasil Pembagian antara','%.2f' %n1 ,'dengan','%.2f' %n2 ,'adalah :','%.2f '%bagi)
                
    elif choice==5:
        print('Terimakasih, telah menggunakan kalkulator kevin maleakhi')
        break
    else:
        print("Input anda salah, silahkan coba lagi")
