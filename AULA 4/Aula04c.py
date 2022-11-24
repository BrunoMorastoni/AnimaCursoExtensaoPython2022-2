# 1 - Importação da biblioteca sqlite3
import sqlite3

# 2 e 3- função conectar()
def conectar():
    conexao = sqlite3.connect('dc_universe.db')
    cursor = conexao.cursor()
    return conexao, cursor
