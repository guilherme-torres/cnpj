import os
from bd_conexao import conexao
import hashlib

def calcular_hash_dos_arquivos():
    base_dir = os.path.join(os.getcwd(), 'dados', 'csv')
    hashes = []
    arquivos_unicos = [
        'Cnaes.csv', 'Motivos.csv', 'Municipios.csv', 'Naturezas.csv',
        'Paises.csv', 'Qualificacoes.csv', 'Simples.csv'
    ]
    # Hash dos arquivos únicos
    for nome_arquivo in arquivos_unicos:
        with open(os.path.join(base_dir, nome_arquivo), 'rb') as arquivo:
            hash = hashlib.sha256()
            while True:
                bloco = arquivo.read(65536)
                if not bloco:
                    break
                hash.update(bloco)
            hashes.append({'nome': nome_arquivo.lower().split('.')[0], 'hash': hash.hexdigest()})
        print(f'Hash de {nome_arquivo} calculado com sucesso')
    
    # Hash arquivos Empresas
    arquivos_empresas = [nome_arquivo for nome_arquivo in os.listdir(base_dir) if nome_arquivo.startswith('Empresas')]
    hashes_arquivos_empresas = []
    for nome_arquivo in arquivos_empresas:
        with open(os.path.join(base_dir, nome_arquivo), 'rb') as arquivo:
            hash = hashlib.sha256()
            while True:
                bloco = arquivo.read(65536)
                if not bloco:
                    break
                hash.update(bloco)
            hashes_arquivos_empresas.append(hash)
        print(f'Hash de {nome_arquivo} calculado com sucesso')
    hash_grupo_empresas = calcular_hash_dos_pares(hashes_arquivos_empresas)
    hashes.append({'nome': 'empresas', 'hash': hash_grupo_empresas})

    # Hash arquivos Estabelecimentos
    arquivos_estabelecimentos = [nome_arquivo for nome_arquivo in os.listdir(base_dir) if nome_arquivo.startswith('Estabelecimentos')]
    hashes_arquivos_estabelecimentos = []
    for nome_arquivo in arquivos_estabelecimentos:
        with open(os.path.join(base_dir, nome_arquivo), 'rb') as arquivo:
            hash = hashlib.sha256()
            while True:
                bloco = arquivo.read(65536)
                if not bloco:
                    break
                hash.update(bloco)
            hashes_arquivos_estabelecimentos.append(hash)
        print(f'Hash de {nome_arquivo} calculado com sucesso')
    hash_grupo_estabelecimentos = calcular_hash_dos_pares(hashes_arquivos_estabelecimentos)
    hashes.append({'nome': 'estabelecimentos', 'hash': hash_grupo_estabelecimentos})

    # Hash arquivos Socios
    arquivos_socios = [nome_arquivo for nome_arquivo in os.listdir(base_dir) if nome_arquivo.startswith('Socios')]
    hashes_arquivos_socios = []
    for nome_arquivo in arquivos_socios:
        with open(os.path.join(base_dir, nome_arquivo), 'rb') as arquivo:
            hash = hashlib.sha256()
            while True:
                bloco = arquivo.read(65536)
                if not bloco:
                    break
                hash.update(bloco)
            hashes_arquivos_socios.append(hash)
        print(f'Hash de {nome_arquivo} calculado com sucesso')
    hash_grupo_socios = calcular_hash_dos_pares(hashes_arquivos_socios)
    hashes.append({'nome': 'socios', 'hash': hash_grupo_socios})

    return hashes


def calcular_hash_dos_pares(lista):
    tamanho_lista = len(lista)
    if tamanho_lista == 1: return lista[0].hexdigest()
    hash_dos_pares = []
    for i in range(0, tamanho_lista, 2):
        hash = hashlib.sha256()
        if tamanho_lista % 2 != 0 and i == tamanho_lista - 1:
            concatenacao_hashes = lista[i].hexdigest() + lista[i].hexdigest()
            hash.update(bytes(concatenacao_hashes, 'utf-8'))
            hash_dos_pares.append(hash)
            break
        concatenacao_hashes = lista[i].hexdigest() + lista[i + 1].hexdigest()
        hash.update(bytes(concatenacao_hashes, 'utf-8'))
        hash_dos_pares.append(hash)
    return calcular_hash_dos_pares(hash_dos_pares)


def salvar_hashes(hashes):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS arquivos (
        nome VARCHAR(30) NOT NULL,
        hash VARCHAR(64) NOT NULL,
        ultima_modificacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );''')
    for hash in hashes:
        nome_arquivo = hash['nome']
        hash_arquivo = hash['hash']
        cursor.execute('INSERT INTO arquivos (nome, hash) VALUES (%s,%s)', [nome_arquivo, hash_arquivo])
    conn.commit()
    conn.close()


def comparar_hashes():
    hashes = calcular_hash_dos_arquivos()
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM arquivos')
    arquivos = cursor.fetchall()
    arquivos_modificados = []
    for arquivo in arquivos:
        nome = arquivo['nome']
        hash_salvo = arquivo['hash']
        for hash in hashes:
            if hash['nome'] == nome and hash['hash'] != hash_salvo:
                arquivos_modificados.append(nome)
                break
    conn.close()
    return arquivos_modificados


if __name__ == '__main__':
    hashes = calcular_hash_dos_arquivos()
    salvar_hashes(hashes)
    arquivos_modificados = comparar_hashes()
    print(arquivos_modificados)
