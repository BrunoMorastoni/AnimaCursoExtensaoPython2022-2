# 1 - Importação da biblioteca sqlite3
import sqlite3

# 2 - Conexão entre o banco de dados
conexao = sqlite3.connect('dc_universe.db')

# 3 - Criação de um objeto do tipo Cursor
cursor = conexao.cursor()

# 4 - Comando para inserir um heroi/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

# 5 - Executando o comando SQL
print(cursor.execute(sql))

# 6 - Confirmar o INSERT com commit() e fechar o banco
conexao.commit()
conexao.close()
