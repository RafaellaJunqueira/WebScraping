from time import sleep
from turtle import pd
import scrapy
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class STFSpider(scrapy.Spider):
    name = "stf_spider"
    start_urls = ["https://portal.stf.jus.br/"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def parse(self, response, **kwargs):
        self.driver.get(self.start_urls[0])

        select = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tipo-pesquisa-processo")))
        Select(select).select_by_value("PARTE_OU_ADVOGADO")

        self.driver.find_element(By.ID, "pesquisaPrincipalParteAdvogado").send_keys("Vitor Borges")
        self.wait.until(EC.element_to_be_clickable((By.ID, "btnPesquisar"))).click()

        sleep(2)
        self.parse_processes(Selector(text=self.driver.page_source))

    def parse_processes(self, selector):
        result = []

        processes = selector.xpath('//table[@id="tabela_processos"]//tr')[1:]
        for process in processes:
            import pdb; pdb.set_trace()
            item = {
                "Identificação": process.xpath('./td[1]/a/text()').get(),
                "Parte": process.xpath('./td[2]/text()').get(),
                "Número único": process.xpath('./td[3]/text()').get(),
                "Data Autuação": process.xpath('./td[4]/text()').get(),
                "Meio": process.xpath('./td[5]/text()').get(),
                "Publicidade": process.xpath('./td[6]/text()').get(),
                "Trâmite": process.xpath('./td[7]/text()').get(),
            }
            result.append(item)

        print(result)
        self.driver.quit()