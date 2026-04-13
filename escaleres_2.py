import time 
def esc(n):
    if n == 1:
        print("Felicidades ya llegaste al piso 1") #Imprime el mensaje caundo ya esta en el piso 1
        
    else:
        print(f"Estas en el piso {n} te faltan 15 escalones para llegar al piso {n-1}") #Mensaje que muestra en que piso esta el usaurio y cuanto le falta para llegar al piso que esta por debajo de este
        print(".")
        esc(n-1) #Condicion recursiva que vuelve a llamar a la funcion misma hasta que el usuario llegue al piso 1
        time.sleep(0.5)
        
        
esc(5) #Asignar un valor a n
