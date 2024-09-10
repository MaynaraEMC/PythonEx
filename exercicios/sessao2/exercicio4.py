#Faça um algoritmo que leia o valor de um produto, implemente 5% de desconto em cima do
# valor do produto e imprima o valor com 5% de desconto

valor_atual = float(input("digite o valor atual do produto: "))
valor_desc = valor_atual - (valor_atual * (5 / 100)) 
print(valor_desc) 