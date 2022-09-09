
arac = []
sayac1 = 0
sayac2 = 0
sayac3 = 0



class sınıf_1():
    def __init__(self,hgs_numarası,isim,soyad,gectigi_tarih,gectigi_saat,bakiye):
        self.hgs_numarası = hgs_numarası
        self.isim = isim
        self.soyad = soyad
        self.gectigi_tarih = gectigi_tarih
        self.gectigi_saat = gectigi_saat
        self.bakiye = bakiye
        self.arac_sınıfı = "1.sınıf"

class sınıf_2():
    def __init__(self,hgs_numarası,isim,soyad,gectigi_tarih,gectigi_saat,bakiye):
        self.hgs_numarası = hgs_numarası
        self.isim = isim
        self.soyad = soyad
        self.gectigi_tarih = gectigi_tarih
        self.gectigi_saat = gectigi_saat
        self.bakiye = bakiye
        self.arac_sınıfı = "2.sınıf"


class sınıf_3():
    def __init__(self,hgs_numarası,isim,soyad,gectigi_tarih,gectigi_saat,bakiye):
        self.hgs_numarası = hgs_numarası
        self.isim = isim
        self.soyad = soyad
        self.gecigi_tarih = gectigi_tarih
        self.gectigi_saat = gectigi_saat
        self.bakiye = bakiye
        self.arac_sınıfı = "3.sınıf"


class gise():
    def __init__(self,bakiye,arac_sınıfı,hgs_numarası):
        self.bakiye = int(bakiye)
        self.arac_sınıfı = arac_sınıfı
        self.hgs_numarası = hgs_numarası


    def odeme(self):
        if (self.arac_sınıfı == "1.sınıf"):
            if(self.bakiye >= 10):
                self.bakiye = self.bakiye - 10
                global  sayac1
                sayac1 += 1
            else:
                print("Bakiye yetersiz")

        elif (self.arac_sınıfı == "2.sınıf"):
            if(self.bakiye >= 20):
                self.bakiye = self.bakiye - 20
                global sayac2
                sayac2 += 1
            else:
                print("Bakiye yetersiz")

        elif (self.arac_sınıfı == "3.sınıf"):
            if(self.bakiye >= 30):
                self.bakiye = self.bakiye - 30
                global sayac3
                sayac3 += 1
            else:
                print("Bakiye yetersiz")

        else:
            print("gecersiz araba sınıfı")


    def gunluk_gecen_araclar(self):
        arac.append(self.hgs_numarası)



class gunluk_bakiye():
    def __init__(self,sayac1,sayac2,sayac3):
        self.sayac1 = sayac1
        self.sayac2 = sayac2
        self.sayac3 = sayac3


    def bakiye(self):
        sınıf1_arac_bakiye = int(sayac1 * 10)
        sınıf2_arac_bakiye = int(sayac2 * 20)
        sınıf3_arac_bakiye = int(sayac3 * 30)
        toplam_bakiye = int(sınıf1_arac_bakiye + sınıf2_arac_bakiye + sınıf3_arac_bakiye)
        print("""sınıf1_arac_toplam_bakiye : {}
sınıf2_arac_toplam_bakiye : {}
sınıf3_arac_toplam_bakiye : {}
toplam_bakiye : {}""".format(sınıf1_arac_bakiye ,sınıf2_arac_bakiye , sınıf3_arac_bakiye , toplam_bakiye))







car1 = sınıf_1("001","ahmet","esmer","07/09/2022","22.10","100")
car2 = sınıf_2("002","burak","esmer","07/09/2022","12.00","200")
car3 = sınıf_3("003","ismail","esmer","07/09/2022","15.12","300")


a = gise(car1.bakiye,car1.arac_sınıfı,car1.hgs_numarası)
a.odeme()
print("{} hgs numaralı aracın kalan bakiyesi : {}".format(a.hgs_numarası,a.bakiye))
a.gunluk_gecen_araclar()


b = gise(car2.bakiye,car2.arac_sınıfı,car2.hgs_numarası)
b.odeme()
print("{} hgs numaralı aracın kalan bakiyesi : {}".format(b.hgs_numarası,b.bakiye))
b.gunluk_gecen_araclar()


c = gise(car3.bakiye,car3.arac_sınıfı,car3.hgs_numarası)
c.odeme()
print("{} hgs numaralı aracın kalan bakiyesi : {}\n".format(c.hgs_numarası,c.bakiye))
c.gunluk_gecen_araclar()


print("{} tarihinde geçen {} hgs numaralı araçlar \n".format(car1.gectigi_tarih,arac))


d = gunluk_bakiye(sayac1,sayac2,sayac3)
d.bakiye()






