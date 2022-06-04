import numpy as np

class Forca:
    def __init__(self):
        self._palavra_secreta = None
        self.chute = None
        self.enforcou = False
        self.acertou = False 
        self.letras_acertadas = None
        self.tentativas = 0
        self.index = 0
        self.count = 0
        self.local = 0
        self.reader = None
        self.palavra = None
        self.letras_chutadas = []

    def busca_palavra(self):
        with open('/home/rhuan/EstudoPython/Alura/palavras.csv', 'r') as arquivo:
            self.reader = np.array(arquivo.readline().split(","))
            self.palavra = np.random.choice(self.reader)
        return self.palavra

    def verifica_palavra(self):
        self._palavra_secreta = self.busca_palavra()
        self.letras_acertadas = self.inicializa_letras_acertadas()
        self.count = len(self._palavra_secreta)
        self.forca()

    def inicializa_letras_acertadas(self):
        return ["_" for letra in self._palavra_secreta]

    def pede_chute(self):
        self.chute = str(input("Qual letra deseja chutar? "))
        return self.chute.strip()

    def acertar(self):
        print(f'A palavra era: {self.letras_acertadas}')
        return True

    def forca(self):
        while (not self.enforcou and not self.acertou):
            print(self.letras_acertadas)
            self.chute = self.pede_chute()
            if(self.chute in self.letras_chutadas):
                print(f'A letra {self.chute} já foi chutado, escolha outra!')
            else:
                self.letras_chutadas.append(self.chute)
                self.local = 0
                for i in self._palavra_secreta:
                    if (self.chute.upper() == i.upper()):
                        self.letras_acertadas[self.local] = i
                        self.count -= 1
                    self.local += 1
                    self.index += 1
                    if (self.count == 0):
                        self.imprime_mensagem_vencedor()
                        self.acertou = self.acertar()

                if (self._palavra_secreta.find(self.chute) == -1):
                    if (self.tentativas < 7):
                        print(f'A letra {self.chute.lower()} nao existe na palavra, voce ainda tem {7 - self.tentativas} tentativas')
                    if (self.tentativas == 7):
                        self.imprime_mensagem_perdedor()
                        enforcou = True
                        return enforcou
                    self.desenha_forca()
                    self.tentativas += 1

    def imprime_mensagem_perdedor(self):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(self._palavra_secreta))
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

    def imprime_mensagem_vencedor(self):
        print("Parabéns, você ganhou!")
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

    def desenha_forca(self):
        print("  _______     ")
        print(" |/      |    ")

        if(self.tentativas == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(self.tentativas == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(self.tentativas == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(self.tentativas == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(self.tentativas == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(self.tentativas == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (self.tentativas == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()
