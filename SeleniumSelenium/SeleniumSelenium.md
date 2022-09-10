1. Instalar o driver (chrome driver ou firefox driver). 
Ele depende do seu sistema operacional e da versão do seu navegador, então atentar-se a isso.
    - Chrome: https://sites.google.com/chromium.org/driver/
    - Firefox: https://github.com/mozilla/geckodriver/releases

Para que o driver possa ser utilizado em ambiente Linux, basta rodar o comando, assim, seus drives ficarão no core da máquina.
```sudo mv chromedriver /src/bin``` ou ```sudo mv geckodriver /src/bin```

Caso seja windows, basta colocar os drivers dentro da pasta do projeto.

2. Instalar selenium 
``` sudo pip install selenium ```

3. Para usar as funções de buscar por elementos, é preciso importar especificamente o By do selenium.webdriver.common.by. Alterações foram feitas no selenium em 2022.

4. Muitas vezes a página demora um pouco a carregar mas o selenium ja tenta achar o elemento de uma vez. Isso pode dar elemento nao encontrado ou em stale (sem referência). Para isso, existem formas de "esperar" a página carregar. A forma menos sofisticada é utilizando o recurso time.sleep .