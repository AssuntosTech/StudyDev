while True:
	try:
		x = int(input("Adicione um número qualquer: "))
		break
	except ValueError:
		print("Oops!  Esse numero não é valido.  Tente novamente...")
