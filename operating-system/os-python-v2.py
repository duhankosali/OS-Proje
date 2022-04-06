from time import sleep
import os
import random

def StartScreen():
    print("PYTHON BASIC OPERATING SYSTEM")
    print("")
    print("Python İşletim Sistemine Hoşgeldiniz.")
    cizgiUret(20)

def LoginScreen():
    print("""

KULLANICI GİRİŞ EKRANI

""")
    sys_username = "duhan"
    sys_password = "123456"
    
    kullanici_adi = input("Kullanıcı Adını Giriniz: ")
    sifre = input("Şifre'yi Giriniz: ")
    
    if (kullanici_adi == sys_username) and (sifre != sys_password):
        return LoginScreenError()
    
    elif (kullanici_adi != sys_username) and (sifre == sys_password):
        return LoginScreenError()
    
    elif (kullanici_adi != sys_username) and (sifre != sys_password):
        return LoginScreenError()
    else:
        print("Giriş yapıldı!")
        print("")

def LoginScreenError():
    print("")
    print("Kullanıcı adı veya parola hatalı!")
    print("Lütfen tekrar deneyiniz.")
    return LoginScreen()



# Olay methodları (İçlerini sonradan dolduracağız)
def StartProcess():
    print("Süreç başlıyor...");
    # Devamı doldurulacak.
def SystemCall():
    print("Sistem çağrısı yapılıyor...");
    # Devamı doldurulacak.
    
def StopProcess():
    print("Süreç sona eriyor...");
    # Devamı doldurulacak.
    

    
# işletim sistemininden çıkış methodu
def ExitOS():
    print("")
    print("İşletim Sisteminden çıkışınız yapılıyor...")
    cizgiUret(20)
    exit(0)


# tasarım amaçlı çizgi üreten method
def cizgiUret(cizgiSayisi):
    cizgi = "-"
    for i in range(cizgiSayisi):
        print(cizgi, end=" ")
        sleep(0.5)



# MAIN KISMI

# Başlangıç ekranı - Start Screen
StartScreen()

# Kullanıcı giriş ekranı - Login Screen
LoginScreen()


# Rastgele sayı üreterek olaylarımızı çağırma işlemi
randomNumbers=[]
counter=0

while counter<=4:
    # Döngüyü sonlandırabilmek için sayacımızı 1 arttırıyoruz.
    counter = counter+1
    # Random sayı üretiyoruz 
    randomNumber = random.randrange(1,100) % 3
    # Random ürettiğimiz sayıyı oluşturduğumuz listemize ekliyoruz.
    randomNumbers.append(randomNumber)
    
    # Listemizdeki elemanlara göre rastgele olaylarımız gerçekleşiyor.
    if (randomNumber==0):
        StartProcess()
    elif (randomNumber==1):
        SystemCall()
    elif (randomNumber==2):
        StopProcess()
    else:
        print("HATA")
    
    sleep(1)


# Sistemden çıkış methodu
ExitOS()




