from tratamento_palavra import Palavra_Tratada
palavra_tratada = Palavra_Tratada()

class Termo:
    def __init__(self):
        self._palavra_do_dia = palavra_tratada.tira_acentos()
        self.chute = []
        self.palavra_chutadas = []
        self.tentativas = 5
        self.acertou = False
        self.count = 0
        self.letras_acertadas = None
        self.posicao = 0
    
    def inicializa_palavra(self):
        return ["_" for letra in self._palavra_do_dia]

    def pede_chute(self):
        self.chute = str(input("Qual palavra deseja chutar? "))
        return self.chute.strip()

    def inicializa_palavra(self):
        return ["_" for letra in self._palavra_do_dia]
    
    def mostra_acerto(self):
        self.posicao = 0
        for i in self.chute:
            if (i==self._palavra_do_dia[self.posicao]):
                self.letras_acertadas[self.posicao] = i
            elif(len(self.chute) > len(self._palavra_do_dia) or len(self.chute) < len(self._palavra_do_dia)):
                return print("Digite uma palavra com a quantidade de letras igual a da palavra do dia!")
            self.posicao +=1
        return print(self.letras_acertadas)

    def termo(self):
        self.letras_acertadas = self.inicializa_palavra()
        print(self.letras_acertadas)
        while(not self.acertou):
            self.letras_acertadas = self.inicializa_palavra()
            self.chute = self.pede_chute()
            if(self.chute in self.palavra_chutadas):
                print(f'A palavra {self.chute} já foi chutada, escolha outra!')
            else:
                self.palavra_chutadas.append(self.chute)
                if(self.chute == self._palavra_do_dia):
                    self.imprime_mensagem_vencedor()
                    break
                else:
                    self.count = 0
                    self.mostra_acerto()
                    # for i in self.chute:
                    #     if i in self._palavra_do_dia:
                    #         self.mostra_palavra()
                    #     else:
                    #         self.count += 1
                    # if(self.count == len(self.chute)):
                    #     print('Além de errar a palavra nao acertou nenhuma letra!')
                    self.tentativas -= 1
                    if(self.tentativas == 1):
                        self.imprime_mensagem_perdedor()
                        break

    
    def imprime_mensagem_vencedor(self):
        print(f'Parabéns, você acertou a palavra {self._palavra_do_dia}')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    def imprime_mensagem_perdedor(self):
        print("Puxa, você errou a palavra do dia, volte amanhã!")
        print(f'A palavra era {self._palavra_do_dia}')
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
