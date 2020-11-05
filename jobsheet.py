#Sistem Matematika
#Membuat Program Menghitung Luas dan keliling Bangun Datar 




from Ipython.display import clear_output

def cls() :
    clear_output(True)


def luas_persegi (s):
    luas = s*s
    return luas
def keliling_persegi (s):
    keliling = 2*(s+s)
    return keliling
def luas_persegipanjang (p,l):
    luas = p*l
    return luas
def keliling_persegipanjang (p,l):
    keliling = 2*(p+l)
    return keliling
def luas_segitiga (a,t):
    luas = (a*t)/2
    return luas
def keliling_segitiga (a,b,c):
    keliling = a+b+c
    return keliling
def luas_lingkaran (r):
    luas = 3,14*r*r
    return luas
def keliling_lingkaran (r):
    keliling = 2*3,14*r
    return keliling
def luas_jajargenjang (a,t):
    luas = a*t
    return luas
def keliling_jajargenjang (a,b):
    keliling = 2*(a+b)
    return keliling
pilihan = 1
while pilihan!=0:
    print("1. Luas persegi")
    print("2. Keliling persegi")
    print("3. Luas persegi panjang")
    print("4. Keliling persegi panjang")
    print("5. Luas segitiga")
    print("6. Keliling segitiga")
    print("7. Luas lingkaran")
    print("8. Keliling lingkaran")
    print("9. Luas jajar genjang")
    print("0. Keliling jajar genjang")
