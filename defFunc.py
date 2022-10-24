while True:
    print("\n")
    print("selamat datang di Warung Midrange ")
    print("---------MENU MAKANAN------- ")
    harga1 = 12000.00
    harga2 = 15000.00
    harga3 = 35000.00
    harga4 = 25000.00
    harga5 = 30000.00
    total1 = (" nasi ayam bakar = " + str (harga1))
    total2 = (" nasi goreng spesial = " + str (harga2))
    total3 = (" rendang = " + str (harga3))
    total4 = (" bubur manado = " + str (harga4))
    total5 = ("soto betawi = " +  str (harga5))
    print("1. nasi ayam bakar ")
    print("2. nasi goreng spesial ")
    print("3. rendang ")
    print("4. bubur manado ")
    print("5. soto betawi ")
    print("\n")
    
    pelanggan = int(input("silahkan pesan makanan sesuai nomor : "))
    if pelanggan == 1 : 
        print(total1)
        print("\n")
        chr = 'Y';
        pelanggan = str(input("ingin melanjutkan pesanan ? (Y/N) "))
        if pelanggan == 'Y' :
            print("\n")
            print("terima kasih sudah memesan kembali, silhkan pilih menu yang tersedia ")
        elif pelanggan == 'N':
            print("baik terima kasih sudah memesan, ---JUMLAH HARGA --- =  ")
            print("\n")
            break
        else :
            print("mohon maaf anda salah menginputkan huruf ")
            break
    
    elif pelanggan == 2:
        print(total2)
        print("\n")
        chr = 'Y';
        pelanggan = str(input("ingin melanjutkan pesanan ? (Y/N) "))
        if pelanggan == 'Y' :
            print("\n")
            print("terima kasih sudah memesan kembali, silhkan pilih menu yang tersedia ")  
        elif pelanggan == 'N':
            print("baik terima kasih sudah memesan, ---JUMLAH HARGA --- =  ")
            print("\n")
            break          
        else :
            print("baik terima kasih sudah memesan ")
            break
    elif pelanggan == 3 : 
        print(total3)
        print("\n")
        chr = 'Y';
        pelanggan = str(input("ingin melanjutkan pesanan ? (Y/N) "))
        if pelanggan == 'Y' :
            print("\n")
            print("terima kasih sudah memesan kembali, silhkan pilih menu yang tersedia ")
        elif pelanggan == 'N':
            print("baik terima kasih sudah memesan, ---JUMLAH HARGA --- =  ")
            print("\n")
            break
        else :
            print("baik terima kasih sudah memesan ")
            break
    elif pelanggan == 4 : 
        print(total4)
        print("\n")
        chr = 'Y';
        pelanggan = str(input("ingin melanjutkan pesanan ? (Y/N) "))
        if pelanggan == 'Y' :
            print("\n")
            print("terima kasih sudah memesan kembali, silhkan pilih menu yang tersedia ")
        elif pelanggan == 'N':
            print("baik terima kasih sudah memesan, ---JUMLAH HARGA --- =  ")
            print("\n")
            break
        else :
            print("baik terima kasih sudah memesan ")
            break
    elif pelanggan == 5 :
        print(total5)
        print("\n")
        chr = 'Y';
        pelanggan = str(input("ingin melanjutkan pesanan ? (Y/N) "))
        if pelanggan == 'Y' :
            print("\n")
            print("terima kasih sudah memesan kembali, silhkan pilih menu yang tersedia ")
        elif pelanggan == 'N':
            print("baik terima kasih sudah memesan, ---JUMLAH HARGA --- =  ")
            print("\n")
            break
        else :
            print("baik terima kasih sudah memesan ")
            break
    else :
        print("mohon maaf anda melebihi batas nomor ")
        print("\n")
        break
    
    

