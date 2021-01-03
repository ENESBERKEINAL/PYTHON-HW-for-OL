try:
    global sayi,cikis
    cikis=True
    sayi=27
    def verigir():
        global gir
        gir=input("1-100 arası bir sayı giriniz: ")
    def kontrol():
        global cikis
        if int(gir) == sayi:
            print("Sayıyı doğru tahmin ettiniz.")
            cikis=False
        else:
            print("Bulamadınız.")
    def aralikkontrol():
        if int(gir)>100 or int(gir)<0:
            print("Aralığı aştınız!")

    print("Sayı bulma oyunumuza hoşgeldiniz. Sayıyı tahmin etmek için sadece 3 hakkınız bulunmaktadır.")

    for i in range(1,4):
        verigir()
        aralikkontrol()
        kontrol()
        if i==2:
            print("Son hakkınız iyi düşünün")
        else:
            print("   ",i,". hakkınız tamamlandı")

        if cikis==False:
            break

except ValueError as hata:
    print("Lütfen sadece sayi girişi yapınız.",hata)
except TypeError as hata2:
    print("Type eror hatası ile karşı karşıyayız",hata2)
finally:
    print("Katıldığınız için teşekkürler.")
