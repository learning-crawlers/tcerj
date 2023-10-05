#######################################
##  TCERJ Contas Irregulares
##    Busca de contas irregulares no TCERJ com Número de Processo, Nome, CPF e Data do Trânsito em Julgado
##
##    Author: Alex Benincasa Santos 
##    Mail: alexbenincasa@ymail.com
##    2019
#######################################
##    Melhorias descritas: ETL com pandas, atualização do By as by com find_elements
##
## Julianna Santos
## mail: juliannafabiola06@gmail.com
## 2023
#######################################

from selenium import webdriver
from selenium.webdriver.common.by import By as by

def inicio_crawler():
 processos = []
 nomes = []
 cpfs = []
 datas_transito = []
 datas_irregularidade = []

browser = webdriver.Chrome()

url = "https://www.tcerj.tc.br/contas-irregulares/#/home"

def requisitar_site(url):
    browser.get(url)

def tratamento_dados(cols):
    
   col0, col1, col2, col3, col4 = cols
   return col0.text, col1.text, col2.text, col3.text, col4.text

def analisar_requisicao(content):
 count = 0
while count <= 53:
    rows = browser.find_elements(by.CSS_SELECTOR, 'tbody tr') #linhas
    for tr in rows:
        cols = tr.find_elements(by.CSS_SELECTOR, 'td')
        print(tr.text)
        Processo, Nome, CPF, Data_Transito, Data_Irregularidade = separa_colunas(cols)
        anon_cpf = f'{CPF[:8]}***{CPF[-3:]}'
        processos.append(Processo)
        nomes.append(Nome)
        cpfs.append(anon_cpf)
        datas_transito.append(Data_Transito)
        datas_irregularidade.append(Data_Irregularidade)
    if count < 53:
        browser.find_element(by.CSS_SELECTOR, 'li.pagination-next').click()
    count = count + 1


def armazenar_dados(trusted_data):
 dados = {
    'processo': processos,
    'nome': nomes,
    'cpf': cpfs,
    'datas_transito': datas_transito,
    'datas_irregularidade': datas_irregularidade,
}

import pandas as pd
df = pd.DataFrame(dados)

filename = 'contas_irregulares2.csv'
df.to_csv(filename, sep= ';')

browser.quit()

