import sys
import getpass
import psycopg
from baixar_dados import baixar_dados
from hash_dos_arquivos import *
from salvar_dados import *

# SCRIPT DE INICIALIZAÇÃO
def init():
    # 1 - baixar dados
    baixar_dados()

    # 2 - setar variaveis de ambiente
    print('-> CONFIGURAR CONEXÃO COM O POSTGRES')
    HOST = input('host: ')
    PORT = input('porta: ')
    DBNAME = input('nome do banco de dados: ')
    DBUSER = input('usuario: ')
    PASSWORD = getpass.getpass(prompt='senha: ')

    with open('.env', 'w') as arquivo_env:
        arquivo_env.write(f"HOST={HOST}\n")
        arquivo_env.write(f"PORT={PORT}\n")
        arquivo_env.write(f"DBNAME={DBNAME}\n")
        arquivo_env.write(f"DBUSER={DBUSER}\n")
        arquivo_env.write(f"PASSWORD={PASSWORD}\n")

    # 3 - criar banco de dados
    conn = psycopg.connect(host=HOST, port=PORT, user=DBUSER, password=PASSWORD, autocommit=True)
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE ' + DBNAME)
    cursor.close()
    conn.close()

    # 4 - salvar hash dos arquivos
    hashes = calcular_hash_dos_arquivos()
    salvar_hashes(hashes)

    # 5 - salvar dados
    salvar_dados()
    
    # 6 - criar indices
    criar_indices()

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == '--init':
            init()
            return
        else:
            print('Uso correto: python main.py --init')
            return
    print('main')
    # SCRIPT QUE SERÁ EXECUTADO MENSALMENTE
    # baixar_dados()
    # arquivos_modificados = comparar_hashes()
    # if len(arquivos_modificados) != 0:
    #     salvar_arquivos_modificados(arquivos_modificados)
    #     for arquivo in arquivos_modificados:
    #         # deletar todos os dados da tabela e salvar novos dados
    #         pass


if __name__ == '__main__':
    main()