# Extração de dados em ambiente Web
Este repositório destina-se aos scripts de extração de dados, utilizando ferramentas e tecnologias para web scraping, como parte prática do Trabalho de Conclusão de Curso 2 em Engenharia de Software.

### Licença
Todos os experimentos deste projeto foram criados e executados para fins acadêmicos, como forma de analisar ferramentas e métodos de extração de dados. Nenhum _script_ foi ou será utilizado para denegriar a imagem da instituição fonte ou para corromper dados acessados.

### Pré-requisitos:
1. Python3 ``` sudo apt-get install python3 ```

2. Pip3 ```sudo apt-get install python-pip```

3. Selenium ```sudo pip3 install selenium```

4. WebDrivers (Chrome e Firefox)

     Chrome: ```https://sites.google.com/chromium.org/driver/```

     Firefox: ```https://github.com/mozilla/geckodriver/releases```
     
5. Mover os WebDrivers para a raíz da máquina

     Chrome: ```sudo mv chromedriver /src/bin```

     Firefox: ```sudo mv geckodriver /src/bin```

6. Beautiful Soup ```pip3 install beautifulsoup4```

7. Scrapy ```pip3 install scrapy```

### Execução dos códigos

1. Clone o repositório ```git clone https://github.com/RafaellaJunqueira/WebScraping.git```
2. Executar experimento 1 (Selenium)
- Acessar o diretório do experimento:
``` cd SeleniumSelenium ```

- Executar o script: ```python3 SeleniumSelenium.py```

3. Executar experimento 2 (Selenium + Beautiful Soup)
- Acessar o diretório do experimento:
``` cd SeleniumBs4 ```

- Executar o script: ```python3 SeleniumBs4.py```

4. Executar experimento 3 (Requisição em API)
- Acessar o diretório do experimento:
``` cd Requests ```

- Executar o script: ```python3 Requests.py```

5. Executar experimento 4 (Selenium e Scrapy)
- Acessar o diretório do experimento:
``` cd SeleniumScrapy ```

- Executar o script: ```python3 SeleniumScrapy.py```

### Executar script para tempos de execução
Na raíz do projeto, executar: ```python3 expTimes.py```


<!-- 
## Referências - dicas
[Site para baixar os driver](https://github.com/mozilla/geckodriver/releases)

[Video sobre webdriver](https://www.youtube.com/watch?v=Ot10qzrb13c)
 -->
