#mostrar alo mundo na tela
print('Alo Mundo!')
#pedir para o usuario digitar um numero e entao imprimir na tela o numero digitado
numero = int(input('Digite um numero: '))
print("Seu numero digitado foi: ", numero)
#conta de soma basica
numero01 = int(input('Digite o Primeiro numero da soma: '))
numero02 = int(input('Agora digite o Segundo numero da soma: '))
soma = numero01 + numero02
print(f'A soma dos dois numeros digitados: {soma}')
#media das notas bimestrais
bimestre01 = int(input('Informe a sua nota no primeiro bimestre: '))
bimestre02 = int(input('Agora informe sua nota do segundo bimestre: '))
media = (bimestre01 + bimestre02)/2
print(f"Sua media nos bimestre foi de: {media}")
#classificaccaco das funcoes, int, string, float e tambem tem outros como lsits, tuples, dict, sets, bool, none e class.
string = 'ola mundo'
inteiro = int(50)
float = 3.75
print(f'{string} {type(string)} minha classificacao e: string.\n{inteiro} {type(inteiro)} minha classificacao e: int.\n{float} {type(float)} minha classificacao e: float')
# tabuada
n = int(input('Digite um numero para saber a tabuada: '))
print(f'A tabuada de {n} será: ')
for i in range (11): 
    print(f'{n}X{i}={n*i}')
#calculadora basica com implementacao da funcao while
primeironumero = int(input('digite um numero: '))
segundonumero = int(input('digite outro numero: '))
print(f"Seus números escolhidos foram: {primeironumero} e {segundonumero}, agora escolha o que deseja fazer com eles.")
soma2 = primeironumero + segundonumero
diferenca = primeironumero - segundonumero
multiplicacao = primeironumero * segundonumero
divisao = primeironumero / segundonumero
quociente = primeironumero // segundonumero
resto = primeironumero % segundonumero
expoente = primeironumero ** segundonumero
opcao = 0
while opcao == 0:
    opcao = int(input("Escolha uma opção: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Quociente\n6 - Resto\n7 - Expoente\nResposta: "))
    if opcao == 1:
        print(f"Resultado= {primeironumero}+{segundonumero}={soma2}")
    if opcao == 2:
        print(f"Resultado= {primeironumero}-{segundonumero}={diferenca}")
    if opcao == 3:
        print(f"Resultado= {primeironumero}*{segundonumero}={multiplicacao}")
    if opcao == 4:
        print(f"Resultado= {primeironumero}/{segundonumero}={divisao}")
    if opcao == 5:
        print(f"Resultado= {primeironumero}//{segundonumero}={quociente}")
    if opcao == 6:
        print(f"Resultado= {primeironumero}%{segundonumero}={resto}")
    if opcao == 7:
        print(f"Resultado= {primeironumero} Elevado a {segundonumero}={expoente}")
print("Fim!")
