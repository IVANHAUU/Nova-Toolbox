def funcao_padrao():
    import socket
    import platform

    print("Socket shell reverse")
    port2 = int(input("Porta: "))
    ip = '127.0.0.1'
    print("Procurando conexões...")
    print(f"HOST: {ip} PORT: {port2}")
    #                            ipv4            tcp
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port2))
    server.listen(1)

    while True:
        exp, con = server.accept()
        print(f"Conectado com {con}")
        print(f"SISTEMA: {platform.platform(con)}")
        command = input("Command:")