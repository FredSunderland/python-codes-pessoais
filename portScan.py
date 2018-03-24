#coding: utf-8

import time
import socket

host = input("ENTRE COM O HOST A SER EXPLORADO:\n-> ")
print("\nDIGITE O NÚMERO DAS PORTAS PARA O INTERVALO DE VARREDURA:")

portaA = int(input("PORTA INICIAL -> "))
portaB = int(input("PORTA FINAL ---> "))

if (portaA > portaB) or (portaA < 0 or portaA > 65536) or (portaB > 65536):
	while (portaA > portaB) or (portaA < 0 or portaA > 65536) or (portaB > 65536):
		print("\nDigita aê direito o valor das porta, namoral!!\n")
		portaA = int(input("PORTA INICIAL -> "))
		portaB = int(input("PORTA FINAL ---> "))

print("\n")

abertas = []

inicioTempo = time.time()

for port in range(portaA, portaB):
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.settimeout(0.05)

   r = client.connect_ex((host, port))

   if r == 0:
      print(str(port) + " -> Open  ####################")
      abertas.append(port)
   else:
      print(str(port) + " -> Closed")

terminoTempo = time.time()

##########################################################################################################

print("\n##########################################################\n\n")

print("TOTAL DE PORTAS ESCANEADAS:\n-> {}".format(portaB-portaA) )##############

print("\nPORTAS ENCONTRADAS ABERTAS:")##########################################
###
count = 0
if (len(abertas) != 0):
	for aberta in abertas:
		print("-> {}ª porta = {}".format((count+1), aberta))
		count += 1
else:
	print("-> Nenhuma porta aberta foi encontrada... =[")
###
print("\nTOTAL DE PORTAS ABERTAS:\n-> {}".format(len(abertas)))#################

print("\nTEMPO DE EXECUÇÃO:\n-> %.1fs (%.1fmim)." % ( (terminoTempo-inicioTempo), ((terminoTempo-inicioTempo)/60) ) )##########

print("\n##########################################################\n\n@fred_melo_07")

#@fred_melo_07 CODES
