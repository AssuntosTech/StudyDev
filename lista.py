#!/usr/bin/python3
lista=[]
for i in range(3):
	while True:
		try:
			lista.append(int(input('Digite um valor: ')))
		break
		except:
			print ('Digite apenas números!!!')
print (lista)
