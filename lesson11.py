import yaml
import json
import pandas as pd

class FilesContainer:

    def __init__(self, number):
        self.number = number
        self.data = []
        self.pddf = pd.DataFrame()

    def get_info(self):
        return f'Number: {self.number}, dicts: {self.data}, df: {self.pddf}'

    def write_yaml(self, name):
        with open(name, 'w') as f:
            yaml.dump(self.data, f)

    def read_yaml(self, name):
        with open(name, 'r') as f:
            yaml_obj = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_obj

    def write_json(self, name):
        with open(name, 'w') as f:
            json.dump(self.data, f, indent=1)

    def read_json(self, name):
        with open(name, 'r') as f:
            json_obj = json.load(f)
        return json_obj

    def write_csv(self, name):
        if not self.data:
            print("Список пуст, CSV будет с C1, C2…")
        self.pddf = pd.DataFrame(self.data)
        self.pddf.to_csv(name, index=False)

    def read_csv(self, name):
        csv_obj = pd.read_csv(name)
        return csv_obj

    def see_pddf(self):
        return self.pddf

    def see_raw_list(self):
        return self.data

# Данные для записи/чтения:
file_cont1 = FilesContainer(1)

file_cont1.list.append({
    'name': 'Egor',
    'surname': 'Nedbaev',
    'age': 22,
    'work': 'cs2 school'
})

file_cont1.list.append({
    'name': 'Natasha',
    'surname': 'Chernysheva',
    'age': 22,
    'work': None
})

file_cont1.list.append({
    'name': 'Gena',
    'surname': 'Nikonov',
    'age': 24,
    'work': 'Builder'
})

file_cont1.list.append({
    'name': 'Andrey',
    'surname': 'Kovalyov',
    'age': 25,
    'work': 'Police'
})

file_cont1.write_yaml('friends.yaml')
# print(file_cont1.read_yaml('friends.yaml'))
file_cont1.write_json('friends.json')
# print(file_cont1.read_json('friends.json'))
file_cont1.write_csv('friends.csv')
# print(file_cont1.read_csv('friends.csv'))

# прочитать yaml и записать в json
data = file_cont1.read_yaml('friends.yaml')
with open(r'friends_from_yaml_to_json.json', 'w') as file:
    json.dump(data, file, indent=1)

# прочитать json и записать в yaml
data = file_cont1.read_json('friends.json')
with open(r'friends_from_json_to_yaml.yaml', 'w') as file:
    yaml.dump(data, file)


# # YAML
#
# yaml_object = yaml.dump(file_cont1.list)  # сериализация данных (+запись в переменную)
# print(yaml_object)
# # запись переменной с сериализированными данными в файл
# with open('friends.yaml', 'w') as file:
#     file.write(yaml_object)
#
# # сериализация и запись одновременно без создания переменной с сериализированными данными:
# with open(r'friends.yaml', 'w') as file:
#     yaml.dump(file_cont1.list, file)
#
# # чтение
# with open(f'friends.yaml', 'r') as file:
#     friends_from_yaml_file = yaml.load(file, Loader=yaml.FullLoader)
# # print(friends_from_yaml_file)
#
#
# # JSON
#
# json_object = json.dumps(file_cont1.list, indent=1) # сериализация данных (+запись в переменную)
# # запись переменной с сериализированными данными в файл:
# with open('friends.json', 'w') as file:
#     file.write(json_object)
#
# # сериализация и запись одновременно без создания переменной с сериализированными данными:
# with open(r'friends.json', 'w') as file:
#     json.dump(file_cont1.list, file, indent=1)
#
# # чтение
# with open(f'friends.json', 'r') as file:
#     friends_from_json_file = json.load(file)
# # print(friends_from_json_file)
#
#
# CSV
#
# df1 = pd.DataFrame(file_cont1.list)
# df1.to_csv('friends.csv', index=False)
#
# friends_from_csv_file = pd.read_csv('friends.csv')
# print(friends_from_csv_file)
