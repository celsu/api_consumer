import requests

# Definindo a URL da API
url = 'https://jsonplaceholder.typicode.com/posts'

# Fazendo a requisição GET à API
response = requests.get(url)

# Verificando se a requisição foi besm-sucedida (código 200)
if response.status_code == 200:
    # Convertendo os dados da resposta para formato JSON
    data = response.json()
    
    # Iterando sobre os posts e imprimindo seus títulos
    for post in data:
        print("Titulo: "+post['title'])
        print("descri: "+post['body'].replace('\n', ''))
        print("")
else:
    # Se a requisição não foi bem-sucedida, imprimir o código de status
    print(f"Erro ao acessar a API. Código de status: {response.status_code}")