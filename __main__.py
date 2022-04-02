import os
import sys


def verificar_caminho(path: str) -> bool:
    return os.path.isdir(path) and len([x for x in os.listdir(path) if x.endswith('.gjf')]) > 0


def listar_arquivos(path: str) -> list:
    return [x for x in os.listdir(path) if x.endswith('.gjf')]


def gerar_arquivo(path: str, nome: str = 'script.sh', arquivos=None) -> str:
    if arquivos:
        with open(os.path.join(path, nome), 'w') as file:
            file.write('#!/bin/bash\n')
            for arquivo in arquivos:
                file.write(f'g09 {arquivo} ;\n')
            file.write('&')

    return os.path.join(path, nome)


def alterar_arquivo_input(path: str, arquivo: str):
    with open(os.path.join(path, arquivo), 'a') as file:
        file.write('\nCl C O N H 0\n6-31g(d,p)\n****\nPt 0\nlanl2dz\n****\n\nPt 0\nlanl2dz')


def print_ajuda():
    texto_ajuda = '''
    [ARGUMENTOS]
    path=<caminho dos arquivos>
    name=<nome do arquivo .sh. Caso nao fornecido o nome sera script.sh>
    change_input=<1, se for necessaria a insercao no final dos arquivos. Caso nao seja, nao usar o argumento>
    
    [EXEMPLOS]
    # arquivos na pasta C:\\gjfs, sem alteracao de input, nome do arquivo 'fila.sh'
    python3 . path=C:\\gjfs name=fila.sh
    
    # arquivos na pasta D:\\opts, com alteracao de input, com nome padrao
    python3 . path=D:\\opts change_input=1
    '''
    print(texto_ajuda)


if __name__ == '__main__':
    caminho = None
    nome_arquivo = None
    alterar_input = None
    print_help = None
    for i in sys.argv:
        if i.lower().startswith('-help') or i.lower().startswith('--help'):
            print_help = 1
        elif i.lower().startswith('path='):
            caminho = i[len('path='):]
        elif i.lower().startswith('name='):
            nome_arquivo = i[len('name='):]
        elif i.lower().startswith('change_input='):
            alterar_input = i[len('change_input='):]
    if print_help:
        print_ajuda()
    else:
        if caminho:
            if verificar_caminho(caminho):
                files = listar_arquivos(path=caminho)
                if alterar_input:
                    for file in files:
                        alterar_arquivo_input(path=caminho, arquivo=file)
                nome_script = gerar_arquivo(path=caminho, nome=nome_arquivo, arquivos=files)
                print(f'arquivo gerado! {caminho}\\{nome_script}')
            else:
                print('Pasta informada nao encontrada ou sem arquivos gjf')
        else:
            print('Caminho dos arquivos nao fornecido!')
