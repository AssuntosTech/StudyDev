#!/usr/bin/python3
lista=[]
for L in range(10):
	while True:
		try:
			lista.append(int(input("Digite um valor: ")))
		break
		except:
			print("Digite apenas números!!!")
print (lista)



