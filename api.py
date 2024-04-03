from fastapi import FastAPI
from bd_conexao import conexao

app = FastAPI()


@app.get('/cnaes/{codigo}')
async def cnaes(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cnaes WHERE codigo=%s', [codigo])
    cnaes = cursor.fetchone()
    cursor.close()
    conn.close()
    return cnaes


@app.get('/paises/{codigo}')
async def paises(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM paises WHERE codigo=%s', [codigo])
    paises = cursor.fetchone()
    cursor.close()
    conn.close()
    return paises


@app.get('/municipios/{codigo}')
async def municipios(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM municipios WHERE codigo=%s', [codigo])
    municipios = cursor.fetchone()
    cursor.close()
    conn.close()
    return municipios


@app.get('/qualificacoes/{codigo}')
async def qualificacoes(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM qualificacoes WHERE codigo=%s', [codigo])
    qualificacoes = cursor.fetchone()
    cursor.close()
    conn.close()
    return qualificacoes


@app.get('/naturezas/{codigo}')
async def naturezas(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM naturezas WHERE codigo=%s', [codigo])
    naturezas = cursor.fetchone()
    cursor.close()
    conn.close()
    return naturezas


@app.get('/motivos/{codigo}')
async def motivos(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM motivos WHERE codigo=%s', [codigo])
    motivos = cursor.fetchone()
    cursor.close()
    conn.close()
    return motivos


@app.get('/empresas/{cnpj_basico}')
async def empresas(cnpj_basico):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM empresas WHERE cnpj_basico=%s', [cnpj_basico])
    empresas = cursor.fetchall()
    cursor.close()
    conn.close()
    return empresas


@app.get('/estabelecimentos/{cnpj_basico}')
async def estabelecimentos(cnpj_basico):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM estabelecimentos WHERE cnpj_basico=%s', [cnpj_basico])
    estabelecimentos = cursor.fetchall()
    cursor.close()
    conn.close()
    return estabelecimentos


@app.get('/simples/{cnpj_basico}')
async def simples(cnpj_basico):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM simples WHERE cnpj_basico=%s', [cnpj_basico])
    simples = cursor.fetchall()
    cursor.close()
    conn.close()
    return simples


@app.get('/socios/{cnpj_basico}')
async def socios(cnpj_basico):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM socios WHERE cnpj_basico=%s', [cnpj_basico])
    socios = cursor.fetchall()
    cursor.close()
    conn.close()
    return socios


@app.get('/porte/{codigo}')
async def porte(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM PorteEmpresa WHERE codigo=%s', [codigo])
    porte = cursor.fetchone()
    cursor.close()
    conn.close()
    return porte


@app.get('/matrizfilial/{codigo}')
async def matrizfilial(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM MatrizFilial WHERE codigo=%s', [codigo])
    matrizfilial = cursor.fetchone()
    cursor.close()
    conn.close()
    return matrizfilial


@app.get('/situacao/{codigo}')
async def situacao(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM SituacaoCadastral WHERE codigo=%s', [codigo])
    situacao = cursor.fetchone()
    cursor.close()
    conn.close()
    return situacao


@app.get('/idsocio/{codigo}')
async def idsocio(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM IdentificacaoSocio WHERE codigo=%s', [codigo])
    idsocio = cursor.fetchone()
    cursor.close()
    conn.close()
    return idsocio


@app.get('/faixaetaria/{codigo}')
async def faixaetaria(codigo):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FaixaEtaria WHERE codigo=%s', [codigo])
    faixaetaria = cursor.fetchone()
    cursor.close()
    conn.close()
    return faixaetaria
