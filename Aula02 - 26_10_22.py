# Comando input() = server para perguntar / comando de entrada #
nome = input('Digite seu nome: ')
print(f'Seu nome é {nome}.')

# Caso queira expecificar o tipo de input basta fazer assim: #
idade = int(input('Digite sua idade: '))
print(f'Sua idade é {idade} anos.')

# testes com if, else e elif (Condições) #
nome = str(input('Qual o seu nome? '))
idade = int(input('Quantos anos você tem? '))
genero = int(input('Qual o seu gênero?\n[1]Masc\n[2]Fem\n[3]Outro\n===> '))

if genero == 1:
    genero = 'Masculino'
elif genero == 2:
    genero = 'Feminino'
elif genero == 3:
    genero = input('Especifique: ')
else:
    genero = 'Não especificado'

print(f'Você se chama {nome} e tem {idade} anos de idade e seu gênero é {genero}. ', end=' ')
if idade > 18:
    print('Você é maior de idade!!!')
elif idade == 18:
    print('Você agora pode bebêr e dirigir, só não faça as duas coisas juntas!!!')
    if genero == 1:
        print('Você tem que se alistar, fique atento!')
else:
    print('Você é menor de idade!!!')
print(f'O dobro de sua idade é {2*idade} anos.')
