#! /usr/bin/python3
#coding: utf-8
try:
	a = int(input("1#: "));
	b = int(input("2#: "));
except:
	print("Insira apenas inteiros...");
	input();

resultado = 0; #variável responsável por acumular o valor de "b".
for i in range(a): #range(a) é a quantidade de vezes que "b" será somado.
	resultado += b; #"b" acumulando em "resultado".

print("\nO resultado é", resultado);