# Meu "primeiro" projeto Python #

print("Hello, World!")  # pra deszicar a praga #

nome = 'Bruno'
idade = 19
hobby = 'Academia'

# Ultilizando Fstring #
print(f'Olá {nome}, você tem {idade} anos e tem o hobby de ir a {hobby}\n')

# Concatenada com o "+" - Não funciona com a idade pois a idade é um int/float e naquela situação deveria ser tratada como uma srting(str) #
print("Meu nome é " + nome)
print('Minha idade é ' + str(idade))

# Ultilizando o .format #
print('Meu hobby é ir a {}'.format(hobby))
