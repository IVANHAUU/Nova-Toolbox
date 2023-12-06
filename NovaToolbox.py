import curses
import os
import sys
import importlib

# Adicione o caminho do diretório externo ao sys.path
diretorio_externo = 'Ferramentas'
sys.path.append(diretorio_externo)

# Lista de módulos disponíveis no diretório externo
modulos_disponiveis = [f.replace('.py', '') for f in os.listdir(diretorio_externo) if f.endswith('.py')]

# Função para executar a função contida no módulo
def executar_funcao(modulo):
    modulo_importado = importlib.import_module(modulo)
    if hasattr(modulo_importado, 'funcao_padrao'):
        curses.endwin()
        modulo_importado.funcao_padrao()
    else:
        print(f'O módulo {modulo} não contém uma função chamada "funcao_padrao".')

# Função para a interface curses
def menu_curses(stdscr):
    curses.curs_set(0)  # Esconde o cursor
    selecao_atual = 0

    while True:
        stdscr.clear()
        altura, largura = stdscr.getmaxyx()

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

        welcome = ("»NOVA TOOLBOX v1.0«")
        width = stdscr.getmaxyx()[1]
        x_title = width//2 - len(welcome)//2
        stdscr.addstr(1, x_title, welcome, curses.color_pair(1))

        for idx, modulo in enumerate(modulos_disponiveis):
            x = largura//2 - len(modulo)//2
            y = altura//2 - len(modulos_disponiveis)//2 + idx
            if idx == selecao_atual:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, modulo)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, modulo)

        stdscr.refresh()

        tecla = stdscr.getch()

        if tecla == curses.KEY_UP and selecao_atual > 0:
            selecao_atual -= 1
        elif tecla == curses.KEY_DOWN and selecao_atual < len(modulos_disponiveis) - 1:
            selecao_atual += 1
        elif tecla == curses.KEY_ENTER or tecla in [10, 13]:
            executar_funcao(modulos_disponiveis[selecao_atual])
            stdscr.getch()  # Aguarda uma tecla para continuar
            break

        stdscr.refresh()

# Inicializa a cor
curses.wrapper(menu_curses)
