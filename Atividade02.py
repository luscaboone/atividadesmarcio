### defina se o valor recebido pelo usuario é positivo, negativo ou nulo!
print("Vamos saber se o numero digitado é positivo, negativo ou nulo.")
numero = int(input("Digite um número: "))
if numero >0:
    print(f"O número {numero} é positivo")
if numero <0:
    print(f"O número {numero} é negativo")
if numero ==0:
    print(f"O número {numero} é nulo.")
    #em portugol esse codigo fica
    # imprima("Vamos saber se o numero digitado é positivo, negativo ou nulo")
    # numero = inteiro(entrada("Digite um número: "))
    # se numero >0:
    #   imprima(f"O número {numero} é positivo")
    # se numero <0:
    #   imprima(f"O número {numero} é negativo")
    # se numero ==0:
    #   imprima(f"O número {numero} é nulo")
###Questão 2! faça um algoritimo que leia um valor e imprima conforme a condição! No codigo mostrado abaixo, faço com que o usuario tenha que adivinhar um numero
###Digitando a entrada, conforme ele digita o numero, ele fica em um laco de repeticao ate que de a entrada do numero correto
import random
numero02 = int(random.randint(1,100))
#faco com o resultado da variavel seja um numero inteiro entre 1 e 100
while True:
#crio o laco de repeticao utilizando while
    n = int(input("Tente acertar o número: "))
    if n == numero02:
         print("Parabens voce acertou!")
         break
    elif n < numero02:
        print(f"O número correto é maior que {n}")
    else:
        print(f"O numero correto é menor que {n}")
#uso a funcao if, elfi e else para dar as condições conforme o resultado da entrada do usuario.
