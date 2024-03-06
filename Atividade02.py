'''### defina se o valor recebido pelo usuario é positivo, negativo ou nulo!
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
#terceira atividade
#Construa um algoritmo que receba como entrada três valores e os imprima em ordem crescente. 
print("Vamos contar valores em ordem crescente e decrescente!\nObs. Os números escolhidos tem que ser diferentes.")
n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))
n3 = float(input("Digite outro valor: "))
# pedir a entrada de dados do usuario de forma aleatoria
valores = [n1,n2,n3]
#definir uma lista
valores.sort()
valores_descrescentes = sorted(valores, reverse=True)
#usar a opção .sort() para definir os valores da variavel em ordem crescente.
print(f"Os valores digitados em ordem crescente são: {valores} e os valores em ordem descrescente são: {valores_descrescentes}")
#imprimir o resultado na tela dos valores em ordem crescente.
print(f" {50*"-"}Fim{50*"-"}")
#atividade 4 = Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a 
#variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados
a = int(input("digite o valor de A: "))
b = int(input("digite o valor de B: "))
print(f"O valor de A={a} e o valor de B={b}")
#o usuario faz a entrada dos valores e é mostrado o valor digitado na tela
c = a
a = b
b = c
# é criada uma nova variável(c) para abrigar o valor de outra variavel para fazer um ciclo e inverter os resultados. 
print(f"Após inverter, o valor de A={a} e o valor de B={b}")'''
