import time 
def escalera ():
    n = int(input("Ingrese un numero entero: ")) #Se le pide al usuario el piso en el que se encuentra
    c = 0 #control del loop
    while c!= 1: #INICIO DEL LOOP
        print(f"Estas en el piso {n}, te faltan 20 escalones para llegar al piso {n-1}") #Muestra en pantalla el mensaje en que piso se encuentra
        print(".")
        time.sleep(0.5)
        print(".")
        n = n -1 #Operacion aritmetica para restar una unidad a la variable n
        if n == 1:
            c = 1
            print(f">> Felicidades llegaste al piso {n} ya puedes salir del edificio <<\n") #Imprime el mesnje cuando ya esta en el piso
escalera()
