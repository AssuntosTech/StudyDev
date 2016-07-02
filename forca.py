word = input("write secret word: ").lower().strip()
for x in range (100):
	print ()
typed = []
correct = []
errors = 0

while True:
	password = ""
	for letters in word:
		password +=letters if letters in correct else "."

	print (password)
	if password == word:
		print ("You are awesome!")
		break

	attempts = input("\nWrite a letter:").lower().strip()
	if attempts in typed:
		print ("You have tried this word!")
		continue

	else:
		typed += attempts
		if attempts in word:
			correct += attempts
		else:
			errors += 1
			print ("You wrong!")

	print ("X ==:==\nX : ")
	print ("x 0 " if errors >= 1 else "X")

	line2 = ""
	if errors == 2:
		line2 = " | "
	elif errors == 3:
		line2 = " \| "
	elif errors >= 4:
		line2 = " \|/ "
	print ("X%s" % line2)
	line3 = ""
	if errors == 5:
		line3 += " / "
	elif errors >= 6:
		line3 += " /\ "
	print ("X%s" % line3)
	print ("X%n=========")
	if errors == 6:
		print ("fuck you dude!")
		break
