#fazer a lista de caracteres banidos para ver se n da bosta


def imprimirdb():
    print(leitura[0])
    print('DB: ',len(leitura),'. Deseja imprimir?')
    
    quero = input()
    if quero == 's':
        if len(leitura)<10:
            print (leitura)
        else:
            x=0
            while quero == 's':
                for i in range (0,10):
                    if (i+x) > len(leitura):
                        break
                    print (leitura[i+x])
                x=x+10
                print ('Deseja imprimir mais?',x,'/',len(leitura))
                quero = input ()


def remover_pretas(letra):
    posicoes = []
    for x in range(len(leitura)):
        for i in range(0,5):
            if leitura[x][i] == letra:
                posicoes.insert(0,x)
                break
            
    for x in range(len(posicoes)):
        remover = posicoes[x]
        leitura.pop(remover)

                   
def salvar_verde(pos,letra):
    posicoes = []
    for x in range(len(leitura)):
        if leitura[x][pos] != letra:
            posicoes.insert(0,x)
    
    for x in range(len(posicoes)):
        remover = posicoes[x]
        leitura.pop(remover)
        
#def salvar_amarela(letra)
        
#sgb-words
with open("sgb-words.txt","r") as arquivo:
	leitura = arquivo.read().split()
print ("dbsize = ", len(leitura))
entrada = 'nada'
"""
Entradas:

am v
vd 3 a
pt l
"""
while entrada != 'sair':    
    entrada = input('Digite o comando: am [letra] / vd [pos] [letra] / pt [letra] \n')
    entrada_limpa = entrada.split()
    if entrada_limpa[0] == 'am':
        #amarelo
        print('amarelow')
    elif entrada_limpa[0] == 'vd':
        #verde
        salvar_verde(entrada_limpa[1],entrada_limpa[2])
        imprimirdb()
    elif entrada_limpa[0] == 'pt':
        #preto
        remover_pretas(entrada_limpa[1])
        imprimirdb()
    else:
        print ('Entrada Inválida, tente novamente.\n')
    """
    try:
            posicao = int(entrada)
            if posicao >= 0 and posicao<= 4:
                caractere = input('digite o caractere\n')
                salvar_verde(posicao,caractere)
                
                imprimirdb()
    except ValueError:
            remover_pretas(entrada)            
            imprimirdb()
    else:
        entrada.split()
        
"""
