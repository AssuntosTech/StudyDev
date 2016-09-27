#! /usr/bin/python3
#-*- encoding:utf-8 -*-
#Compara os números e aponta qual é o menor e qual é o maior.

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
if a >= b and a >= c:
	print ("O número maior é %d" %a)
elif b >= a and b >= c:
	print ("O número maior é %d" %b)
elif c >= a and c >= b:
	print ("O número maior é %d" %c)

if a <= b and a <= c:
	print ("O número menor é %d" %a)
elif b <= a and b <= c:
	print ("O número menor é %d" %b)
elif c <= a and c <= b:
	 print ("O número menor é %d" %c)
if a == b == c:
	print ("Todos são iguais")

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# if a >= b and a >= c:
#     print ('Maior: %d' %a)
# elif b >= c:
#     print ('Maior: %d' %b)
# else:
#     print ('Maior: %d' %c)
# 
# if a <= b and a <= c:
#     print ('Menor: %d' %a)
# elif b <= c:
#     print ('Menor: %d' %b)
# else:
#     print ('Menor: %d' %c)
