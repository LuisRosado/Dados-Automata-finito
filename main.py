import random
from typing import get_type_hints

class Automata:
    def __init__(self,cadena):
        self.cadena=cadena
    def Aut(self):
        self.estado=1
        for i in range (0,len(self.cadena)):
            self.transicion=self.cadena[i]
            """""
            A U T O M A T A   F I N I T O
            Q = {1,2,3,4,5,6}
            A = {0,1,2}
            q0 = 1
            F = 6
            s = {1x0=2, 1x1=2, 2x0=3, 2x1=3, 3x0=4, 3x1=4, 4x0=5, 4x1=5, 5x0=6, 5x1=6, 6x2=5}
            """

            #Estado inicial q0
            if self.estado == 1:
                if str.isdigit(self.transicion):
                    if self.transicion == '1' or self.transicion == '0':
                        self.estado=2
                    else:
                        return False
                else:
                    return False
            #Segundo estado
            elif self.estado == 2:
                if str.isdigit(self.transicion):
                    if self.transicion == '1' or self.transicion == '0':
                        self.estado=3
                    else:
                        return False
                else:
                    return False
            # Tercer estado
            elif self.estado == 3:
                if str.isdigit(self.transicion):
                    if self.transicion == '1' or self.transicion == '0':
                        self.estado=4
                    if self.transicion == '4':
                        self.estado=5
                    else:
                        return False
                else:
                    return False
            # Cuarto estado
            elif self.estado == 4:
                if str.isdigit(self.transicion):
                    if self.transicion == '1' or self.transicion == '0':
                        self.estado=5
                    if self.transicion == '3':
                        self.estado=1
                    else:
                        return False
                else:
                    return False
            # Quinto estado
            elif self.estado == 5:
                if str.isdigit(self.transicion):
                    if self.transicion == '1' or self.transicion == '0':
                        self.estado=6
                    else:
                        return False
                else:
                    return False
            # Sexto estado (Estado de aceptacion)
            elif self.estado == 6:
                if str.isdigit(self.transicion):
                    if self.transicion == '2':
                        self.estado=1
                    else:
                        return False
                else:
                    return False
        if self.estado == 6:
            return True
        else:
            return False


valorMin = 1
valorMax = 6

intentos = 1
correctos = 0
maxIntentos = 6
cadena = ""
jugar_otra_vez = "si"



print("Hola! Cual es tu nombre?: ")
username = input()

print("Bueno, "+ username + ". Debes adivinar el numero que saldra al tirar los dados (numero entre 2 y 12)")

while intentos < maxIntentos:
    print("")
    print("------------------------------------------------------")
    print("Adivina: ")
    respuesta = input()
    respuesta = int(respuesta)
    if respuesta >= 2 and respuesta <= 12:
        Dado1 = random.randint(valorMin, valorMax)
        Dado2 = random.randint(valorMin, valorMax)
        SumaDados = Dado1 + Dado2


        print("Primer Dado: " + str(Dado1))
        print("Segundo Dado: " + str(Dado2))
        print("Suma de ambos Dados: " + str(SumaDados))

        if respuesta != SumaDados:
            print("TU RESPUESTA ES INCORRECTA")

            if intentos == 3:
                maxIntentos = maxIntentos-2
                cadena = str(cadena) + str(4)
            else: cadena = str(cadena) + str(0)

        if respuesta == SumaDados:
            print("TU RESPUESTA ES CORRECTA")
            correctos = correctos + 1
            if intentos == 4:
                maxIntentos = maxIntentos+3;
                cadena = str(cadena) + str(3)
            else: cadena = str(cadena) + str(1)




        print("------------------------------------------------------")
        print("")
        intentos = intentos+1
    else:
        print("Ese numero no es valido...")

    if (5-intentos) < 0 and correctos < 1:
        intentos = 0
    else:
        print("Te quedan " + str(4 - intentos) + " intentos.")
        print("Acierto: " + str(correctos))

#Validacion por el automata

print("\n***********")
print("Cadena: "+str(cadena))
AFD=Automata(cadena)
if AFD.Aut() == True:
    print("Es una cadena Valida.")
else:
    print("Es una cadena Valida.")
