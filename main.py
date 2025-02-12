import json
import urllib.request
import webbrowser
import os
import sys


class IPAddressLocator:
    def __init__(self):
        self.R = '\033[91m'
        self.B = '\033[1;34m'
        self.W = '\033[0;37m'
        self.G = '\033[1;32m'  # Yeşil renk kodu ekledim
        self.path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')

    def start(self):
        os.system('cls')  # Windows için ekran temizleme komutu
        print(self.B + """
 
                                                                  .   
                                                                .o8   
 .oooo.o oooo  oooo  oo.ooooo.  oo.ooooo.   .ooooo.  oooo d8b .o888oo 
d88(  "8 `888  `888   888' `88b  888' `88b d88' `88b `888""8P   888   
`"Y88b.   888   888   888   888  888   888 888   888  888       888   
o.  )88b  888   888   888   888  888   888 888   888  888       888 . 
8""888P'  `V88V"V8P'  888bod8P'  888bod8P' `Y8bod8P' d888b      "888" 
                      888        888                                  
                     o888o      o888o                                 
                                                                      
 """ + self.W + self.W + """
        
        
         IP Checker
        
    """ + self.W + self.W + """----""" + self.B + """ Github: dk6m """ + self.W + """----""" + self.W + "")

    def m3(self):
        try:
            print(self.W + """\n
    #""" + self.B + """ Select option""" + self.W + """ """ + self.W + """
    
    1)""" + self.W + """ Check your IP""" + self.W + """ 
    2)""" + self.W + """ Check other IP""" + self.W + """
    3)""" + self.W + """ Exit
    """)
            ch = int(input(self.B + "root@you:~$: " + self.W))
            if ch == 1:
                self.main2()
                self.m3()
            elif ch == 2:
                self.main()
                self.m3()
            elif ch == 3:
                print(self.W + "Exit................" + self.W)
                sys.exit(0)
            else:
                print(self.R + "\nInvalid choice, try again\n")
                self.m3()
        except ValueError:
            print(self.R + "\nInvalid choice, try again\n")
            self.m3()

    def finder(self, u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)

                print(self.W + "\n-------------------------------------------1&")
                print(self.W + '\n>>>' + self.B + ' IP address details; \n ')
                print(self.B + "1) IP Address : " + self.W, data['query'], '\n')
                print(self.B + "2) Org : " + self.W, data['org'], '\n')
                print(self.B + "3) City : " + self.W, data['city'], '\n')
                print(self.B + "4) Region : " + self.W, data['regionName'], '\n')
                print(self.B + "5) Country : " + self.W, data['country'], '\n')
                print(self.B + "6) Location\n")
                print(self.B + "7) Lattitude : " + self.W, data['lat'], '\n')
                print(self.B + "8) Longitude : " + self.W, data['lon'], '\n')
                l = 'https://www.google.com/maps/place/' + str(data['lat']) + '+' + str(data['lon'])
                print(self.B + "\n#" + self.B + " Google Map link : " + self.B, l)
                path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link = 'am start -a android.intent.action.VIEW -d ' + str(l)
                    pr = input(self.B + "\n>>>" + self.W + " Open link in browser?" + self.G + " (y|n): " + self.W)
                    if pr == "y":
                        lnk = str(link) + " > /dev/null"
                        os.system(str(lnk))
                        self.start()
                        self.m3()
                    elif pr == "n":
                        print("\nCheck another IP or exit using Ctrl + C\n\n")
                        self.start()
                        self.m3()
                    else:
                        print("\nInvalid choice! Please try again\n")
                        self.m3()
                else:
                    pr = input(self.W + "\n>>" + self.W + " Open link in browser?" + self.B + " (y|n): " + self.W)
                    if pr == "y":
                        webbrowser.open(l, new=0)
                        self.start()
                        self.m3()
                    elif pr == "n":
                        print(self.B + "\n----------------------------------------------------------1")
                        print(self.W + "\nCheck another IP or exit using " + self.B + "Ctrl + C\n\n")
                        self.start()
                        self.m3()
                    else:
                        print( + "\nInvalid choice! Try again\n")
                        self.m3()
                return
            except KeyError:
                print(self.R + "\nError! INVALID IP/URL!\n" + self.W)
                self.m3()
        except urllib.error.URLError:
            print(self.R + "\nError!" + self.R + "Bro, Check Your Internet Connection\n" + self.W)
            exit()

    def main(self):
        u = input(self.G + "\n>>> " + self.W + "Enter IP Address/URL:" + self.W + " ")
        if u == "":
            print(self.R + "\nBROOO ENTER VALID IP ADDRESS/URL !!!!")
            self.main()
        else:
            url = 'http://ip-api.com/json/' + u
            self.finder(url)

    def main2(self):
        url = 'http://ip-api.com/json/'
        self.finder(url)

    def run(self):
        try:
            self.start()
            self.m3()
        except KeyboardInterrupt:
            print(self.B + "\nbye." + self.W)

if __name__ == "__main__":
    ip_locator = IPAddressLocator()
    ip_locator.run()
