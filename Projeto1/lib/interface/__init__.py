def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def interface(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[36m{c}\033[m-\033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = int(input('Sua opção: '))
    return opc