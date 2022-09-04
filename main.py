from adivinha_numero import Adivinhacao
from jogar_forca import Forca
from termo import Termo

adivinha = Adivinhacao()
forca = Forca()
jogo_termo = Termo()
def main(): 
    while(True):
        jogo = int(input("QUAL JOGO DESEJA JOGAR? 1 Forca 2 Adivinhacao 3 Termo paraguaio: "))
        if (jogo == 1):
            print("Voce vai jogar o jogo da Forca!")
            forca.verifica_palavra()    
            break
        elif (jogo == 2):
            print("Voce vai jogar o jogo da Adivinhacao!")
            adivinha.jogar_adivinhacao()
            break
        elif (jogo == 3):
            print("Voce vai jogar o Termo paraguaio")
            jogo_termo.termo()
            break
        else:
            print("Jogo inválido, escolha uma alternativa válida!")

if __name__ == '__main__':
    main()
