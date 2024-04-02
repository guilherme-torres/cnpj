import getpass
import argparse
from baixar_dados import baixar_dados
from hash_dos_arquivos import *
from salvar_dados import *
from bd_conexao import conexao

def init():
    baixar_dados()

    print('-> CONFIGURAR CONEXÃO COM O POSTGRES')
    HOST = input('host: ')
    PORT = input('porta: ')
    DBNAME = 'postgres'
    DBUSER = input('usuario: ')
    PASSWORD = getpass.getpass(prompt='senha: ')

    with open('.env', 'w') as arquivo_env:
        arquivo_env.write(f"HOST={HOST}\n")
        arquivo_env.write(f"PORT={PORT}\n")
        arquivo_env.write(f"DBNAME={DBNAME}\n")
        arquivo_env.write(f"DBUSER={DBUSER}\n")
        arquivo_env.write(f"PASSWORD={PASSWORD}\n")

    criar_tabelas()
    hashes = calcular_hash_dos_arquivos()
    salvar_hashes(hashes)
    salvar_dados()
    criar_indices()


def main():
    parser = argparse.ArgumentParser(
        description='Criar um Banco de Dados com os dados de CNPJ disponibilizados pela Receita Federal do Brasil.'
    )
    parser.add_argument('--init', action='store_true', help='configura e inicializa o Banco de Dados')
    args = parser.parse_args()

    if args.init:
        init()
        return
    
    baixar_dados()
    arquivos_modificados = comparar_hashes()
    if len(arquivos_modificados) != 0:
        print(f'Arquivos modificados -> {arquivos_modificados}')
        salvar_arquivos_modificados(arquivos_modificados)
        for arquivo in arquivos_modificados:
            csv_para_tabela(conexao=conexao, nome_tabela=arquivo['nome'])


if __name__ == '__main__':
    main()
