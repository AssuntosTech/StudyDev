#! usr/bin/python3
#-*- encoding:utf-8 -*-
# Pequeno bug, quando se coloca o mesmo valor nas 3 variaveis ele printa o resultado 3 vezes.

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
if a >= b and a >= c :
	print ("O número maior é %d" %a)
if b >= a and b >= c:
	print ("O número maior é %d" %b)
if c >= a and c >= b:
	print ("O número maior é %d" %c);
 
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# if a >= b and a >= c:
#     print ('Maior: %d' %a)
# elif b >= c:
#     print ('Maior: %d' %b)
# else:
#     print ('Maior: %d' %c)
