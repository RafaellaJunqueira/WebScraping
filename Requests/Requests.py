import time
import requests

class RequestResponse:
    TOTAL_PAGES = 'totalDePaginas'
    INTERNAL_ID = 'id'
    INTERNAL_PERSON_ID = 'pessoaId'
    PEOPLE = 'partes'
    request_original_values = {
        'pessoaNome': "Nome do envolvido",
        'processoIdentificacao': 'Idenficador do processo',
        'processoId': 'Numero do processo',
        'processoNumeroUnico': 'Numero Unico',
        'processoDataAutuacao': 'Data de autuacao',
        'processoMeio': 'Tipo de processo',
        'processoPublicidade': 'Publicidade do processo',
        'processoEmTramitacao': 'Processo em tramitacao'
    }

class My_Requests():

    def format_for_list(json_list):
        clean_json = list()
        for item in json_list:
            tmp_dict = dict()
            for key, value in item.items():
                if type(value) is dict():
                    pass
                else:
                    tmp_dict[key] = str(value)
            clean_json.append(tmp_dict)
        return clean_json

    def format_for_dict(self, json_dict):
        clean_json = dict()

        # Percorrer cada item do dicionario, por suas respctivas chaves e valores
        for key, item in json_dict.items():

            # Caso o item do dicionario seja uma lista, percorrer a lista e pegar valores somente se exstirem e não forem strings vazias
            if type(item) is list:
                tmp_list = list()
                for _list in item:
                    if not _list or _list == '':
                        continue
                    tmp_dict = dict()

                    # Percorrer os itens da lista. Caso seja uma lista de listas, vai pegar todos os dados e só depois passar para o resultado final
                    for _key, _item in _list.items():
                        tmp_dict[_key] = _item
                    tmp_list.append(tmp_dict)
                clean_json[key] = tmp_list

            # Caso o item do dicionário seja outro dicionário, a função é chamada recursivamente pois ela mesma trata esse caso e os itens dento do dicionario.
            if type(item) is dict:
               self.format_for_dict(item)

            # Se o item do dicionário sea apenas uma tupla simples, adiciona diretamente ao resultado final
            else:
                clean_json[key] = item
        return clean_json

    def search_name(self, **in_args):
        user_input = in_args['name']
        current_page = '1'
        request_url = f'https://digital.stf.jus.br/integracoes-processos/api/public/partes/processos?nome={user_input}&registrosPorPagina=20&pagina={current_page}'
        response = requests.get(request_url)

        # Verificar se a requisição funcionou corretamente
        if response.status_code == 200:
            if response.text == '':
                return list()
            _response = eval(response.text.replace('false', 'False').replace('null', 'None'))

            # Caso a resposta seja um dicionário
            if type(_response) is dict:
                formated_json = self.format_for_dict(_response)

            # Caso a resposta seja uma lista
            if type(_response) is list:
                formated_json = self.format_for_list(_response)

            # Tratamento dos resultados para que as chaves dos dicionarios tenham dados mais compreensiveis
            final_result = list()
            formated_json.pop(RequestResponse.TOTAL_PAGES)
            for each_item in formated_json[RequestResponse.PEOPLE]:
                tmp_dict = dict()

                # Remover as informações que não são relevantes para o extração desejada
                each_item.pop(RequestResponse.INTERNAL_ID)
                each_item.pop(RequestResponse.INTERNAL_PERSON_ID)

                # Popular um novo dicionario onde as chaves dos valores assume os novos nomes definidos na classe auxiliar RequestResponse
                for key, value in each_item.items():
                    tmp_dict[RequestResponse.request_original_values[key]] = value
                final_result.append(tmp_dict)
            
            print(f'RESULTADO: {final_result}')
            return final_result

if __name__ == '__main__':
    stf = My_Requests()
    start = time.time()
    args = {"name": "Vitor Borges"}
    stf.search_name(**args)
    end = time.time()
    print(f'TEMPO DE EXECUÇÃO:{end - start}')