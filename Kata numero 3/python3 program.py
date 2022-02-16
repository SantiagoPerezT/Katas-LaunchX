#program python
sum= 1+2;
print("El resultado es", sum);

#ejemplo
suma= 1+2+3;
product= suma*2;
print("aqui esta tu resultado", product);

#Ejemplo de tipo de variables

planetas_en_el_sistema_solar= 8; # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri= 4.367; # float, años luz
puede_despegar= True;
transbordador_que_aterrizo_en_la_luna= ("Apollo 11"); #string
distancia_a_alfa_centauri = 4.367; # Aparece un decimal por lo tanto es un flotante

#La otra forma es usar la función:type()

print(type(distancia_a_alfa_centauri));

#Operadores

#existen 2 tipos los aritmeticos y los de asignacion

#Aritmenticos

#+	Operador de adición que suma dos valores juntos	1 + 1
#-	Operador de resta que quita el valor del lado derecho del lado izquierdo	1 - 2
#/	Operador de división que divide el lado izquierdo tantas veces como especifique el lado derecho	10 / 2
#*	Operador de multiplicación	2 * 2

#Asignacion

#=	x = 2
#x ahora contiene 2.

#+=	x += 2
#x incrementado en 2. Si antes contenía 2, ahora tiene un valor de 4.

#-=	x -= 2
#x decrementado por 2. Si antes contenía 2, ahora tiene un valor de 0.

#/=	x /= 2
#x dividido por 2. Si antes contenía 2, ahora tiene un valor de 1.

#*=	x *= 2
#x multiplicado por 2. Si antes contenía 2, ahora tiene un valor de 4.

#---------Fecha--------------#

# Obtenemos la fecha de hoy
from datetime import date
# Obtenemos la fecha de hoy
date.today();
# Mostramos la fecha en la consola
print(date.today());

print("el dia de hoy es: " + str(date.today()));

#-------Recopilador de informacion-------#

#print("Bienvenido al programa de bienvenida")
#name = input("Introduzca su nombre ")
#print("Saludos: " + name)

print("Calculadora")
first_number = int(input("Primer número: "))
second_number = int(input("Segundo número: "))
print(first_number + second_number)



