from bd_conexao import conexao
import os
import csv

def criar_tabelas():
    conn = conexao()
    with open('criar_tabelas.sql') as arquivo_sql:
        sql = arquivo_sql.read()
        cursor = conn.cursor()
        cursor.execute(sql)
    conn.commit()
    conn.close()


def salvar_dados():
    criar_tabelas()

    base_dir = os.path.join(os.getcwd(), 'dados', 'csv')

    # # Cnaes
    # caminho_arquivo = os.path.join(base_dir, 'Cnaes.csv')
    # with open(caminho_arquivo, encoding='Latin-1') as arquivo_csv:
    #     reader = csv.reader(arquivo_csv, delimiter=';')

    #     conn = conexao()
    #     cursor = conn.cursor()
    #     cursor.execute('DELETE FROM cnaes')
    #     conn.commit()
    #     contagem_de_linhas = 0
    #     for row in reader:
    #         contagem_de_linhas += 1
    #         cursor.execute('INSERT INTO cnaes VALUES (%s, %s)', row)
    #         if contagem_de_linhas == 1000:
    #             conn.commit()
    #             contagem_de_linhas = 0
    #     conn.commit()
    #     conn.close()
    #     print('dados de Cnaes salvos com sucesso')

    # # Paises
    # caminho_arquivo = os.path.join(base_dir, 'Paises.csv')
    # with open(caminho_arquivo, encoding='Latin-1') as arquivo_csv:
    #     reader = csv.reader(arquivo_csv, delimiter=';')

    #     conn = conexao()
    #     cursor = conn.cursor()
    #     cursor.execute('DELETE FROM paises')
    #     conn.commit()
    #     contagem_de_linhas = 0
    #     for row in reader:
    #         contagem_de_linhas += 1
    #         cursor.execute('INSERT INTO paises VALUES (%s, %s)', row)
    #         if contagem_de_linhas == 1000:
    #             conn.commit()
    #             contagem_de_linhas = 0
    #     conn.commit()
    #     conn.close()
    #     print('dados de Paises salvos com sucesso')

    # # Municipios
    # caminho_arquivo = os.path.join(base_dir, 'Municipios.csv')
    # with open(caminho_arquivo, encoding='Latin-1') as arquivo_csv:
    #     reader = csv.reader(arquivo_csv, delimiter=';')

    #     conn = conexao()
    #     cursor = conn.cursor()
    #     cursor.execute('DELETE FROM municipios')
    #     conn.commit()
    #     contagem_de_linhas = 0
    #     for row in reader:
    #         contagem_de_linhas += 1
    #         cursor.execute('INSERT INTO municipios VALUES (%s, %s)', row)
    #         if contagem_de_linhas == 1000:
    #             conn.commit()
    #             contagem_de_linhas = 0
    #     conn.commit()
    #     conn.close()
    #     print('dados de Municipios salvos com sucesso')

    # # Qualificacoes
    # caminho_arquivo = os.path.join(base_dir, 'Qualificacoes.csv')
    # with open(caminho_arquivo, encoding='Latin-1') as arquivo_csv:
    #     reader = csv.reader(arquivo_csv, delimiter=';')

    #     conn = conexao()
    #     cursor = conn.cursor()
    #     cursor.execute('DELETE FROM qualificacoes')
    #     conn.commit()
    #     contagem_de_linhas = 0
    #     for row in reader:
    #         contagem_de_linhas += 1
    #         cursor.execute('INSERT INTO qualificacoes VALUES (%s, %s)', row)
    #         if contagem_de_linhas == 1000:
    #             conn.commit()
    #             contagem_de_linhas = 0
    #     conn.commit()
    #     conn.close()
    #     print('dados de Qualificacoes salvos com sucesso')
    
    # # Naturezas
    # caminho_arquivo = os.path.join(base_dir, 'Naturezas.csv')
    # with open(caminho_arquivo, encoding='Latin-1') as arquivo_csv:
    #     reader = csv.reader(arquivo_csv, delimiter=';')

    #     conn = conexao()
    #     cursor = conn.cursor()
    #     cursor.execute('DELETE FROM naturezas')
    #     conn.commit()
    #     contagem_de_linhas = 0
    #     for row in reader:
    #         contagem_de_linhas += 1
    #         cursor.execute('INSERT INTO naturezas VALUES (%s, %s)', row)
    #         if contagem_de_linhas == 1000:
    #             conn.commit()
    #             contagem_de_linhas = 0
    #     conn.commit()
    #     conn.close()
    #     print('dados de Naturezas salvos com sucesso')

    # # Motivos
    # caminho_arquivo = os.path.join(base_dir, 'Motivos.csv')
    # with open(caminho_arquivo, encoding='Latin-1') as arquivo_csv:
    #     reader = csv.reader(arquivo_csv, delimiter=';')

    #     conn = conexao()
    #     cursor = conn.cursor()
    #     cursor.execute('DELETE FROM motivos')
    #     conn.commit()
    #     contagem_de_linhas = 0
    #     for row in reader:
    #         contagem_de_linhas += 1
    #         cursor.execute('INSERT INTO motivos VALUES (%s, %s)', row)
    #         if contagem_de_linhas == 1000:
    #             conn.commit()
    #             contagem_de_linhas = 0
    #     conn.commit()
    #     conn.close()
    #     print('dados de Motivos salvos com sucesso')

    # # Simples
    # arquivos = [os.path.join(base_dir, arquivo) for arquivo in os.listdir(base_dir) if arquivo.startswith('Simples')]
    # conn = conexao()
    # cursor = conn.cursor()
    # cursor.execute('DELETE FROM simples')
    # conn.commit()
    # contagem_de_linhas = 0
    # for arquivo in arquivos:
    #     with open(arquivo, encoding='Latin-1') as arquivo_csv:
    #         reader = csv.reader(arquivo_csv, delimiter=';')
    #         for row in reader:
    #             contagem_de_linhas += 1
    #             cursor.execute('INSERT INTO simples VALUES (%s,%s,%s,%s,%s,%s,%s)', row)
    #             if contagem_de_linhas == 1000:
    #                 conn.commit()
    #                 contagem_de_linhas = 0
    #         conn.commit()
    # conn.close()
    # print('dados de Simples salvos com sucesso')

    # # Empresas
    # arquivos = [os.path.join(base_dir, arquivo) for arquivo in os.listdir(base_dir) if arquivo.startswith('Empresas')]
    # conn = conexao()
    # cursor = conn.cursor()
    # cursor.execute('DELETE FROM empresas')
    # conn.commit()
    # contagem_de_linhas = 0
    # for arquivo in arquivos:
    #     with open(arquivo, encoding='Latin-1') as arquivo_csv:
    #         reader = csv.reader(arquivo_csv, delimiter=';')
    #         for row in reader:
    #             contagem_de_linhas += 1
    #             cursor.execute('INSERT INTO empresas VALUES (%s,%s,%s,%s,%s,%s,%s)', row)
    #             if contagem_de_linhas == 1000:
    #                 conn.commit()
    #                 contagem_de_linhas = 0
    #         conn.commit()
    # conn.close()
    # print('dados de Empresas salvos com sucesso')

    # Estabelecimentos
    arquivos = [os.path.join(base_dir, arquivo) for arquivo in os.listdir(base_dir) if arquivo.startswith('Estabelecimentos')]
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM estabelecimentos')
    conn.commit()
    contagem_de_linhas = 0
    for arquivo in arquivos:
        with open(arquivo, encoding='Latin-1') as arquivo_csv:
            reader = csv.reader((linha.replace('\0', '') for linha in arquivo_csv), delimiter=';')
            for row in reader:
                contagem_de_linhas += 1
                cursor.execute('INSERT INTO estabelecimentos VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
                if contagem_de_linhas == 1000:
                    conn.commit()
                    contagem_de_linhas = 0
            conn.commit()
    conn.close()
    print('dados de Estabelecimentos salvos com sucesso')

    # Socios
    arquivos = [os.path.join(base_dir, arquivo) for arquivo in os.listdir(base_dir) if arquivo.startswith('Socios')]
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM socios')
    conn.commit()
    contagem_de_linhas = 0
    for arquivo in arquivos:
        with open(arquivo, encoding='Latin-1') as arquivo_csv:
            reader = csv.reader(arquivo_csv, delimiter=';')
            for row in reader:
                contagem_de_linhas += 1
                cursor.execute('INSERT INTO socios VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
                if contagem_de_linhas == 1000:
                    conn.commit()
                    contagem_de_linhas = 0
            conn.commit()
    conn.close()
    print('dados de Socios salvos com sucesso')


if __name__ == '__main__':
    salvar_dados()
