#!/usr/bin/python3
# Um programinha para testar como resolver problema de erros, do tipo que fexa sem motivo aparente...
# Nesse exemplo usando o erro da divisão por zero para que possamos entender como funciona, talvez até extrapolar para outras situações, fazendo uso do mesmo mecanismo.

while True:                                 # Para começar um loop, ou seja uma repetição...
	try:                                      # Traduzindo acho que significa tentar.
	        x = int(input("Um numero: "))     #Entrada de numeros inteiros.
        	y = int(input("Dividido por: "))  # Mesmo coisa do anterior
        	x/y                               # Uma divisão
        	break                             # Uma quebra da repetição.
	except ZeroDivisionError:                 # Aqui criamos uma exceção
		print("Não faça isso! Novamente ...")   # Caso ocorra um problema ou uma exceção... o ciclo se repete para que se corrija
print("Parabens, você conseguiu!")          # Não há problemas

# Fim do programa
