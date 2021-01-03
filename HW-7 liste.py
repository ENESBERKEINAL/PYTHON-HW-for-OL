try:
    def listeye_cevir(adi, soyadi, kurum, miktar,yedek:list):
        liste = []
        print("Listeye çevirme işlemi yapılıyor.")
        liste.append(adi)
        liste.append(soyadi)
        liste.append(kurum)
        liste.append(miktar)
        yedek.append(liste)                 #Listemizi küme şeklinde eklemek için böyle bir çözüm buldum kendimce
    def liste_yazdir():
        print("Listemizin tamamı: ")
        print(yedek)

    yedek = []
    print("Müşteri bilgilerini alan programımıza hoşgeldiniz!")
    while True:
        adi = input("Müşterinin adını giriniz: ")
        if adi == "çık":
            liste_yazdir()
            break
        soyadi = input("Müşterinin soyadını giriniz: ")
        kurum = input("Kurum adını giriniz: ")
        miktar = input("Sipariş miktarını giriniz: ")
        listeye_cevir(adi, soyadi, kurum, miktar,yedek)

except:
    print("Hata")
    raise
