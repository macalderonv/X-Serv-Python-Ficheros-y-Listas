#Maria de los Ángeles Calderón Velasco
#!/usr/bin/python3

#Tabla del 1

#Tabla del 2
#...
#10 por 10 100

for numero1 in range(1,11):
    print('\nTabla del', numero1)
    for numero2 in range(1,11):
        multiplicacion = numero1 * numero2
  
        print(str(numero1) + '*' + str(numero2) + ' = ' + str(multiplicacion))
