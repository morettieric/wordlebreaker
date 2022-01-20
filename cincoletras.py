import os
os.system('cls' if os.name == 'nt' else 'clear')

print("ola mundo")
#sgb-words
with open("teste.txt","r") as arquivo:
	leitura = arquivo.read().split()
print (leitura[1])
print ("dbsize = ", len(leitura))
entrada = 'nada'

for i in range(len(leitura)):
    print(leitura[i])

while entrada != 'sair':
    posicao = input('digite a posicao\n')
    posint = int(posicao)
    caractere = input('digite o caractere\n')
    posicoes = []
    for x in range(len(leitura)):
        if leitura[x][posint] != caractere:
            posicoes.insert(0,x)
    print (posicoes,len(posicoes))
    
    for x in range(len(posicoes)):
        print(x,posicoes[x])
        remover = posicoes[x]
        leitura.pop(remover)
    print(leitura)
                                       
#for i in len(leitura)

print ("deu bom",entrada)
	
