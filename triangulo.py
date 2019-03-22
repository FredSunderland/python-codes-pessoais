#! /usr/bin/python3
#coding: utf-8
from math import *
try:
	hipotenusa = int(input("Hipotenusa: "));
	cateto1 = int(input("Cateto1: "));
	cateto2 = int(input("Cateto2: "));
except:
        print("\nDigite apenas inteiros!");
        input();
if (hipotenusa >= (cateto1 + cateto2)):
        print("\nNão é um triangulo!");
elif (cateto1 > 0 and cateto2 > 0):
        print("\nÉ um triangulo");

	#Semiperímetro do Triângulo:
        s=(hipotenusa+cateto1+cateto2)/2;
        #Teorema de Herão:
        area=sqrt(s*(s-hipotenusa)*(s-cateto1)*(s*cateto2));

        print("Área do triângulo: {:.2f}.".format(area));