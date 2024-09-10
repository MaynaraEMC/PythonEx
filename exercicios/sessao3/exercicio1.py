import requests 

cep = input("Digite o cep que deseja buscar: ")
link = f'https://viacep.com.br/ws/{cep}/json/'
requisicao = requests.get(link)
print(requisicao)
dic_requisicao = requisicao.json()

print(requisicao.json())