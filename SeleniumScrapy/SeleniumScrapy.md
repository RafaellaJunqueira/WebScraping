- Instalar o scrapy com 

```
pip3 install scrapy
```
- O scrapy é um framework mas não sabe lidar com páginas dinâmicas (javascrpit) então ele consegue raspar páginas estáticas mas se tiver que clicar em algo até chegar onde se deseja ou se o carregamento do conteúdo estiver dentro de um javascript (como iframe, por exemplo), ele nao vai conseguir.

- Eu iniciei um projeto inteiro de scrapy com o comando abaixo. Isso deu a ele um nome, my_scrapy, e fez ele iniciailizar na minha pasta todo o projeto com um monte de pastas base.

```
scrapy startproject my_scrapy
```

- É preciso entrar no projeto dele, no caso aqui, se chama my_scrapy ```cd my_scrapy``` e depois criar um spider específico pro seu projeto, utilizando 

```
scrapy genspider <nome_que_quiser> <site_que_quiser>
```

- Ele cria um arquivo com o nome que voce colocou na estrutura do projeto, na parte dos spiders.

- Pra rodar como se fosse o debug normal do vscode, tem que executar no terminal o comando que abre o shell do scrapy, ou seja, uma espécie de ambiente de teste ```scrapy shell```. Ou então, colocar na linha que deseja ter um debugger basta inserir a linha ```import pdb; pdb.set_trace()```. O case vai parar lá e aí, no terminal, pode ir inserindo as coisas e testando, como um debug normal.

- O scrapy gera um spider que vai herdar da classe principal Spider, e requer que o método parse seja sobrescrito. Assim como algumas informações, como o site que se deseja pegar e o nome do spider do projeto.

- DESAFIO: os seletores para pegar elementos se restringem a css_selector e xpath. Limitado...

- DESAFIO: tive que listar como itens todos os campos que serão buscados e extraídos da página.

- DESAFIO: Pra rodar não serve o debuger do vscode, tem que ser com ```scrapy list``` e depois ```scrapy crawl <nome_do_arquivo> (no caso foi scrapy crawl stf_spider)```. Esse nome do arquivo NÃO inclui o ```.py```, somente o nome mesmo.

- "Selenium is much slower when compared to Scrapy."

- O scrapy tem dois métodos bases e por padrão: o def start_requests(self) (que tambem pode ser alterado apenas para uma lista chamada start_urls = [<sites que vc quer>]) e o def parse(self, response) que é responsável por tratar dos dados e fazer a extração do que vc quiser. 

- Esse framework é todo orientado a links, a navegação dele se dá por links. Então ele funciona como envio de request para uma url > indica um callback, que vai fazer a extração dos dados específicos a partir da página inteira que ele pegou. Ele não sabe clicar, nao interaje com a página, mas sabe abrir links, mandar a requisição e extrair dados. A paginação, por exemplo, funciona se o botão de paginar contiver um link que direciona à próxima página.

- DESAFIO: O site identifica o uso de um "robô" de busca e impede a extração, gerando o erro 403, conforme a imagem abaixo:

![erro403](/img/erro403.png)

Para contornar esse problema, foi necessário incluir o user agent (o mesmo necessário no experimento com Requests) no arquivo de settings do projeto de Scrapy e inserir na variável USE_AGENT a chave respectiva.