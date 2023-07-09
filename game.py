import random
import os

class TicTacToe():
    def __init__(self):
        self.resetar_tabuleiro()
    
    def tabuleiro(self):
        print(' -=tabuleiro=- ')
        print('  ' + self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2])
        print('----------')
        print('  ' + self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2])
        print('----------')
        print('  ' + self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2])
    
    def analise_tabuleiro(self):
        dict_vencedor = {}
        
        #vencer horizontal
        for i in ['X', 'O']:
            dict_vencedor[i] = (self.board[0][0] == self.board[0][1] == self.board[0][1] == i)
            dict_vencedor[i] = (self.board[1][0] == self.board[0][1] == self.board[0][1] == i) or dict_vencedor[i]
            dict_vencedor[i] = (self.board[2][0] == self.board[0][1] == self.board[0][1] == i) or dict_vencedor[i]
            
        #vencer vertical
        for i in ['X', 'O']:
            dict_vencedor[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_vencedor[i]
            dict_vencedor[i] = (self.board[0][1] == self.board[1][1] == self.board[2][2] == i) or dict_vencedor[i]
            dict_vencedor[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_vencedor[i]
            
        #vencer diagonal
        for i in ['X', 'O']:
            dict_vencedor[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_vencedor[i]
            dict_vencedor[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_vencedor[i]
            
        if dict_vencedor['X']:
            self.done = 'X'
            print('X venceu!')
            return
        
        elif dict_vencedor['O']:
            self.done = 'O'
            print('O venceu!')
            return
        
        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != '':
                    c += 1
                    break
        
        if c == 0:
            self.done = 'd'
            print('Deu empate!')
            return    
    
    def jogador(self):
        movimento_invalido = True
        
        while movimento_invalido:
            try:
                print('Digite a linha do seu próximo lance:')
                x = int(input())
                
                print('Digite a coluna do seu próximo lance:')
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print('Coordenadas inválidas!')
                
                if self.board[x][y] != '':
                    print('Coordenadas já preenchidas!')
                    continue
                
            except Exception as e:
                print(e)
                continue
        
            movimento_invalido = False
        self.board[x][y] = 'X'
    
    def computador(self):
        lista_computador = []
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    lista_computador.append((i, j))

        if len(lista_computador) > 0:
            x, y = random.choice(lista_computador)
            self.board[x][y] = 'O'
    
    
    def resetar_tabuleiro(self):
        self.board = [['','',''], ['','',''], ['','','']]
        self.done = ''

tic_tac = TicTacToe()
tic_tac.tabuleiro()
jogar_tictac = 0

while jogar_tictac == 0:
    os.system('clear')
    tic_tac.tabuleiro()
    while tic_tac.done == '':
        tic_tac.jogador()
        tic_tac.computador()
        os.system('clear')
        tic_tac.tabuleiro()
        tic_tac.analise_tabuleiro()
    
    print('Digite 1 para sair do jogo, ou pressione qualquer tecla para continuar.')
    
    jogar_tictac = int(input())
    if jogar_tictac == 1:
        break
    else:
        tic_tac.resetar_tabuleiro()
        tic_tac = 0
        
    