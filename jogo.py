#Paranaues importantes
import os
import time
#comentario bug
#Variaveis globais
empate = 0
Novo_Jogo = 0
x = 0
end_game = 0

l1 = '     |     |     '
l2 = '  t  |  i  |  c  '
l3 = '_____|_____|_____'
l4 = '     |     |     '
l5 = '  t  |  a  |  c  '
l6 = '_____|_____|_____'
l7 = '     |     |     '
l8 = '  t  |  o  |  e  '
l9 = '     |     |     '

L1 = [x for x in l1]
L2 = [x for x in l2]
L3 = [x for x in l3]
L4 = [x for x in l4]
L5 = [x for x in l5]
L6 = [x for x in l6]
L7 = [x for x in l7]
L8 = [x for x in l8]
L9 = [x for x in l9]

T=[L1,L2,L3,L4,L5,L6,L7,L8,L9]

# Fun__es:

#fun__o para converter cada linha em string, antes de printar
def tabuleiro (T):
    os.system('clear')
    for linha in T:
        lt = ''
        for esp in linha:
            lt = lt + str(esp)
        print lt


#fun__o para testar vit_ria/empate
def verifica (T):
    global empate
    global end_game
    empate += 1


    #horizontal, mant_m linha, confere coluna
    vic = [True,True,True]
    a = ['']*3
    count = 0
    for l in [1,4,7]:
        for c in [2,8,14]:
            if count <= 3:
                a[count] = T[l][c]
                count += 1
                if map(lambda z: z== 'O', a) == vic:
                    print 'Jogador O ganhou!'
                    count = 0
                    a = ['']*3
                    empate = 0
                    end_game = 1
                elif map(lambda z: z== 'X', a) == vic:
                    print 'Jogador X ganhou!'
                    count = 0
                    a = ['']*3
                    empate = 0
                    end_game = 1
                elif count == 3:
                    count = 0
                    a = ['']*3

    #vertical, mant_m coluna, confere linha
    b = ['']*3
    count2 = 0
    for c in [2,8,14]:
        for l in [1,4,7]:
            if count2 <= 3:
                b[count2] = T[l][c]
                count2 += 1
                if map(lambda z: z== 'O', b) == vic:
                    print 'Jogador O ganhou!'
                    count2 = 0
                    b = ['']*3
                    empate = 0
                    end_game = 1
                elif map(lambda z: z== 'X', b) == vic:
                    print 'Jogador X ganhou!'
                    count2 = 0
                    b = ['']*3
                    empate = 0
                    end_game = 1
                elif count2 == 3:
                    count2 = 0
                    b = ['']*3

    #Diagonal principal, linha e coluna tem o mesmo valor no jogo, mas n_o no programa.
    e = ['']*3
    count3 = 0
    for lc in [[1,2],[4,8],[7,14]]:
        if count3 <= 3:
            e[count3] = T[lc[0]][lc[1]]
            count3 += 1
            if map(lambda z: z== 'O', e) == vic:
                print 'Jogador O ganhou!'
                count3 = 0
                e = ['']*3
                empate = 0
                end_game = 1
            elif map(lambda z: z== 'X', e) == vic:
                print 'Jogador X ganhou!'
                count3 = 0
                e = ['']*3
                empate = 0
                end_game = 1
            elif count3 == 3:
                count3 = 0
                e = ['']*3


    #Diagonal secund_ria, linha e coluna n_o tem o mesmo valor no jogo, nem no programa.
    f = ['']*3
    count4 = 0
    for lc in [[1,14],[4,8],[7,2]]:
        if count4 <= 3:
            f[count4] = T[lc[0]][lc[1]]
            count4 += 1
            if map(lambda z: z== 'O', f) == vic:
                print 'Jogador O ganhou!'
                count4 = 0
                f = ['']*3
                empate = 0
                end_game = 1
            elif map(lambda z: z== 'X', f) == vic:
                print 'Jogador X ganhou!'
                count4 = 0
                f = ['']*3
                empate = 0
                end_game = 1
            elif count4 == 3:
                count4 = 0
                f = ['']*3

    #EMPATE, todas as casas preenchidas sem vit_ria
    if empate == 9:
            print 'JOGO EMPATADO'
            end_game = 1



def jogadas(xis):
    global x
    jogador = ['BOLA','XIS']
    M=[[2,8,14],[1,4,7]]
    s = ['Linha','Coluna']
    ajuste = []
    free_position = 0
    print 'Vez de %s \n' %(jogador[x])

    while free_position == 0:
        for a in range(0,2):
            w = 0
            while w == 0:
		while True:
			try:
				input_lc = int(raw_input('Digite o numero da %s _1_2_3\n'  %(s[a].lower())))
				break
			except ValueError:
				print 'Escolha invalida, digite um numero de 1 a 3'
				time.sleep(1)
				tabuleiro(T)
                if input_lc == 1:

		    teste = 1
                    if teste == 1: #teste de linha/coluna cheia
                        d=[' ']*3
                        d1 = 0
                        for teste2 in M[a]:
			    if a == 0:
				d[d1] = T[1][teste2]
                                d1 += 1
                            elif a==1:
                                d[d1] = T[teste2][2]
                                d1 += 1
                        if map(lambda a: a != ' ', d) == [True, True, True]:
                            print '%s cheia, digite novamente\n' %(s[a])
                            time.sleep(2)
                            tabuleiro(T)
                            teste = 0
                        else:
                            if a == 0:
                                l = 1
                                w = 1
                            elif a == 1:
                                c = 2
                                w = 1

                elif input_lc == 2:
                    teste = 1
                    if teste == 1: #teste de linha/coluna cheia
                        d=[' ']*3
                        d1 = 0
                        for teste2 in M[a]:
                            if a == 0:
                                d[d1] = T[4][teste2]
                                d1 += 1
                            elif a==1:
                                d[d1] = T[teste2][8]
                                d1 += 1
                        if map(lambda a: a != ' ', d) == [True, True, True]:
                            print '%s cheia, digite novamente\n' %(s[a])
                            time.sleep(2)
                            tabuleiro(T)
                            teste = 0
                        else:
                            if a == 0:
                                l = 4
                                w = 1
                            elif a == 1:
                                c = 8
                                w = 1


                elif input_lc == 3:
                    teste = 1
                    if teste == 1: #teste de linha/coluna cheia
                        d=[' ']*3
                        d1 = 0
                        for teste2 in M[a]:
                            if a == 0:
                                d[d1] = T[7][teste2]
                                d1 += 1
                            elif a==1:
                                d[d1] = T[teste2][14]
                                d1 += 1
                        if map(lambda a: a != ' ', d) == [True, True, True]:
                            print '%s cheia, digite novamente\n' %(s[a])
                            time.sleep(2)
                            tabuleiro(T)
                            teste = 0
                        else:
                            if a == 0:
                                l = 7
                                w = 1
                            elif a == 1:
                                c = 14
                                w = 1

                else:
                    print 'Jogada Invalida'
                    w = 0

        if T[l][c] == ' ':
            if x == 0:
                T[l][c] = 'O'
                tabuleiro(T)
                free_position = 1
                x = 1
            elif x == 1:
                T[l][c] = 'X'
                tabuleiro(T)
                free_position = 1
                x = 0
        else:
            print 'Local ocupado'
            time.sleep(2)
            tabuleiro(T)
            free_position = 0




#Inicio de jogo:
#Apresenta_o
inicio = 0
sp = ['',' ']*5
while inicio <= 9:
    print '%sBem vindo ao tic tac toe' %(sp[inicio])
    inicio += 1
    time.sleep(.15)
    os.system('clear')
tabuleiro(T)


sacanagem =1
while sacanagem == 1:
        global x
        print 'Deseja iniciar um novo jogo?\n'
        NG = str(raw_input('S/N\n')).lower()
        if NG == 's':
	    for limpa in [1,4,7]:
		for limpa2 in [2,8,14]:
			T[limpa][limpa2] = ' '
	    os.system('clear')
	    tabuleiro(T)
            sacanagem2 = 1
            while sacanagem2 == 1:
                player = str(raw_input('Qual jogador vai iniciar? X ou O\n')).lower()

		if player == 'x':
                    x = 1
                    sacanagem2 = 0
		    end_game = 0
                elif player == 'o':
                    x = 0
                    sacanagem2 = 0
		    end_game = 0
                else:
                    sacanagem2=1
                    print'Escolha invAlida. X ou O\n'
                    tabuleiro(T)

        elif NG == 'n':
            print 'Good Bye!!'
            end_game = 1
	    sacanagem = 0

        else:
            print 'Escolha invAlida.\n'
            sacanagem ==1
            tabuleiro(T)

        while end_game == 0:
            jogadas(x)
            verifica(T)
            time.sleep(1)
            sacanagem = 1
