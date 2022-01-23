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
        
def salvar_amarela(pos, letra):
    posicoes = []
    for x in range(len(leitura)):
        contem = 0
        for i in range(0,5):
            if leitura[x][i] == letra:
                contem = contem+1
        if contem == 0:
            posicoes.insert(0,x)
            
    for x in range(len(posicoes)):
        remover = posicoes[x]
        leitura.pop(remover)

    posicoes = []
    for x in range(len(leitura)):
        if leitura[x][pos] == letra:
            posicoes.insert(0,x)
    
    for x in range(len(posicoes)):
        remover = posicoes[x]
        leitura.pop(remover)
    
        
'''        
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
verdes = []
while entrada != 'sair':    
    entrada = input('Digite o comando: am [pos] [letra] / vd [pos] [letra] / pt [letra] / im: ')
    if entrada != '':
        entrada_limpa = entrada.split()
        
        if entrada_limpa[0] == 'am':
            #amarelo
            if len(entrada_limpa) == 3:
                salvar_amarela(int(entrada_limpa[1])-1,entrada_limpa[2])
                print('Palavras filtradas: ',len(leitura),'. Primeira palavra: ',leitura[0],'.')
            else:
                print('Entrada Inválida, digite novamente')

        elif entrada_limpa[0] == 'vd':
            #verde
            if len(entrada_limpa) == 3:
                salvar_verde(int(entrada_limpa[1])-1,entrada_limpa[2])
                verdes.insert(0,entrada_limpa[2])
                print('Palavras filtradas: ',len(leitura),'. Primeira palavra: ',leitura[0],'.')
            else:
                print('Entrada Inválida, digite novamente')

        elif entrada_limpa[0] == 'pt':
            #preto
            if len(entrada_limpa)>1:
                if (entrada_limpa[1] in verdes):
                    print ('Erro, entrada já existente na verde')
                else:
                    remover_pretas(entrada_limpa[1])
                    print('Palavras filtradas: ',len(leitura),'. Primeira palavra: ',leitura[0],'.')
            else:
                print('Entrada Inválida, digite novamente')

        elif entrada_limpa[0] == 'im':
            imprimirdb()
        elif entrada_limpa[0] == 'rs':
            with open("sgb-words.txt","r") as arquivo:
                leitura = arquivo.read().split()
            print ("dbsize = ", len(leitura))
            verdes = []
            

        else:
            print ('Entrada Inválida, tente novamente.')
    else:
        print('Entrava vzia, tente novamente')

'''