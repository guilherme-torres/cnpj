import psycopg
from psycopg.rows import dict_row
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DBNAME = os.getenv('DBNAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

def conexao():
    conn_string = f'host={HOST} port={PORT} dbname={DBNAME} user={USER} password={PASSWORD}'
    conn = psycopg.connect(conn_string, row_factory=dict_row)
    return conn
