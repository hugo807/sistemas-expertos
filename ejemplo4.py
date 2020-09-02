# calculadora con opciones aritmeticas


while 1:
    x= float(input("ingresa el primer numero"))
    y= float(input("ingresa el segundo numero"))

    print("selecciona la opcion que desees realizar")
    print("1 suma")
    print("2 resta")
    print("3 multiplicacion")
    print("4 divicion")

    n = int(input("¿cual opcion quieres? "))
    if n==1:
        resultado= x+y
        print(resultado)
    elif n==2:
        resultado= x-y
        print(resultado)
    elif n==3:
        resultado= x*y
        print(resultado)
    elif n==4 and y!=0:
        resultado= x/y
        print(resultado)