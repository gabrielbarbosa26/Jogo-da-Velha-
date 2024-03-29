#Jogo da Velha: feito por Gabriel
tabuleiro = [['_','_','_'],['_','_','_'],['_','_','_']]
historicoTab = []
ganhadores = []
ganhar = False
jogador1 = "X"
jogador2 = "O"



'''Funções'''
def escolherOpcaoEOrientar():
    print()
    print('1 - Jogar ')
    print()
    print('2 - Instruções')
    print()
    print("3 - Encerrar")
    print()
    opcao = int(input("Digite sua opção: "))

    while opcao != 3:
        if opcao == 1:
            limparTabuleiro()
            jogar()
            
        
        if opcao == 2:
            print("Participam duas pessoas, que jogam alternadamente, preenchendo cada um dos espaços vazios. Cada participante deve usar um símbolo (X ou O). Vence o jogador que conseguir formar primeiro uma linha com três símbolos iguais, seja ela na horizontal, vertical ou diagonal.")


        if opcao ==  3:
          print("Fim do jogo!")


        print()
        print('1 - Jogar ')
        print()
        print('2 - Instruções')
        print()
        print("3 - Encerrar")
        print()
        opcao = int(input("Digite sua opção: "))



def jogar():
    
    while(True):
        mostrarTabuleiro()
        inserirLinhaColuna(jogador1)

        if(checarSeGanhou(jogador1) == True):
            break
            
        mostrarTabuleiro()
        inserirLinhaColuna(jogador2)

        if(checarSeGanhou(jogador2) == True):
            break



def mostrarTabuleiro():
    print('-------------------------Jogo da velha-------------------------')
    for i in range(0,3):
        print()
        print('                         ',
              tabuleiro[i][0],'|', tabuleiro[i][1],'|', tabuleiro[i][2])
    print()



def inserirLinhaColuna(jogador):
    linha1 = int(input('Jogador '+ jogador+' | Digite a linha: '))
    coluna1 = int (input('Jogador '+ jogador+' | Digite a coluna: '))
    print()

    tabuleiro[linha1 - 1][coluna1 - 1] = jogador



def limparTabuleiro():
    for i in range(0,3):
        for j in range(0,3):
            tabuleiro[i][j] = '_'


def checarSeGanhou(jogador):
    velha = darVelha()
    linha =ganharEmLinha()
    coluna = ganharEmColuna()
    diagonal = ganharEmDiagonal()

    if(velha == True or linha == True or coluna == True or diagonal == True):
        mostrarTabuleiro()
        historicoTab.append(tabuleiro)
        return True

        

def ganharEmLinha():
    for a in range (0,3):
        if tabuleiro[a][0] == 'X' and tabuleiro[a][1] == 'X' and tabuleiro[a][2] == 'X':
            print('Jogador 1 Ganhou!')
            ganhadores.append("jogador 1 ganhou!")
            return True
            
        if tabuleiro[a][0] == 'O' and tabuleiro[a][1] == 'O' and tabuleiro[a][2]== 'O':
            print('Jogador 2 Ganhou!')
            ganhadores.append("jogador 2 ganhou!")
            return True
        
    return False



def ganharEmColuna():
    for k in range (0,3):
        if tabuleiro[0][k] == 'X' and tabuleiro[1][k] == 'X' and tabuleiro[2][k] == 'X' :
            print('Jogador 1 Ganhou!')
            ganhadores.append("jogador 1 ganhou!")
            return True
                  
        if tabuleiro[0][k] == 'O' and tabuleiro[1][k] == 'O' and tabuleiro[2][k] == 'O' :
            print('Jogador 2 Ganhou!')
            ganhadores.append("jogador 2 ganhou!")            
            return True
    return False



def ganharEmDiagonal():
    if tabuleiro[0][0]== 'X' and tabuleiro[1][1]== 'X' and tabuleiro[2][2] == 'X':
        print ('Jogador 1 Ganhou!')
        ganhadores.append("jogador 1 ganhou!")
        return True
          
    if tabuleiro[0][2]== 'X' and tabuleiro[1][1]== 'X' and tabuleiro[2][0] == 'X':
        print ('Jogador 1 Ganhou!')
        ganhadores.append("jogador 1 ganhou!")
        return True
                  
    if tabuleiro[0][0]== 'O' and tabuleiro[1][1]== 'O' and tabuleiro[2][2] == "O":
        print ('Jogador 2 Ganhou!')
        ganhadores.append("jogador 2 ganhou!")
        return True
          
    if tabuleiro[0][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][0] == 'O':
        print('Jogador 2 Ganhou!')
        ganhadores.append("jogador 2 ganhou!")
        return True

    return False



def darVelha():
    if (tabuleiro[0][0] != '_' and tabuleiro[0][1] != '_'and tabuleiro[0][2] != '_'):
        if(tabuleiro[1][0] != '_' and tabuleiro[1][1] != '_' and tabuleiro[1][2] != '_'):
            if (tabuleiro[2][0] != '_' and tabuleiro[2][1] != '_' and tabuleiro[2][2] != '_'):
                if (ganharEmLinha() == False and ganharEmColuna() == False and ganharEmDiagonal() == False):
                    print ("# Deu velha #")
                    ganhadores.append("Velha")
                    return True
    return False



escolherOpcaoEOrientar()
