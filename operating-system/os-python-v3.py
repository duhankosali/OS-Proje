from time import sleep
import os
import random
import enum


def StartScreen():
    print("PYTHON BASIC OPERATING SYSTEM")
    print("")
    print("Python İşletim Sistemine Hoşgeldiniz.")
    print("Lütfen bekleyiniz.")
    cizgiUret(20)

def LoginScreen():
    print("""
KULLANICI GİRİŞ EKRANI
""")
    sys_username = "duhanenes"
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



# işletim sistemininden çıkış methodu
def ExitOS():
    print("")
    print("İşletim Sisteminden çıkışınız yapılıyor...")
    print("Lütfen bekleyiniz.")
    cizgiUret(20)
    exit(0)



# tasarım amaçlı çizgi üreten method
def cizgiUret(cizgiSayisi):
    cizgi = "-"
    for i in range(cizgiSayisi):
        print(cizgi, end=" ")
        sleep(0.5)



# Processlerimizi tutan Enum sınıfımız
class Loglevel(enum.Enum):
    def StartProcess():
        print("Süreç Başlıyor")
    def SystemCall():
        print("Sistem çağrısı yapılıyor...")
    def StopProcess():
        print("Süreç sona eriyor...")
    def TimerCut():
        print("Zamanlayıcı kesimi...")
        
# MAIN KISMI

# Başlangıç ekranı - Start Screen
StartScreen()

# Kullanıcı giriş ekranı - Login Screen (username: duhanenes, password: 123456)
LoginScreen()


# Processlerimizi içeren listemiz.
liste=[Loglevel.StartProcess, Loglevel.SystemCall, Loglevel.StopProcess, Loglevel.TimerCut()]

# Processlerimizin rastgele çalışmasını sağlayan While döngüsü
counter = 0
while counter<=2:
    
    # Random sayı üretiyoruz 
    randomNumber = random.randrange(1,100) % 3
    
    # Listemizdeki elemanlara göre rastgele olaylarımız gerçekleşiyor.
    liste[counter]()
    sleep(2)
    
    # Döngüyü sonlandırabilmek için sayacımızı 1 arttırıyoruz.
    counter = counter+1


# Sistemden çıkış methodu
ExitOS()