from Projeto1.lib.arquivo import *
from Projeto1.lib.interface import *

ficha = 'cadastros.txt'

if not fichaExiste(ficha):
    criarFicha(ficha)

while True:
    r = interface(['Ver Cadastros', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if r == 1:
        lerFicha(ficha)
    elif r == 2:
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastro(ficha, nome, idade)
    elif r == 3:
        print('\033[32mEncerrando a execução, Até mais!\033[m')
        break
    else:
        print('\033[31mDigite um número válido\033[m')