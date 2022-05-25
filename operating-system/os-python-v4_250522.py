from time import sleep
import sys, os
import random
import enum


# işletim sistemininden çıkış methodu
def ExitOS():
    print("")
    print("İşletim Sisteminden çıkışınız yapılıyor...")
    print("Lütfen bekleyiniz.")
    cizgiUret(20)
    


# tasarım amaçlı çizgi üreten method
def cizgiUret(cizgiSayisi):
    cizgi = "-"
    for i in range(cizgiSayisi):
        print(cizgi, end=" ")
        #sleep(0.5)

print("")

# Processlerimizi tutan Enum sınıfımız
class Loglevel(enum.Enum):
    def StartProcess():
         return "Süreç Başlıyor      :"
    def SystemCall():
        return "Sistem Çağrısı      :"
    def StopProcess():
        return "Süreç sonlandı      :"
    def TimerCut():
        return "Zamanlayıcı Kesimi  :"

        

def ScheduleAlgorithm(n):
    
    print("Mevcut süreç sayısı: ",n);
    d = dict()
     
   
    
    for i in range(n):
        key = "P: "+str(liste[i]())
        a = int(input(str(liste[i]())+" için başlangıç zamanını (arrival time) giriniz: "))
        b = int(input(str(liste[i]())+" için çalışma süresi (burst time) giriniz: "))
        l = []
        l.append(a)
        l.append(b)
        d[key] = l
     
    d = sorted(d.items(), key=lambda item: item[1][0])
     
    ET = []
    for i in range(len(d)):
        # first process
        if(i==0):
            ET.append(d[i][1][1])
     
        # get prevET + newBT
        else:
            ET.append(ET[i-1] + d[i][1][1])
     
    TAT = []
    for i in range(len(d)):
        TAT.append(ET[i] - d[i][1][0])
     
    WT = []
    for i in range(len(d)):
        WT.append(TAT[i] - d[i][1][1])
     
    avg_WT = 0
    for i in WT:
        avg_WT +=i
    avg_WT = (avg_WT/n)
     
    print("Process                     | Arrival | Burst | Exit | Turn Around | Wait |")
    for i in range(n):
          print("",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
    print("Ortalama Bekleme Süresi: ",avg_WT)



# MAIN KISMI


# Processlerimizi içeren listemiz.
liste=[Loglevel.StartProcess, Loglevel.SystemCall, Loglevel.StopProcess, Loglevel.TimerCut]

boyut = len(liste)

ScheduleAlgorithm(boyut)



print("")

counter = 0
while counter<=3:
    
    
    print(str(counter)+". eleman için Sanal adres "+str(liste[counter]()))
    print(str(counter)+". eleman için Fiziksel adres "+str(liste[counter]))
    liste[counter]()
    # Döngüyü sonlandırabilmek için sayacımızı 1 arttırıyoruz.
    counter = counter+1




# Sistemden çıkış methodu
ExitOS()