#!/usr/bin/python3
# Vamos calcular o volume do cubo.
# Formula básica, 'volume = a*a*a', depois 'área = 6*a*a'
import os
os.system('clear')

print ("""############################################################################
############### Escolha destre as opções seguintes #########################
############ Apenas números de 1 ao 9 são aceitaveis #######################
############################################################################


	1  adição
	2  subtração
	3  multiplicação
	4  divisão
	5  bonus área e volume

""")

ask = int(input("Digite algo entre 1 à 5: "))
if ask == 1:
	os.system('clear')
	print ("""
############################################################################
############### Faça uma simples comta de adição ###########################
######## Qualquer valor é aceitaveis, mas apenas números! ################## 
############################################################################
	""")
	
	adc1 = int(input("valor 1: "))
	adc2 = int(input("valor 2: "))
	print ("O resultadado da soma deu %s" %(adc1+adc2))

if ask == 2:
	os.system('clear')
	print ("""
############################################################################
############### Faça uma simples comta de subtração ########################
######## Qualquer valor é aceitaveis, mas apenas números! ################## 
############################################################################

	""")
	sub1 = int(input("valor 1: "))
	sub2 = int(input("valor 2: "))
	print ("O resultadado da subtração deu %s" %(sub1-sub2))

if ask == 3:
	os.system('clear')
	print ("""
############################################################################
############ Faça uma simples comta de multplicação ########################
######## Qualquer valor é aceitaveis, mas apenas números! ################## 
############################################################################
	""")
	mult1 = int(input("valor 1: "))
	mult2 = int(input("valor 2: "))
	print ("O resultadado da multplicação deu %s" %(mult1*mult2))

if ask == 4:
	os.system('clear')
	print ("""
############################################################################
############## Faça uma simples comta de divizão ###########################
######## Qualquer valor é aceitaveis, mas apenas números! ##################
############################################################################
	""")
	div1 = int(input("valor 1: "))
	div2 = int(input("valor 2: "))
	print ("O resultadado da divisão deu %s" %(div1-div2))

if ask == 5:

	os.system('clear')
	print ("""
#######################################################################
###### 'Bem vindo a sua calculadora interativa de área e volume' ######
## Responda com 2 para 2D(bidimencional) ou 3 para 3D(tridimencional)##
#######################################################################

	""")
	
	dim = int(input("Objeto 2D ou 3D: "))


	if dim == 2:
		os.system('clear')
		print ("""
###################################################################
################## Objeto 2D selecionado ##########################
############### Use apenas numeros de 1 ao 9 ######################
###################################################################

		""")
		x = int(input("Altura: "))
		y = int(input("largura: "))
		n = ("%s x %s" %(x,y))
		print ("A área do quadrado é %s = %s" %(n,x*y))

	if dim == 3:

		os.system('clear')
		print ("""
####################################################################
################## Objeto 3D selecionado ##########################
############### Use apenas numeros de 1 ao 9 ######################
###################################################################
		""")
		x = int(input("Altura: "))
		y = int(input("largura: "))
		z = int(input("Profundidade: "))
		n = ("%s x %s x %s" %(x,y,z))
		print ("volume %s = %s" %(n,x*y*z))
		print ("Área %s x %s = %s" %(x,y,x*y*6))

print ("Até logo!")
