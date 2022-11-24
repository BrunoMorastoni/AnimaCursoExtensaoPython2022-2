# 1 - Importação da biblioteca sqlite3
import sqlite3

# 2 - Conexão entre o banco de dados
conexao = sqlite3.connect('dc_universe.db')

# 3 - Criação de um objeto do tipo Cursor
cursor = conexao.cursor()

# 4 - Comando SQL do banco
sql = 'SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas'

# 5 - Executando comando SQL dentro do cursor
cursor.execute(sql)

# 6 - Exibir a consulta com todos nomes de herois e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
    print(pessoa)

for pessoa in pessoas:
    print(f'Nome: {pessoa[1]} ===> {pessoa[3]}')
