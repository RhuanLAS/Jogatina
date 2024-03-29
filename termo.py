from tratamento_palavra import Palavra_Tratada
palavra_tratada = Palavra_Tratada()

class Termo:
    def __init__(self):
        self._palavra_do_dia = palavra_tratada.busca_palavra()
        self.chute = []
        self.palavra_chutadas = []
        self.tentativas = 6
        self.acertou = False
        self.letras_acertadas = []
        self.posicao = None
        
    def inicializa_palavra(self):
        return ["_" for letra in self._palavra_do_dia[2:7]]

    def pede_chute(self):
        self.chute = str(input("Qual palavra deseja chutar? "))
        return self.chute.strip()
    
    def print_colorido(self):
        self.posicao = 0
        self.letras_acertadas = []
        for i in self.chute:
            if(len(self.chute) > len(self._palavra_do_dia[2:7]) or len(self.chute) < len(self._palavra_do_dia[2:7])):
                return print("Digite uma palavra com a quantidade de letras igual a da palavra do dia!")
            elif(i==self._palavra_do_dia[self.posicao+2]):
                self.letras_acertadas.append(i)
                print(self.colored(0, 255, 0, i), end=' ')
            elif(i in self._palavra_do_dia[2:7] and i not in self.letras_acertadas):
                self.letras_acertadas.append(i)
                print(self.colored(255, 255, 0, i), end=' ')
            elif(i not in self._palavra_do_dia[2:7]):
                print(self.colored(255, 0, 0, i), end=' ')
            self.posicao += 1
        print()

    def colored(self,r, g, b, text):
        return f'\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m'

    def termo(self):
        print(self.inicializa_palavra())
        while(not self.acertou):
            self.chute = self.pede_chute()
            if(palavra_tratada.confere_chute(self.chute) == False):
                print(f'A palavra {self.chute} não é aceita')
            elif(self.chute in self.palavra_chutadas):
                print(f'A palavra {self.chute} já foi chutada, escolha outra!')
            else:
                self.palavra_chutadas.append(self.chute)
                if(self.chute == self._palavra_do_dia[2:7]):
                    self.imprime_mensagem_vencedor()
                    break
                else:
                    self.print_colorido()
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

