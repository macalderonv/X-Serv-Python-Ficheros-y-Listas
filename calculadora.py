#Maria de los Ángeles Calderón Velasco
#!/usr/bin/python3

import sys

#print(sys.argv)
#print(sys.argv[1])
    
operador = sys.argv[2] 
if operador == '+':
    suma = int(sys.argv[1]) + int(sys.argv[3])
    print("El resultado de la suma " + str(sys.argv[1]) + " + " + str(sys.argv[3]) + " = " + str(suma))
elif operador == '-':
    resta = int(sys.argv[1]) - int(sys.argv[3])
    print("El resultado de la resta " + str(sys.argv[1]) + " - " + str(sys.argv[3]) + " = " + str(resta)) 
elif operador == '*':
   multiplicacion = int(sys.argv[1]) * int(sys.argv[3])
   print("El resultado de la multiplicacion " + str(sys.argv[1]) + " * " + str(sys.argv[3]) + " = " + str(multiplicacion)) 
elif operador == '/':
    try:
        division = int(sys.argv[1]) / int(sys.argv[3])
        print("El resultado de la division " + str(sys.argv[1]) + " / " + str(sys.argv[3]) + " = " + str(division)) 
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
else:
    print("operador erroneo")
            

