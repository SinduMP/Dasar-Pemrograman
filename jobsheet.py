#Sistem Matematika
#Membuat Program Menghitung Luas dan keliling Bangun Datar 


from Ipython.display import clear_output

def cls() :
    clear_output(True)

pilihan = 1
while pilihan !=0:
    print("1. menghitung Luas bujur sangkar")
    print("2. menghitung Keliling bujur sangkar")
    print("3. menghitung Luas persegi panjang")
    print("4. menghitung Keliling persegi panjang")
    print("5. menghitung Luas segitiga")
    print("6. menghitung Keliling segitiga")
    print("7. menghitung Luas lingkaran")
    print("8. menghitung Keliling lingkaran")
    print("9. menghitung Luas jajar genjang")
    print("10. menghitung Keliling jajar genjang")
    
    pilihan = int(input("masukkan pilihan : "))
    print('')
    print('')
    
    if pilihan == 1 :
        print("Luas bujur sangkar")
        print('')
        s=int(input("Masukkan sisi:"))
        print("Luas bujur sangkar adalah:",luas_bujur_sangkar(s))
        print('')
        print('')
    elif pilihan==2:
        print("Keliling bujur sangkar")
        print('')
        s=int(input("Masukkan sisi:"))
        print("Keliling bujur sangkar adalah :",keliling_bujur_sangkar(s))
        print('')
        print('')
    elif pilihan==3:
        print("Luas persegi panjang")
        print('')
        p=int(input("Masukkan panjang:"))
        l=int(input("Masukkan lebar:"))
        print("Luas persegi panjang adalah :",luas_persegi_panjang(p,l))
        print('')
        print('')
    elif pilihan==4:
        print("Keliling persegi panjang")
        print('')
        p=int(input("Masukkan panjang:"))
        l=int(input("Masukkan lebar:"))
        print("Keliling persegi panjang adalah:",keliling_persegi_panjang(p,l))
        print('')
        print('')
    elif pilihan==5:
        print("Luas segitiga")
        print('')
        a=int(input("Masukkan alas:"))
        t=int(input("Masukkan tinggi:"))
        print("Luas segitiga adalah:",luas_segitiga(a,t))
        print('')
        print('')
    elif pilihan==6:
        print("Keliling segitiga")
        print('')
        a=int(input("Masukkan sisi a:"))
        b=int(input("Masukkan sisi b:"))
        c=int(input("Masukkan sisi c:"))
        print("Keliling segitiga adalah:",keliling_segitiga(a,b,c))
        print('')
        print('')
    elif pilihan==7:
        print("Luas lingkaran")
        print('')
        r=int(input("Masukkan jari jari:"))
        print("Luas lingkaran adalah:",luas_lingkaran(r))
        print('')
        print('')
    elif pilihan==8:
        print("Keliling Lingkaran")
        print('')
        r=int(input("Masukkan jari jari:"))
        print("Keliling lingkaran adalah:",keliling_lingkaran(r))
        print('')
        print('')
    elif pilihan==9:
        print("Luas jajar genjang")
        print('')
        a=int(input("Masukkan alas:"))
        t=int(input("Masukkan tinggi:"))
        print("Luas jajar genjang adalah:",luas_jajar_genjang(a,t))
        print('')
        print('')
    elif pilihan==10:
        print("Keliling jajar genjang")
        print('')
        a=int(input("Masukkan nilai a:"))
        b=int(input("Masukkan nilai b:"))
        print("Keliling jajar genjang adalah:",keliling_jajar_genjang(a,b))
        print('')
        print('')
    else:
        print("Input yang anda masukkan salah")
        ptint('')
        print('')
        
