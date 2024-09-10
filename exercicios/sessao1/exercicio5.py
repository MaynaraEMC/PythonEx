#5 - Escreva um programa que peça ao usuário para digitar seu peso (em kg) e sua altura (em metros), e calcule seu Índice de Massa Corporal (IMC). 
#A fórmula para o cálculo do IMC é: IMC = peso / (altura ** 2).

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = (peso / (altura ** 2) * 1000) 
print("seu imc é: ", imc)