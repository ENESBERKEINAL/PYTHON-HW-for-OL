global cik
cik=1

def cikisYap():
    global cik
    cik=0

def degeral():
    global deger
    deger = input("Degerinizi giriniz: ")

def harfYazdır(x):
    for i in str(x):
        print(i)

def asalKontrol(y):
    sayac = 0
    for i in range(2, int(y)):
        if (int(y) % i == 0):
            sayac += 1
            break
    if (sayac != 0):
        print(y,"Sayısı Asal Değildir.")
    else:
        print(y,"Sayısı Asaldır")


while cik==1:
    print("Yazdığınız değer yazı ise harflerini yazdırılacak\n"
          "sayi ise asal olup olmadığı kontrolü yapılacaktır.")
    degeral()
    #isinstance(x,int);
    if deger.isdigit()==True:
        asalKontrol(deger)
    elif type(deger)==str:
        harfYazdır(deger)
    else:
        print("Hatalı tuşlama yaptınız")

    print("Tekrar sayı girmek istiyor musunuz?")
    tez=input("Çıkış yapmak için x e basınız: ")
    if tez=="x":
        cikisYap()
    else:
        print("\tDevam ediliyor...!\n\n")

