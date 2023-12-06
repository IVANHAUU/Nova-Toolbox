def funcao_padrao():
    import requests

    a = ["secreto","sec","admin","www", "support"]
    v = input("Url:")
    for su in a:
        ss = "https://"+su+"."+v
        try:
            resp = requests.get(ss)
            print(f"Site encontrado! {ss}")
        except:
            print(f"Subdominio não encontrado {ss}")