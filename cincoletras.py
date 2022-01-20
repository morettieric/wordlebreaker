def imprimirdb():
    print(leitura[1],leitura[2],leitura[3])
    print('DB: ',len(leitura),'. Deseja imprimir?')
    
    quero = input()
    if quero == 's':
        x=0
        while quero == 's':
            for i in range (0,10):
                if (i+x) > len(leitura):
                    break
                print (leitura[i+x])
            x=x+10
            print ('Deseja imprimir mais?',x,'/',len(leitura))
            quero = input ()

        
#sgb-words
with open("sgb-words.txt","r") as arquivo:
	leitura = arquivo.read().split()
print ("dbsize = ", len(leitura))
entrada = 'nada'

while entrada != 'sair':
    entrada = input('Digite a posição ou a letra a ser bloqueada\n')
    try:
        posicao = int(entrada)
        if posicao >= 0 and posicao<= 4:
            caractere = input('digite o caractere\n')
            posicoes = []
            for x in range(len(leitura)):
                if leitura[x][posicao] != caractere:
                    posicoes.insert(0,x)
        
            for x in range(len(posicoes)):
                remover = posicoes[x]
                leitura.pop(remover)
            imprimirdb()
    except ValueError:  
        posicoes = []
        for x in range(len(leitura)):
            for i in range(0,5):
                if leitura[x][i] == entrada:
                    posicoes.insert(0,x)
                    break
        #print (posicoes)
    
        for x in range(len(posicoes)):
            #print(x,posicoes[x])
            remover = posicoes[x]
            leitura.pop(remover)
        imprimirdb()

