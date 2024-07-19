
with open("main/static/main/files/cities.txt", 'r', encoding='utf-8') as file:
    str1 = file.read()
    cities_list = str1.split()

cities_dict = {
    'cities': cities_list
}