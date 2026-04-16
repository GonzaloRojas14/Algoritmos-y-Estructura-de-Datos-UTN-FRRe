
while True:
    a=int(input("Ingrese el valor de a "))
    b=int(input("Ingrese el valor de b "))
    c=int(input("Ingrese el valor de c "))
    if (a>b and b>c):
        print(" caso 1 el mayor es",a," el del medio ",b,"y el menor " ,c)# a b c
    elif (a>c and c>b):
        print(" caso 2 el mayor es ",a,"el del medio ",c," y el menor ",b)# a c b
    elif (b>a and a>c):
        print("caso 3 el mayor es ",b,"el del medio ",a," y el menor ",c)# b a c
    elif (b>c and c>a):
        print("caso 4 el mayor es ",b,"el del medio ",c," y el menor ",a)#b c a
    elif (c>a and a>b):
        print("caso 5 el mayor es ",c,"el del medio ",a," y el menor ",b)#c a b
    else:#a=1 b=2 c=3
        print("caso 6 el mayor es ",c,"el del medio ",b," y el menor ",a)#c b a
    print()

