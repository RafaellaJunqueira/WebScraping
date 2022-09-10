import time
import requests
from bs4 import BeautifulSoup

class My_Requests():

    def search_name(self, **in_args):
        user_input = in_args['name']
        request_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'}
        request_url = f'https://portal.stf.jus.br/processos/listarPartes.asp?termo={user_input}'
        response = requests.get(request_url, headers=request_headers)

        # Verificar se a requisição funcionou corretamente
        if response.status_code == 200:
            if response.text == '':
                return list()
            print(response.text)
            # Pode-se visualizar que a resposta printada é somente a estrutura HTML da resposta à requisição, e que nela o local das respostas aparece como javascript, logo, é uma página dinâmica, o que torna impossível a raspagem dos dados. 
            soup = BeautifulSoup(response, "html.parser")

if __name__ == '__main__':
    stf = My_Requests()
    start = time.time()
    args = {"name": "Vitor Borges"}
    stf.search_name(**args)
    end = time.time()
    print(f'TEMPO DE EXECUÇÃO:{end - start}')