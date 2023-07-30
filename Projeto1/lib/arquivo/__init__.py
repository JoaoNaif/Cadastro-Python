from Projeto1.lib.interface import *
def fichaExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarFicha(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mNão possível criar este arquivo\033[m')
    else:
        print(f'Arquivo {nome} foi criado com sucesso')


def lerFicha(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro na leitura do arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastro(ficha, nome='Indigente', idade=0):
    try:
        a = open(ficha, 'at')
    except:
        print('\033[31mOcorreu um erro na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mOcorreu um erro na digitação dos dados\033[m')
        else:
            print(f'\033[32mNovo registro de {nome} adicionado!\033[m')
            a.close()