import Aula04c as bd

con, cur = bd.conectar()

nome = input('Informe o nome do herói(na)/vilã(o): ')
nome_civil = input('Informe o nome civil do herói(na)/vilã(o): ')
tipo_numerico = input('Tecle 1 para herói(na) e 2 para vilâ(o): ')

# Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == '1':
    tipo = 'Herói(na)'
else:
    tipo = 'Vilã(o)'

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"
cur.execute(sql)
con.commit()
con.close()
