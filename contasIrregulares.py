#######################################
##  TCERJ Contas Irregulares
##    Busca de contas irregulares no TCERJ com Número de Processo, Nome, CPF e Data do Trânsito em Julgado
##
##    Author: Alex Benincasa Santos 
##    Mail: alexbenincasa@ymail.com
##    2019
#######################################

import os
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait

# caminho para o binário do geckodriver.exe
bin_path = 'C:\\www\\tcerj\\geckodriver.exe'

browser = webdriver.Firefox(executable_path=bin_path)
wait = WebDriverWait(browser, 15)

url = "https://www.tcerj.tc.br/contas-irregulares/#/home"
browser.get(url)

# esperando os dados serem carregados
wait.until(ec.presence_of_all_elements_located((by.CSS_SELECTOR, '#datagrid-0 tbody tr')))

while True:
	for row in browser.find_elements_by_css_selector('#datagrid-0 tbody tr'):
		print(row.text)

	if browser.find_element_by_css_selector('li.pagination-next'):
		browser.find_element_by_css_selector('li.pagination-next a').click()
	else:
		break

browser.quit()