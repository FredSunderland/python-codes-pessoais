#coding: utf-8
class Pessoa:
	def __init__(self, nome, idade, sexo):
		self.nome = nome
		self.idade = idade
		self.sexo = sexo

print("\x1b[2J\x1b[1;1H", end="") # Limpar a tela.
decisao = input("\"novo\" para inserir novo usuário e \"sair\" para terminar o programa:\n-> ")
id = []
count = 0

while decisao == "novo":
	nome = input("Nome: ")
	idade = int(input("Idade: "))
	sexo = input("Sexo: ")
	id.append(None) # Apenas cria uma nova posição na lista id.
	id[count] = Pessoa(nome, idade, sexo)
	count += 1
	decisao = input("Inserir novo nome?(digite \"novo\" ou \"sair\")\n-> ")

print("\x1b[2J\x1b[1;1H", end="")
for i in range(count):
	print("Nome:",id[i].nome)
	print("Idade:",id[i].idade)
	print("Sexo:",id[i].sexo)
	print("-"*15)