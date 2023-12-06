def funcao_padrao():
    import platform

    x = platform.platform()
    b = platform.architecture()
    c = platform.system()
    d = platform.processor()
    l = platform.win32_ver()
    print(x,"\n", b , "\n", c , "\n", d , "\n", l)