import random

class Adivinhacao:
    def __init__(self):
        self.escolha = None
        self._n1 = int(random.randrange(1, 100))
        self.pontos = 20
        self.numero_tentativas = None
        self.count = 0
        self.chute = None

    def jogar_adivinhacao(self):
        while (True):
            self.escolha = int(input("Qual dificuldade voce vai querer? 1 facil 2 medio 3 dificil: "))
            
            if (self.escolha == 1):
                self.numero_tentativas = 20
                break
            elif (self.escolha == 2):
                self.numero_tentativas = 10
                break
            elif (self.escolha == 3):
                self.numero_tentativas = 5
                break
            else:
                print("Escolha uma alternativa válida!")

        while (self.numero_tentativas > 0):
            self.count += 1
            self.chute = int(input("Digite seu número: "))
            print(f'Voce digitou {self.chute}')

            if (self.chute == self._n1):
                self.pontos = self.pontos - self.count
                print(f'Parabéns, você acertou e fez {self.pontos} pontos!')
                break

            elif (self.chute < self._n1):
                print(f'O número {self.chute} está abaixo do número sorteado')
            else:
                print(f'O número {self.chute} está acima do número sorteado')
            self.numero_tentativas -= 1

            if (self.numero_tentativas == 0):
                print("Voce zerou as tentativas, perdeu o jogo!")