1. Às vezes o requests.get() sozinho não consegue acessar o conteúdo porque a página rejeita solicitações GET que não identificam um User-Agent. Isso gera  um erro 403 de forbidden access. Para contornar isso, é preciso inspecionar a tela, verificar em Network a url desejada (mesmo processo na extraçõa por API, para descobrir onde realizar a solicitação), acessar o cabeçalho da requisição e copiar o user agent que aparece lá, conforme imagem seguir:

![user agent](/img/user-agent.png)

As duas seleções em azul indicam a url correspondente ao desejado e o user agent aceito, respectivamente. Ou pode simplesmente rodar o comando ```navigator.userAgent``` no console da inspeção que ele vai aparecer.

2. A requisição get é capaz de receber alguns parâmetros, como cookies, proxies, informações de timeout e informações de headers. Por isso basta passar parâmetros de headers para a requisição e indicar qual informação complementar deve constar na formação da requisição.

3. [desafio] a biblioteca requests não trabalha com interfaces visuais do navegador, ela envia uma solicitação e recebe uma resposta. Essa resposta não é a página web, o get do requests não funciona como o get do selenium. O get do selenium redireciona a página e o do requests faz uma solicitação do tipo HTTP, ou seja, se a resposta daquela URL solicitada não for uma resposta JSON, ou outro formato textual, com os dados desejados, o que será obtido será apenas a página html e seus javascripts.