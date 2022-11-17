#                                       FUNÇÕES                                     #


# calculando apenas 5% de imposto #
preco = 1999.90
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

# Função de calculo de imposto de 5% #
valor = float(input('Digite o valor do produto: '))
calcular_imposto = valor * 0.05
print(
    f'O valor do produto com imposto aplicado é R$: {calcular_imposto:.2f}, sendo R$: {valor:.2f} seu valor original.')

# Calculo de imposto de 7% dentro de uma lista #
valores = [1.99, 24.50, 78.27, 1515.5]
for valor in valores:
    print(f'O imposto de {valor} é {valor*0.07}')

# Declarar um função calcula_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão. #
def calcula_imposto_aliquota(valor, aliquota=7):
    imposto = valor * (aliquota / 100)
    return imposto
