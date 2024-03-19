#Exercicios de while

n1=1
while n1 <= 3:
    n2 = int(input("Digite um número: "))
    n3 = int(input("Digite outro número: "))
    soma = n2 + n3
    print(soma)
    n1 = n1+1
    
#Repetir um valor em while e imprimir se o número é par ou impar
numero = 1
while numero <= 3:
    par_ou_impar = int(input("Digite um número: "))
    if par_ou_impar%2 == 0:
        print(f"O número {par_ou_impar} é par.")
    else:
        print(f"O número {par_ou_impar} é impar.")
    numero = numero + 1
