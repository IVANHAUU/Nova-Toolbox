def funcao_padrao():
    import requests
    import time
    import sys


    lista = ["admin","secreto",".git","git"]
    o = input("site: ")
    ac = requests.get(o)
    if ac.status_code == 200 or ac.status_code >= 299:

        print("[1] Lista padrão [2] Lista customizada")
        oo = input("Escolha: ")
        oo = int(oo)


        if str(oo) == 2:
            f = input("Lista: ")
            for lis in f:
                if o[len(o) -1] == "/":
                        cc = o + lis
                else:
                    cc = o+"/"+lis

                    resposta =  requests.get(cc)
                if resposta.status_code == 200 and resposta.status_code() <= 299:
                        print(f"Diretório achado {cc} | Reqeust:"+resposta)

                elif resposta.status_code >= 400 and  resposta.status_code < 500:
                    print(f"Diretorio não achado{cc} | Request:"+resposta)
        if oo == 1:
            for li in lista:
                if o [len(o) -1] == "/":
                    p = o+li
                else:
                    p = o+"/"+li    
                res = requests.get(p)
                if res.status_code == 200 and res.status_code < 300:
                    print(f"Diretório achado! {res} "+p)
            
                elif res.status_code == 401 or res.status_code == 403:
                    print(f"Diretório não autorizado {res} "+p)
            
                elif res.status_code > 400 and  res.status_code <= 499:
                    print(f"Diretório não achado! ou não autorizado(401, 403) {res} | "+p)
            
                elif res.status_code > 500 and res.status_code <= 599:
                    print(f"Falha no servidor do site! {res} | "+ p)    
    else:
        print("Url inválida!")
        time.sleep(2)
        sys.exit()