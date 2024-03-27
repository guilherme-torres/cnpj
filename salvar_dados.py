from bd_conexao import conexao
import os
import csv

def criar_tabelas():
    conn = conexao()
    with open('criar_tabelas.sql', encoding='utf-8') as arquivo_sql:
        sql = arquivo_sql.read()
        cursor = conn.cursor()
        cursor.execute(sql)
    conn.commit()
    conn.close()


def csv_para_tabela(conexao, nome_tabela):
    base_dir = os.path.join(os.getcwd(), 'dados', 'csv')
    arquivos = [os.path.join(base_dir, arquivo) for arquivo in os.listdir(base_dir) if arquivo.startswith(nome_tabela)]
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {nome_tabela}')
    conn.commit()
    contagem_de_linhas = 0
    for arquivo in arquivos:
        with open(arquivo, encoding='Latin-1') as arquivo_csv:
            reader = csv.reader((linha.replace('\0', '') for linha in arquivo_csv), delimiter=';')
            for row in reader:
                placeholders = ','.join(['%s'] * len(row))
                contagem_de_linhas += 1
                cursor.execute(f'INSERT INTO {nome_tabela} VALUES ({placeholders})', row)
                if contagem_de_linhas == 10000:
                    conn.commit()
                    contagem_de_linhas = 0
            conn.commit()
    conn.close()
    print(f'dados de {nome_tabela} salvos com sucesso')


def salvar_dados():
    arquivos = [
        'Cnaes', 'Paises', 'Municipios', 'Qualificacoes', 'Naturezas',
        'Motivos', 'Simples', 'Empresas', 'Socios', 'Estabelecimentos'
    ]
    for nome in arquivos:
        csv_para_tabela(conexao=conexao, nome_tabela=nome)


def criar_indices():
    conn = conexao()
    with open('criar_indices.sql') as arquivo_sql:
        sql = arquivo_sql.read()
        cursor = conn.cursor()
        cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # salvar_dados()
    # criar_indices()
    criar_tabelas()
