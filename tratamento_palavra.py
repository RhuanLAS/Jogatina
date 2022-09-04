import re
import unicodedata
from random import sample
import pandas as pd
from pathlib import Path
import csv

class Palavra_Tratada:
    def __init__(self):
        self._texto = self.busca_palavra()

    def busca_palavra(self):
        self.csv = pd.read_csv(Path(__file__).parent / "palavras_modificadas.csv")   
        self.reader = []
        for i in self.csv['Palavras']:
            self.reader.append(i)
        return str(sample(self.reader, 1))

        # with open(Path(__file__).parent / "palavras_modificadas.csv", 'r') as arquivo:
        #     self.reader = np.array(arquivo.readline().split("\n"))
        #     self.palavra = np.random.choice(self.reader)
        # return self.palavra

    # def tira_acentos(self):
    #     try:
    #         self._texto = unicode(self._texto, 'utf-8')
    #     except (TypeError, NameError): # unicode is a default on python 3 
    #         pass
    #     self._texto = unicodedata.normalize('NFD', self._texto)
    #     self._texto = self._texto.encode('ascii', 'ignore')
    #     self._texto = self._texto.decode("utf-8")
    #     return str(self._texto)

    # def texto(self):
    #     self._texto = self.tira_acentos(self._texto.lower())
    #     self._texto = re.sub('[ ]+', '_', self._texto)
    #     self._texto = re.sub('[^0-9a-zA-Z_-]', '', self._texto)
    #     return self._texto

    def confere_chute(self, palavra):
        self.my_content = pd.read_csv(Path(__file__).parent / "palavras_modificadas.csv")
        self.palavras = []
        for row in self.my_content['Palavras']:
            self.palavras.append(row)
        return True if palavra in self.palavras else False

        # with open(Path(__file__).parent / "palavras_modificadas.csv", 'r') as arquivo:
        #     my_content = csv.reader(arquivo, delimiter='\n')
        #     for row in my_content:
        #         return True if palavra in row else False