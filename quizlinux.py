#!/usr/bin/python3
# Um programa do tipo quiz, só para passar o tempo!!

import os
os.system('clear')

print ("""
################################################################
############## Bem vindo ao Super Quiz #########################
################################################################

Vamos a primeira pergunta!

O que é mais pesado do que um kilo de pão?

1 Um kilo de batata
2 Dois de melancia
3 Quinhentas gramas de maionese

""")


ask1 = int(input("Digite: "))
if ask1 == 1:
    os.system('clear')
    print ("Errado")
if ask1 == 2:
    os.system('clear')
    print ("Correto")
if ask1 == 3:
    os.system('clear')
    print ("Errado")

ask = int(input("Digite 1 se for parar 2 para continuar: "))
if ask == 1:
        os.system('clear')
        print ("Tchau")
if ask == 2:
        os.system('clear')

        print ("""
Vamos a segunda pergunta!

Formula quimica da agua?
1 H2O
2 ISO
3 CNH

""")

        ask2 = int(input("Digite: "))
        if ask2 == 1:
            os.system('clear')
            print ("Correto")
        if ask2 == 3:
            os.system('clear')
            print ("Errado")
        if ask2 == 3:
            os.system('clear')
            print ("Errado")


#   FUTURA PERGUNTA
#       ask = int(input("Digite 1 se for parar 2 para continuar: "))
#       if ask == 1:
#           os.system('clear')
#           print ("Tchau")
#       if ask == 2:
#           os.system('clear')

        print ("Parabéns! Você concluiu o quiz!")
        pass
