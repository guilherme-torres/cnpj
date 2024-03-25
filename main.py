import sys
import getpass
from baixar_dados import baixar_dados
from bd_conexao import conexao
from hash_dos_arquivos import *
from salvar_dados import *

# SCRIPT DE INICIALIZAÇÃO
def init():
    # 1 - baixar dados
    baixar_dados()
    # 2 - setar variaveis de ambiente
    HOST = input('host: ')
    PORT = input('porta: ')
    DBNAME = input('nome do banco de dados: ')
    DBUSER = input('usuario: ')
    PASSWORD = getpass.getpass(prompt='senha: ')

    
    # 3 - criar banco de dados cnpj

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
            print('inicializando...')
            # init()
            sys.exit(0)
        else:
            print('Uso correto: python main.py --init')
            sys.exit(1)

    # SCRIPT QUE SERÁ EXECUTADO MENSALMENTE
    # 1 - baixar dados
    # 2 - comparar hashes dos arquivos
    # 3 - atualizar tabela de hashes com as modificações
    # 4 - ver quais arquivos foram modificados e realimentar a tabela com novos dados
    print('main')


if __name__ == '__main__':
    main()
