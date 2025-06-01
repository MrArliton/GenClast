# Преобразует файлы кластеризации к читаемому виду
import json
# Путь до папки где лежат данные кластеризации
path = 'C:\\Users\\MrArl\\Genetic Nii\\cancer-testicular-two-nodes-and-dist\\Clasters\\Agglomerative - ward'
# Название файлов без индексов
file = 'cls'
# Перечисление индексов для преобразования
indexes = range(5,8 + 1)
for index in indexes:
    mp = 0
    with open(path + '/' + file + f'{index}.json', 'r') as fl:
        mp = json.load(fl)

    with open(path + '/' + f'out{index}.txt', 'w') as fl:
        for index, item in mp.items():
            fl.write(index + ' кластер: [')
            if(len(mp[index]['points']) > 0):
                fl.write(f'{mp[index]["points"][0]+1} ')
            for point in range(1,len(mp[index]['points'])):
                fl.write(f', {mp[index]["points"][point]+1}')
            fl.write(']')
            fl.write(f', Количество:{mp[index]["length"]}')
            fl.write('\\\\ \n')
                
    
