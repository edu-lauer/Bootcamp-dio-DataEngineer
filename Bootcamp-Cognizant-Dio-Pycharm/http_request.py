import requests


def dados_cep(cep):
    response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
    dados_json = response.json()  # retorna um dicionário
    dados_str = response.text  # retorna uma “string”
    print(response.status_code)
    print(response.text)
    print(dados_json['logradouro'])
    return dados_json


def api_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
    print(response.status_code)
    dados_pokemon = response.json()
    return dados_pokemon


pikachu = api_pokemon('pikachu')
print(pikachu)
