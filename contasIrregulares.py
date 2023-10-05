#######################################
##  TCERJ Contas Irregulares
##  Busca de contas irregulares no TCERJ com Número de Processo, Nome, CPF e Data do Trânsito em Julgado
##
##  Author: Alex Benincasa Santos 
##  Mail: alexbenincasa@ymail.com
##  2019
##  -----------------------------
##  ETL com pandas, atualização do By as by com find_elements
##
##  Author: Julianna Santos
##  Mail: juliannafabiola06@gmail.com
##  2023
#######################################

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By as by

def separa_colunas(cols):
   col0, col1, col2, col3, col4 = cols
   return col0.text, col1.text, col2.text, col3.text, col4.text

def analisar_requisicao(browser):
    processos = []
    nomes = []
    cpfs = []
    datas_transito = []
    datas_irregularidade = []
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
    dados = {
        'processo': processos,
        'nome': nomes,
        'cpf': cpfs,
        'datas_transito': datas_transito,
        'datas_irregularidade': datas_irregularidade,
    }
    return dados

def armazenar_dados(dados):
    df = pd.DataFrame(dados)
    filename = 'contas_irregulares2.csv'
    df.to_csv(filename, sep= ';')

def inicio_crawler():
    browser = webdriver.Chrome()
    url = "https://www.tcerj.tc.br/contas-irregulares/#/home"
    browser.get(url)
    dados = analisar_requisicao(browser)
    armazenar_dados(dados)
    browser.quit()

inicio_crawler()