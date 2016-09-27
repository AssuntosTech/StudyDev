#! usr/bin/python3
#-*- encoding:utf-8 -*-

peso = float(input("Quantos quilos de peixe você pescou hoje ? "))
if peso > 50:
	maior = peso - 50
	multa = maior * 4
	print ("O valor da sua multa é R$ %1.2f" %multa)
	print ("Você pescou %1.0f KG a mais do que o permitido." %maior)
else:
	print ("Sem multa")
