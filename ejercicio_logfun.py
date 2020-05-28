*******ejercicio-lugfun************"""
@author: juanc

	https://www.computrabajo.com.mx/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-batch-exp-sistemas-abiertos-en-queretaro-601BC72F6CEBB0F761373E686DCF3405
	En una empresa solicitan Lic./Ing. en Sistemas, Computación o afín.
	con los siguientes requisitos:
	• Oracle BBDD

	• SQL y PL/SQL

	• Linux

	• Unix

	• Shell (Linux - Unix)

	• C++, Proc*C y Tuxedo V12 o anteriores

	• Visual Basic 6.0

	• Java (Frameworks) , Web Services y Micro Servicios APIs
	
	Realizar un programa que realice preguntas al usuario
	y que apartir de sus respuestas evalue si es cadidato o no
	
	(usen conjuntos)
"""

Requisitos = {
	"Oracle","SQL/PL","Linux","Unix","Shell","C++",
	"Proc*C","TuxedoV12", "VB6", "Java","WebServices","MicroServicios"
} 

print(Requisitos)

print("¿ Tiene Una Experiencia Minima de 2 años en los siguientes puntos ?")
print("Escriba SI o NO segun corresponda")

def candidato():
	R1 = input("\n Oracle BBDD   : ").upper()
	R2 = input(" SQL y PL/SQL  : ").upper()
	R3 = input(" Linux         : ").upper()
	R4 = input(" Unix          : ").upper()
	R5 = input(" Shell (Linux - Unix) : ").upper()
	R6 = input(" C++           : ").upper()
	R7 = input(" Proc*C        : ").upper()
	R8 = input(" TuxedoV12     : ").upper()
	R9 = input(" VB6           : ").upper()
	R10 = input(" Java          : ").upper()
	R11 = input(" WebServices   : ").upper()
	R12 = input(" MicroServicios: ").upper()
	ExpUsuario = set()
	if R1 == "SI":
		ExpUsuario.add("Oracle")
	if R2 == "SI":
		ExpUsuario.add("SQL/PL")
	if R3 == "SI":
		ExpUsuario.add("Linux")
	if R4 == "SI":
		ExpUsuario.add("Unix")
	if R5 == "SI":
		ExpUsuario.add("Shell")
	if R6 == "SI":
		ExpUsuario.add("C++")
	if R7 == "SI":
		ExpUsuario.add("Proc*C")
	if R8 == "SI":
		ExpUsuario.add("TuxedoV12")
	if R9 == "SI":
		ExpUsuario.add("VB6")
	if R10 == "SI":
		ExpUsuario.add("Java")
	if R11 == "SI":
		ExpUsuario.add("WebServices")
	if R12 == "SI":
		ExpUsuario.add("MicroServicios")
	ConjDif = Requisitos - ExpUsuario
	ConjInter = Requisitos & ExpUsuario
	print("\nExperiencia Del Usuario ",ExpUsuario)
	print("\nHabilidades Que No Tiene El Usuario ",ConjDif)
	Req = len(Requisitos)
	Experiencia = len(ConjInter)
	ReqMinimos = Req - 4
	if Experiencia >= ReqMinimos:
		return "\nEs Candidato"
	else:
		return "\nNO Es Candidato"

print(candidato())