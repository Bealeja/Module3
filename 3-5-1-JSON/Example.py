import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print(r.text)
print(type(r.text))

content = json.loads(r.text)

print(content['title'])
print(type(content))


# OUTPUT:
# {
#   "userId": 1,
#   "id": 1,
#   "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#   "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
# }
# <class 'str'>
# sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# <class 'dict'>