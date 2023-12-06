def funcao_padrao():
    import os
    import time
    import requests
    import json

    os.system("figlet Consultas")

    print("[1]ip track\n[2]cpf")
    cs = int(input("Selecione: "))

    if cs == 1:
        os.system("figlet IP TRACKER!")
        ipip = requests.get("https://api.ipify.org/")
        print(f"Seu ip é {ipip.text}")
        ip2 = input("IP: ")
        requi = requests.get(f"http://ipwho.is/{ip2}")
        info = json.loads(requi.text)
        time.sleep(2)
        print(f"Latitude:", info["latitude"])
        print(f"Longitude:", info["longitude"])
        print(f"Cidade:", info["city"])
        print( info["region"])