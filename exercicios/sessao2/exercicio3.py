#3 - Faça um algoritmo que leia o salário de um
# funcionário e mostre seu novo salário com 15% de aumento.

salario_atual = float(input("Digite seu salário atual: "))
salario_aum = salario_atual + salario_atual * (15 / 100)
print(salario_aum)