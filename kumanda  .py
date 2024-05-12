import random
import  time


class Kumanda():
    
    
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_liste=["trt"],kanal="trt"):
        self.tv_durum=tv_durum
        
        self.tv_ses=tv_ses
 
        self.kanal_liste=kanal_liste
        
        self.kanal=kanal
        

    def tv_ac(self):
        if (self.tv_durum == "Açık"):
            print("televizyon zaten açık...")
            
        else:
            print("televizyon açılıyor...")
            self.tv_durumu="Açık"
            
    def tv_kapat(self):
        
        if (self.tv_durum =="Kapalı"):
            print("televizyon zaten kapalı")
        else:
            print("televizyon kapanıyor...")
            self.tv_durum ="Kapalı"
            
    def ses_ayarları(self):
        
    
        while True:
        
            cevap = input("sesi azalt:'<'/n sesi artırır: '>' \nçıkış :çıkış")
    
            if (cevap=='<'):
                if(self.tv_ses !=0):
            
                   self.tv_ses -=1
                   print ("ses:",self.tv_ses)
            elif (cevap == ">"):
        
                if (self.tv_ses != 31):
            
                    self.tv_ses += 1
            
                    print("ses:",self.tv_ses)
        
            else:
                print("ses güncellendi:",self.tv_ses)
                break
       
    
    def kanal_ekle (self,kanal_ismi):
        
        print("kanal ekleniyor...")
        time.sleep(1)
        
        
        self.kanal_liste.append (kanal_ismi)
        
        
        print ("kanal eklendi ....")
        
    def rasgele_kanal(self ):
        
        rastgele= random.randint(0,len(self.kanal_liste)-1)
        
        
        self.kanal= self.kanal_listesi[rastgele]
        
        print ("şu anki kanal:",self.kanal)
        
    def __len__ (self):
        
        return len(self.kanal_liste)
    def __str__(self):
        
        return "tv durumu: {}\n tv ses: {}\n şu anki kanal: {}\n".format (self.tv_durum,self.tv_ses,self.kanal_liste)

kumanda = Kumanda()    
    
    
print("""
          Televizyon Uygulaması
          
1. Tv Açma

2.Tv Kapat

3.Ses Ayarları

4.Kanal Ekle

5.Kanal Sayısını Öğrenme

6.Rasgele Kanala Geçme          
          
7.televizyon bilgileri

çıkmak için "q"ya basınıız """)


while True :
    
    işlem = input("işlemi seçiniz")
    
    if (işlem =="q"):
        print("program sonlandırılıyor...")
        break
    elif(işlem =="1"):
        kumanda.tv_ac()
       
       
    elif(işlem =="2"):
         kumanda.tv_kapat()
       
    elif(işlem =="3"):
        kumanda.ses_ayarları()
        
        
    elif (işlem=="4"):
       kanal_isimleri =input("kanal isimlerini ',' ile ayırarak girin:")
       
       kanal_listesi =kanal_isimleri.split(",")
       
       for eklenecekler in kanal_listesi:
           kumanda.kanal_ekle(eklenecekler)
           
    elif (işlem=="5"):
        
        print("kanal sayısı:",len(kumanda))
        
    elif (işlem =="6"):
        kumanda.rasgele_kumanda()
        
    elif (işlem=="7"):
        
        print(kumanda)
        
    else:
        print("geçersiz işlem.....")
        
        
        
        
           
           
        

  


          
          
          
          
          
          
         
    
    
    
    
    
    
    
    
    
    
    
    
    
            