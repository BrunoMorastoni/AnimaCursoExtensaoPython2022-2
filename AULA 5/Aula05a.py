#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
bruno = Pessoa(1, 'Bruno G. Morastoni')
print(bruno)

#Quero mostrar só o nome
print(bruno.nome)

#Chama o objeto de banco de dados
db = Database()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll()
for pessoa in pessoas:
  print(pessoa)