1. Antes de utilizar a biblioteca requests, é preciso verificar se o site apresenta suporte de API para coleta dos dados va requisição. A forma utilizada neste experimento se deu da seguinte forma: inpecionando a tela e acessando as respostas geradas ao realizar uma busca. Dentre as respostas de tipo json, foi analisado se alguma contemplava as respostas do site. O retorno foi positivo e uma delas continha todos os resultados, conforme a imagem abaixo.

![request_get](/img/request_get.png)

Abrindo a resposta (dois cliques sobre a url), é possível ver que todos os dados estavam presentes nesta response do tipo GET. 

![json_response](/img/json_response.png)

2. Desta forma, foi necessário fazer uma requisição direto nesta url que devolvia uma resposta JSON com todos os resultados.

3. Após acessar os dados JSON, na resposta, foi preciso passar pela resposta e reorganizar os dados para serem estruturados da forma desejada (no caso destes experimentos, uma lista de dicionários).

4. Caso o resultado tenha paginação, foi criada uma variável ```current_page``` que se alteraria e seria incorporada à requisição para coleta dos resultados até que se findassem.

5. Ao utilizar o requests, vc nao precisa de um driver porque ele nao vai raspar nada de nenhum navegador, vai apenas fazer uma requisição que nao precisa de interface.

6. O resultado de uma requisição vem como json, fica a critério do desenvolvedor tratar os dados da forma mais conveniente. Para este experimento, informações adicionais que vieram na resposta da requisição foram excluídas para que as informações salvas fossem as mesmas que aparecem quando é feita a raspagem no site, pela interface.

7. Criei uma classe auxiliar para mapear as chaves recebidas na response da API e poder modificar a forma como apareceriam ao guardar os dados, aoenas para fins de organização dos dados.