from time import sleep
import os

def LoginScreen():
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

def LoginScreenError():
    print("")
    print("Kullanıcı adı veya parola hatalı!")
    print("Lütfen tekrar deneyiniz.")
    return LoginScreen()



# Olay methodları (İçlerini sonradan dolduracağız)
def StartProcess():
    print("Süreç başlıyor...");

def SystemCall():
    print("Sistem çağrısı yapılıyor...");
    
def ProcessEnd():
    print("Süreç sona eriyor...");
    

    
# işletim sistemini kapat
def ExitOS():
    print("Python İşletim Sisteminden çıkışınız yapılıyor...")
    cizgiUret(10)
    sleep(3)
    exit(0)



def cizgiUret(cizgiSayisi):
    cizgi = "-"
    for i in range(cizgiSayisi):
        print(cizgi, end=" ")
        sleep(0.5)




# MAIN KISMI

# Başlangıç ekranı - Start Screen
print("PYTHON BASIC OPERATING SYSTEM")
print("")
print("Python İşletim Sistemine Hoşgeldiniz.")

cizgiUret(20)

# Kullanıcı giriş ekranı - Login Screen
print("""

KULLANICI GİRİŞ EKRANI

""")
LoginScreen()



# Olaylar kısmı
liste = [StartProcess(), SystemCall(), ProcessEnd()]



# Sistemden çıkış
#ExitOS()




