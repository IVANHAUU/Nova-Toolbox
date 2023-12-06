def funcao_padrao():
    import subprocess
    import time

    green = "\033[0;32m"
    red = "\033[0;31m"
    white = "\033[0;37m"
    print("*********************")
    print("**Mudar Mac Address**")
    print("*********************")

    interface = input("Interface: ")
    Mac_new = input("Mac desejado: ")

    subprocess.call(["ifconfig", interface, "down"])
    print(green+"Desabilitando a interface: "+red+f"{interface}")
    time.sleep(1)
    subprocess.call(["ifconfig", interface, "hw", "ether", Mac_new])
    subprocess.call(["ifconfig", interface, "up"])
    print(green+"[+]Mac Mudado com sucesso[+]"+white)