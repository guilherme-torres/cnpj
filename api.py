# import json
from fastapi import FastAPI
# from fastapi.responses import Response
from bd_conexao import conexao

app = FastAPI()


@app.get("/")
async def root():
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cnaes')
    dados_cnaes = cursor.fetchall()
    cursor.close()
    conn.close()
    # dados_json = json.dumps(dados_cnaes, ensure_ascii=False).encode('utf-8')
    # resposta = Response(content=dados_json, media_type='application/json')
    return dados_cnaes
