import os
import sqlite3
import hashlib

def calcular_hash_dos_arquivos():
    base_dir = os.path.join(os.getcwd(), 'dados', 'csv')
    nome_arquivo_lista = [nome_arquivo for nome_arquivo in os.listdir(base_dir)]
    hashes = []
    for nome_arquivo in nome_arquivo_lista:
        with open(os.path.join(base_dir, nome_arquivo), 'rb') as arquivo:
            hash = hashlib.sha256()
            while True:
                bloco = arquivo.read(65536)
                if not bloco:
                    break
                hash.update(bloco)
            hashes.append({'nome_arquivo': nome_arquivo, 'hash': hash})
        print(f'Hash de {nome_arquivo} calculado com sucesso')
    return hashes


def salvar_hashes(hashes):
    conn = sqlite3.connect('cnpj.db')
    cursor = conn.cursor()
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS arquivos (
        nome VARCHAR(30) NOT NULL,
        hash VARCHAR(64) NOT NULL,
        ultima_modificacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );''')
    for hash in hashes:
        nome_arquivo = hash['nome_arquivo']
        hash_arquivo = hash['hash']
        cursor.execute('INSERT INTO arquivos (nome, hash) VALUES (?,?)', (nome_arquivo, hash_arquivo))
    conn.commit()
    conn.close()


def comparar_hashes():
    pass


if __name__ == '__main__':
    hashes = calcular_hash_dos_arquivos()
    salvar_hashes(hashes)
