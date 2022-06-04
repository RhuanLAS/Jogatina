import re
import unicodedata
import numpy as np

class Palavra_Tratada:
    def __init__(self):
        self._texto = self.busca_palavra()

    def busca_palavra(self):
        with open('/home/rhuan/EstudoPython/Alura/palavras.csv', 'r') as arquivo:
            self.reader = np.array(arquivo.readline().split(","))
            self.palavra = np.random.choice(self.reader)
        return self.palavra

    def tira_acentos(self):
        try:
            self._texto = unicode(self._texto, 'utf-8')
        except (TypeError, NameError): # unicode is a default on python 3 
            pass
        self._texto = unicodedata.normalize('NFD', self._texto)
        self._texto = self._texto.encode('ascii', 'ignore')
        self._texto = self._texto.decode("utf-8")
        return str(self._texto)

    def texto(self):
        self._texto = self.tira_acentos(self._texto.lower())
        self._texto = re.sub('[ ]+', '_', self._texto)
        self._texto = re.sub('[^0-9a-zA-Z_-]', '', self._texto)
        return self._texto
