1. Instalar o beautiful soup

```pip3 install beautifulsoup4) ```

2. Importar o bs4 para o projeto
3. O Beuatiful soup só consegue mexer em objetos que sejam do tipo dele, do tipo bs4, por assim dizer. Como o case começou com Selenium, é preciso transformar aquele objeto selenium para um objeto bs4, por isso fazemos o _parse_ de um pra outro.

4. O parser utilizado foi o lxml pois ele é mais rápido que o parser html. Isso porque uma das métricas analisada é o tempo de execução e o lxml é mais rápido, dentre outras vantagens, conforme imagem a seguir.

![parsers_lxml](/img/parser_bs4.png) 

Imagem extraída da documentação oficial do [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/)

5. A partir daí, a forma de extração depende do que se deseja e da afinidade. Eu utilizei css selector e busca por tags por ser mais intuitivo e fácil para mim. Além de que o css selector ser mais rápido que xpath.