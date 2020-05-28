# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:22:50 2020

@author: juanc
"""
"""
# Programación  Lógica



# Modus ponendo ponens

"el modo que, al afirmar, afirma"

P → Q. P ∴ Q


Se puede encadenar usando algunas variables

P → Q. 
Q → S. 
S → T. P ∴ T

Ejercicio 
Defina una funcion que resuelva con verdadero o falso segun corresponada

Laura esta en Queretaro
Alena esta en Paris
Claudia esta en San Francisco
Queretaro esta en Mexico
Paris esta en Francia
San Francisco esta en EUA
Mexico esta en America
Francia esta en Europa
EUA esta en America

def esta(E1,E2):
	pass


print(esta("Alena","Europa"))
# true

print(esta("Laura","America"))
# true

print(esta("Laura","Europa"))
# false

Base = [
	["Laura","Queretaro"],
	["EUA","America"]
]

"""
Base = [
	["Laura","Queretaro"],
    ["Alena","Paris"],
    ["Claudia","San Francisco"],
    ["Queretaro","Mexico"],
    ["Paris","Francia"],
    ["San Francisco","EUA"],
    ["Mexico","America"],
    ["Francia","Europa"],
	["EUA","America"]
]

def donde_esta(X,Y):
	if not X:
		return []
	if len(X):
		if Y == X[0][0]:
			return X[0][1]
		else:
			return donde_esta(X[1:],Y)


def esta (E1,E2):
	R = donde_esta(Base,E1)
	L = donde_esta(Base, R)
	if L == E2 or R == E2:
		return True
	S = donde_esta(Base, L)
	if S == E2:
		return True
	else:
		return False
print(esta("Alena","Europa"))
# true

print(esta("Laura","America"))
# true

print(esta("Laura","Europa"))
# false