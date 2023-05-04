import os

# Список файлов
file_list = ['1.txt', '2.txt', '3.txt']

# Функция для получения количества строк в файле
def get_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return len(f.readlines())

# Список с информацией о файлах
file_info_list = [(filename, get_file_lines(filename)) for filename in file_list]

# Сортируем список по количеству строк в файле
file_info_list.sort(key=lambda x: x[1])

# Записываем содержимое файлов в результирующий файл
with open('result.txt', 'w', encoding='utf-8') as f:
    for filename, file_lines in file_info_list:
        f.write(filename + '\n')
        f.write(str(file_lines) + '\n')
        with open(filename, 'r', encoding='utf-8') as f_in:
            f.write(f_in.read())
        f.write('\n')  # добавляем символ переноса строки