from asyncio import selector_events
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://portal.stf.jus.br/')

# select_box = '//select[@class="campo-texto tipo-pesquisa-processo"]'
# driver.find_element(By.XPATH, select_box).click()

driver.find_element(By.XPATH, '//option[@value="PARTE_OU_ADVOGADO"]').click()
driver.find_element(By.ID, 'pesquisaPrincipalParteAdvogado').send_keys('Vitor Borges')
driver.find_element(By.ID, 'btnPesquisar').click()

print('teste')
if __name__ == '__main__':
    print("oi")