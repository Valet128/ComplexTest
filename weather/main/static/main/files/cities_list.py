import json

with open("main/static/main/files/cities.json", encoding='utf-8') as file:
    result = json.load(file)
    
cities_list = []
for i in result['city']:
    if i['name'] not in cities_list:
        cities_list.append(i['name'])
cities_dict = {
    'cities': cities_list
}
