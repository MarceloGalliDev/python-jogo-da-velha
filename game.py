import random
import os

class TicTacToe():
    def __init__(self):
        self.reset()
    
    def tabuleiro(self):
        print('')
        print('' + self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2])
        print('------')
        print('' + self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2])
        print('------')
        print('' + self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2])
    
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
    
    def jogador(self):
        pass
    
    def computador(self):
        pass
    
    
    def resetar_tabuleiro(self):
        self.board = [['','',''], ['','',''], ['','','']]
        self.done = ''

self = TicTacToe()
self.tabuleiro()