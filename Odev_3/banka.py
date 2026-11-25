class Hesap :  #class yarattık 
    def __init__(self,hesap_sahibi , hesap_no , bakiye = 0 ): #class içinde constructer metod  oluşturduk 
        self.hesap_sahibi = hesap_sahibi  #properties oluşturduk 
        self.hesap_no = hesap_no            #properties oluşturduk 
        self.bakiye = bakiye                    # properties oluşturduk burda default olarak 0 olmasını amaçladım

    def para_yatir(self,miktar):  #metod oluşturduk class içindeki functionlar metod deniyor. 
        if (miktar > 0):   #yatırılan para poziif olmalı . 
            self.bakiye += miktar  #objectin yeni bakiyesi = eski + miktar 
            print(f"{miktar} TL yatırma işlemi tamamlandı. Güncel bakiye = {self.bakiye} TL") #bilgilendirme metni. 
        else :  # sayı negatifse veya 0 ise 
            print("Lütfen pozitif bir miktar giriniz.") #uyarı mesajı 
    def para_cek(self,miktar): #para çekim metodu 
        if(miktar > 0):  #çekilen para da pozitif olmalı 
            if(miktar > self.bakiye): #çekilen para bakiyeden yüksek olamaz.  
                print(f"Hesap bakiyeniz yetersiz ! Çekebileceğiniz maksimum tutar : {self.bakiye} TL") #uyarı mesajı 
            else :  #her şey okey ise 
                self.bakiye -= miktar  # yeni bakiye = eski - miktar 
                print(f"Hesabınızdan {miktar} TL para çekimi yapıldı. Güncel bakiye = {self.bakiye} TL ") #bilgilendirme metni 
        else :  # çekilen para pozitif değilse 
            print("Lütfen pozitif bir sayı giriniz") # yönlendirme mesajı 
    def hesap_bilgileri(self): #hesap detaylarını görmek için metod 
        print(f"Hesap sahibi:{self.hesap_sahibi}\nHesap no:{self.hesap_no} \nGüncel bakiyeniz : {self.bakiye} TL")  #tüm hesap detaylarını yazdıran metod 

name = input("Merhaba, başlamak için lütfen isminizi giriniz..: ") # ilk value alımı 
no = input("Devam etmek için hesap numarası giriniz..: ") #2. value alımı 

account = Hesap(name,no) #account adında obje yarattım 
while True :  #döngü breaksiz bozulmayacak. 
    print ("\n1 - Para yatır.")   #para yatırma
    print("2 - Para çek.")          #para çekme 
    print("3 - hesap bilgilerini görüntüle.")   #hesap bilgileri 
    print("4 - Çıkış")      #çıkmak için 

    choice = int(input("Lütfen yapmak istediğiniz işlemin numarasını tuşlayınız..:\n")) #choice diye kafama göre değişken oluşturdum ve sayı değeri aldım
    if (choice == 1):  #1i seçtiyse yukarıdaki menüden gözüktüğü gibi para yatırma
        miktar=float(input("Yatırmak istediğiniz miktarı giriniz..:\n")) #inputla miktar alma
        account.para_yatir(miktar)  #objeden metod çağırma 
    elif (choice == 2):  #para çekme tercihi 
        miktar = float(input("Çekmek istediğiniz miktarı giriniz..:\n")) #inputla miktar alma 
        account.para_cek(miktar) #obje üzerinden metod çağırma 
    elif (choice == 3): #hesap bilgilerini görüntüleme 
        account.hesap_bilgileri() #hespa bilgilerini yazdırma. 
    elif (choice == 4 ):  #çıkış yapma
        print("Çıkış yapılıyor , yine bekleriz..:\n ")#çıkış metni.
        break #break komutu 
    else :
        print("Lütfen listeden bir sayı seçiniz..: \n") # girdiği sayı listede yoksa.