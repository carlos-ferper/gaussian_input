import os
import sys


def verificar_caminho(path: str) -> bool:
    return os.path.isdir(path) and len([x for x in os.listdir(path) if x.endswith('.gjf')]) > 0


def listar_arquivos(path: str) -> list:
    return [x for x in os.listdir(path) if x.endswith('.gjf')]


def gerar_arquivo(path: str, nome: str = 'script.sh', arquivos: list = []) -> str:
    with open(os.path.join(path, nome), 'w') as file:
        file.write('#!/bin/bash\n')
        for arquivo in arquivos:
            file.write(f'g09 {arquivo} ;\n')
        file.write('&')

    return os.path.join(path, nome)


def alterar_arquivo_input(path: str, arquivo: str):
    with open(os.path.join(path, arquivo), 'a') as file:
        file.write('\nCl C O N H 0\n6-31g(d,p)\n****\nPt 0\nlanl2dz\n****\n\nPt 0\nlanl2dz')


if __name__ == '__main__':
    path = None
    nome = None
    alterar_input = None
    for i in sys.argv:
        if i.lower().startswith('path='):
            path = i[len('path='):]
        if i.lower().startswith('name='):
            nome = i[len('name='):]
        if i.lower().startswith('alterar_input='):
            alterar_input = i[len('alterar_input='):]

    if path:
        if verificar_caminho(path):
            arquivos = listar_arquivos(path=path)
            if alterar_input:
                for arquivo in arquivos:
                    alterar_arquivo_input(path=path, arquivo=arquivo)
            nome_script = gerar_arquivo(path=path, nome=nome, arquivos=arquivos)
            print(f'arquivo gerado! {path}\\{nome_script}')
        else:
            print('Pasta informada nao encontrada ou sem arquivos gjf')
    else:
        print('Caminho dos arquivos nao fornecido!')
