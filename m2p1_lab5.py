'''
classe: m2p1_lab5.py
descricao: Lista os titulos em mai�sculo dos org�os do Congresso.:
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 18 de setembro de 2018
'''

from  lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos()

for org in listJson.orgaos():
    id   = org['id']
    nome = org['nome']
    print(id,nome.upper())