import os
import sys


def verificar_caminho(path: str) -> bool:
    return os.path.isdir(path) and len([x for x in os.listdir(path) if x.endswith('.gjf')]) > 0


def listar_arquivos(path: str) -> list:
    return [x for x in os.listdir(path) if x.endswith('.gjf')]


def gerar_arquivo(path: str, nome: str = 'script.sh', arquivos: list = []) -> str:
    with open(os.path.join(path, nome), 'w') as file:
        file.write('#!/bin/bash')
        for arquivo in arquivos:
            file.write(f'g09 {arquivo} ;\n')
        file.write('&')

    return os.path.join(path, nome)


def transformar_executavel(arquivo: str) -> None:
    comando = 'chmod u+x deploy.sh'
    os.system(comando)



if __name__ == '__main__':
    path = None
    nome = None
    for i in sys.argv:
        if i.lower().startswith('path='):
            path = i[len('path='):]
        if i.lower().startswith('name='):
            nome = i[len('name='):]

    if path:
        if verificar_caminho(path):
            arquivos = listar_arquivos(path=path)
            nome_script = gerar_arquivo(path=path, nome=nome, arquivos=arquivos)
            # transformar_executavel(arquivo=nome_script)
            print('arquivo gerado!')
        else:
            print('Pasta informada nao encontrada ou sem arquivos gjf')
    else:
        print('Caminho dos arquivos nao fornecido!')

