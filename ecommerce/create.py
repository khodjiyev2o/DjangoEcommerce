import requests


headers={
    'Authorization': 'Token 266b20ed8cd6c0f58dc08a48804badba58a3120d'
}
endpoint='http://localhost:8000/api/products/create'
data={
    'name': 'Someproduct',
    'price': 32
}
get_response=requests.post(endpoint,json=data,headers=headers)
print(get_response.json())
