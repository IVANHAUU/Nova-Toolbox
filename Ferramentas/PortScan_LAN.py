def funcao_padrao():
    import socket

    alvo = input("Alvo: ")
    for porta in range(1,65535):
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        if s.connect_ex((alvo, porta)) == 0:
            print(f'Porta {porta} Status - [+]Aberta[+]')
        s.close()