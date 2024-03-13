#   1. Formatar uma string com f-string:
#   Crie uma variável com o nome de uma pessoa.
#	Crie uma variável com a idade da pessoa.
#	Exiba a string formatada na tela.
nome = "Lucas"
idade = 20
print(f"Meu nome é: {nome} e minha idade é: {idade}!")

#   2. Explique o que é uma variável e qual sua função em um programa.
"""A variável é a declaração de um termo que nós atribuimos um valor a ela e sua função é armazenar o valor que nós queremos, podendo ser números e textos(str)."""

#   3. Marque abaixo os itens que representam declaração de variável em Python.
"""
(   ) String nome= “Pedro”
( x ) nome= “Pedro”
( x ) numero = 10
( x ) _numero= 10.5
(   )  print = “Olavo”
"""

#   4. Dê exemplo dos tipos de dados em Python abaixo:
"""
	Lógico = and,or e not

    Aritmético = (+) soma, (-) subtração, (/) divisão e (*) multiplicação.
"""

#   5.	Faça um Programa que peça dois números e imprima a soma.
numero = int(input("Digite um número: "))
segundonumero = int(input("Digite outro número: "))
soma = (numero + segundonumero)
print(f"A soma dos números {numero} + {segundonumero} = {soma}!")

#   6.	Crie um algoritmo que verifique se um número digitado pelo usuário é maior ou menor que 10.
terceironumero = int(input("Digite um número: "))
if numero > 10:
    print(f"O número {terceironumero} é maior que 10.")
elif numero < 10:
    print(f"O número {terceironumero} é menor que 10.")
else:
    print(f"O número {terceironumero} é igual a 10.")

#   7.	Crie um algoritmo que verifique se um numero é lido é par e maior que 10. 
#   Condições:
#	Deve ser usado o operador: “and”.
#	Utilize f string para formatar a saída de dados.
if terceironumero%2 == 0 and terceironumero >= 10:
    print(f"O número {terceironumero} é par e maior ou igual a 10!") 
elif terceironumero%2 == 0 and terceironumero <= 10:
    print(f"O numero {terceironumero} é par e menor ou igual a 10!")
else:
    print(f"O número {terceironumero} é impar!")
