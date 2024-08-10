from bs4 import BeautifulSoup
import requests
import zipfile
import os
import tqdm
import concurrent.futures
import shutil

def download(link, filename):
    resposta = requests.get(link, stream=True)
    arquivo_zip = filename
    if resposta.status_code == 200:
        with open(arquivo_zip, 'wb') as arquivo:
            total = int(resposta.headers.get('content-length', 0))
            tqdm_params = {
                'desc': link,
                'total': total,
                'miniters': 1,
                'unit': 'B',
                'unit_scale': True,
                'unit_divisor': 1024,
            }
            with tqdm.tqdm(**tqdm_params) as pb:
                for chunk in resposta.iter_content(chunk_size=65536):
                    pb.update(len(chunk))
                    arquivo.write(chunk)
    else:
        resposta.raise_for_status()


def download_file_wrapper(args):
    return download(*args)


def baixar_dados():
    url = 'https://dadosabertos.rfb.gov.br/CNPJ/'
    destino = os.path.join(os.getcwd(), 'dados')

    if not os.path.exists(destino):
        os.mkdir(destino)
    
    shutil.rmtree(destino)
    os.mkdir(destino)

    resposta = requests.get(url)
    pagina = BeautifulSoup(resposta.content, 'html.parser')
    links = []

    for link in pagina.find_all('a'):
        href = link.get('href')
        if href.endswith('.zip'):
            links.append((url + href, os.path.join(destino, href)))

    num_threads = 4
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(download_file_wrapper, links))

    for link, filename in links:
        print('Descompactando ' + filename)
        destino_csv = os.path.join(destino, 'csv')
        with zipfile.ZipFile(filename, 'r') as zip_file:
            novo_nome = os.path.join(destino_csv, filename.split('.')[0] + '.csv')
            if os.path.exists(novo_nome):
                os.remove(novo_nome)
            nome_original = os.path.join(destino_csv, zip_file.namelist()[0])
            zip_file.extractall(destino_csv)
            os.rename(nome_original, novo_nome)
        print(filename + ' descompactado com sucesso')


if __name__ == '__main__':
    baixar_dados()
