def funcao_padrao():
    import whois

    print("********************")
    print("**Consulta de Site**")
    print("********************")
    a = input("Url: ")
    res = whois.whois(a)
    print(res.text)
    f = whois.all
    print(f.text)