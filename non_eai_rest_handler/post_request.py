import requests

data = {'somekey': 'somevalue'}
r = requests.post('https://localhost:8089/services/movie_count_by_lang', auth=('admin', 'monitor!'),verify=False,data=data)
print(r.text)