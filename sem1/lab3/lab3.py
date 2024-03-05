import requests, pprint 
query = 'programming' 
url = 'https://en.wikipedia.org/w/api.php' 
params = { 
    'action': 'query', 
    'format': 'json', 
    'list': 'search', 
    'srlimit': 20, 
    'utf8': 1, 
    'srsearch': query 
} 
response = requests.get(url, params=params).json() 

# Извлечение результатов поиска
search_results = response['query']['search']

# Сортировка данных в порядке времени их последнего изменения
sorted_results = sorted(search_results, key=lambda x: x['timestamp'])

# Вывод списка словарей
pprint.pprint([{'Title': result['title'], 'Last Updated': result['timestamp']} for result in sorted_results])

# for result in sorted_results:
#     print(result['title'], result['timestamp'])
