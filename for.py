
#exemplo
x=0
for x in range(5):
    print("ola")
    
#segundo exemplo
times = ["flamengo", "corinthians", "palmeiras"]
for x in times:
    print(x)

#breve explicação, o for é como se fosse um while porém ele é determinado, não ha a necessidade de criar um esquema para dar um fim a ele pois a própria função ja possuí um desfecho


# exemplo de um laço em for
n1 = 1
for n1 in range(5):
    print("teste em for")

# exemplo do mesmo codigo em while
n2 = 1
while n2 <= 5:
    print("teste em while")
    n2 = n2+1
    # ENQUANTO O FOR REPETE A FUNCAO PARA UM ETERMINADO NUMERO, O WHILE REPETE ESSA FUNCAO POREM PRECISAMOS DEFINIR COM UMA LOGICA QUANDO ESSA FUNCAO IRA FINALIZAR.

tabuada = int(input("Digite um número: "))
for x in range (1,11,2): #(inicio,final,casas)
    soma = (x*tabuada)
    print(f"{tabuada}x{x}={soma}")
