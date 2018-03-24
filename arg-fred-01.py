#coding: utf-8

import sys # Biblioteca sys permite usar algumas coisas do SISTEMA OPERACINAL
print("*********************************************\n")

argumento = sys.argv # argv1 metodo // argv2 -> n1 // argv3 -> n2

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def help():
	print("-Bem-vindo ao programa de argumentos do Fred-\n")
	print("-Usando o Programa:\n")
	print("->Carregue o \"python3\" junto com o nome do programa \"arg-fred-01.py\";\n")
	print("->Seguindo o nome do programa são usados três argumentos separados por espaços:\n")
	print("  *1º: \"soma\" para efetuar soma entre o 2º e 3º argumentos ou \"subtracao\" para efetuar subtracao entre o 2º e 3º argumentos.\n")
	print("  *2º: um argumento como número REAL.\n")
	print("  *3º: um argumento como número REAL.\n")

if argumento[1] == "soma":
	resp = soma(float(argumento[2]), float(argumento[3]))
elif argumento[1] == "subtracao":
	resp = subtracao(float(argumento[2]), float(argumento[3]))
elif (argumento[1] == "-h") or (argumento[1] == "-help"):
	resp = help()

print(resp)

print("\n*********************************************")
