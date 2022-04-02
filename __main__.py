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


def alterar_arquivo_input(caminho: str, arquivo: str):
    with open(os.path.join(caminho, arquivo), 'a') as file:
        file.write('\nCl C O N H 0\n6-31g(d,p)\n****\nPt 0\nlanl2dz\n****\n\nPt 0\nlanl2dz')


if __name__ == '__main__':
    caminho = None
    nome_arquivo = None
    alterar_input = None
    for i in sys.argv:
        if i.lower().startswith('path='):
            caminho = i[len('path='):]
        if i.lower().startswith('name='):
            nome_arquivo = i[len('name='):]
        if i.lower().startswith('alterar_input='):
            alterar_input = i[len('alterar_input='):]

    if caminho:
        if verificar_caminho(caminho):
            files = listar_arquivos(path=caminho)
            if alterar_input:
                for file in files:
                    alterar_arquivo_input(caminho=caminho, arquivo=file)
            nome_script = gerar_arquivo(path=caminho, nome=nome_arquivo, arquivos=files)
            print(f'arquivo gerado! {caminho}\\{nome_script}')
        else:
            print('Pasta informada nao encontrada ou sem arquivos gjf')
    else:
        print('Caminho dos arquivos nao fornecido!')
