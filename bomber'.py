import requests 

def main():
    logo = r'''
       ____    ___       ___      __  __     ____  U _____ u   ____     
    U | __")u / _"\  u  / _"\  uU|' \/ '|uU | __")u\| ___"|/U |  _"\ u  
     \|  _ \/| / U |/  | / U |/ \| |\/| |/ \|  _ \/ |  _|"   \| |_) |/  
      | |_) || \// |,-.| \// |,-.| |  | |   | |_) | | |___    |  _ <    
      |____/  \___/(_/  \___/(_/ |_|  |_|   |____/  |_____|   |_| \_\   
     _|| \\_   //        //     <<,-,,-.   _|| \\_  <<   >>   //   \\_  
    (__) (__) (__)      (__)     (./  \.) (__) (__)(__) (__) (__)  (__) 

nomer = input("Введи номер/write phone number:")

a= requests.get ("https://www.instagram.com/data/manifest.json,"
	json={"phone_number": nomer},)
print(a)
input