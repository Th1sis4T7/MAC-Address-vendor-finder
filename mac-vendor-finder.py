import os , uuid , csv

def check_file():
    if os.path.exists("/usr/share/ieee-data/oui.csv"):
        pass
    else:
        print ("(!) OUI file doesnt exists.\nexiting...")
        exit()
def main(method):
    try:
        if method == 1:
            ousr_mac = hex(uuid.getnode())
            ousr_mac = ousr_mac[2::]
            nusr_mac = str()
            count = 0
            info = list()
            for word in ousr_mac:
                if count % 2 == 0 and count != 0 :
                    nusr_mac += f":{word}"
                else:
                    nusr_mac += word
                count += 1
            with open("/usr/share/ieee-data/oui.csv") as oui:
                reader = csv.reader(oui, delimiter=',')
                for line in reader:
                    if ousr_mac.upper()[0:6] in str(line):
                        info = list(line)
                        break
            print (f"(*) Result:\nMAC address : {nusr_mac}\nVendor info : {info[2]}\nVendor address : {info[3]}")

        elif method == 2:
            ousr_mac = str(input("(*) Enter your MAC address: "))
            nusr_mac = str()
            for word in ousr_mac:
                if word == ":":
                    pass
                else:
                    nusr_mac += word
            with open("/usr/share/ieee-data/oui.csv") as oui:
                reader = csv.reader(oui, delimiter=',')
                for line in reader:
                    if nusr_mac.upper()[0:6] in str(line):
                        info = list(line)
                        break
            print (f"(*) Result:\nMAC address : {ousr_mac}\nVendor info : {info[2]}\nVendor address : {info[3]}")
    except:
        print ("(!) unknown error!")
        exit()

def banner ():
    print ("""
  __  __          _____                       _               __ _           _           
 |  \/  |   /\   / ____|                     | |             / _(_)         | |          
 | \  / |  /  \ | |      __   _____ _ __   __| | ___  _ __  | |_ _ _ __   __| | ___ _ __ 
 | |\/| | / /\ \| |      \ \ / / _ \ '_ \ / _` |/ _ \| '__| |  _| | '_ \ / _` |/ _ \ '__|
 | |  | |/ ____ \ |____   \ V /  __/ | | | (_| | (_) | |    | | | | | | | (_| |  __/ |   
 |_|  |_/_/    \_\_____|   \_/ \___|_| |_|\__,_|\___/|_|    |_| |_|_| |_|\__,_|\___|_|   
                                                                                         
                       Github : https://github.com/Th1sis4T7
                    Telegram Channel : https://t.me/LearnExploit
    """)
    print ("(*) Enter your method:\n1-find local MAC vendor.\n2-find other MAC vendor.")
    try:
        m = int(input("==> "))
        check_file()
        main(m)
    except KeyboardInterrupt:
        pass
    except:
        print ("(!) Something went worng...")
        exit()
banner()