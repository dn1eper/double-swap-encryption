from sys import argv
from math import ceil
from lib import *

_RES_FILE_NAME = "decrypted.txt"

def decrypt(text, key):
    """
    Дешифрует текст с помощью полученного ключа методом двойной перестановки
    """
    # Преобразуем входные данные к нужному формату
    text = convert_text(text)
    key = convert_key(key)
    # Вычисляем размеры таблицы
    m = ceil(len(text) / len(key))
    # Создаем таблицу (матрицу) нужного размера
    table = str_to_table(text, len(key), m)
    # Генерируем второй ключ из первого нужной длинны
    key2 = str_to_seq(create_key(key, m))
    key1 = str_to_seq(key)

    # Дешифруем, обходя строки и столбцы таблицы в обратном порядке, который задается ключами
    res = ""
    for i in key1:
        for j in key2: 
            if table[i][j] == "-":
                res += " "
            else:
                res += table[i][j]

    return res.rstrip()

if __name__ == '__main__':
    if len(argv) == 3:
        # Считывание входных данных
        key = argv[1]
        with open(argv[2], 'r', encoding='utf-8') as file:
            text = file.read()
        # Дешифрование
        decrypted = decrypt(text, key)
        # Запись результата в файл
        with open(_RES_FILE_NAME, "w", encoding='utf-8') as file:
            file.write(decrypted)
            print("Расшифрованый текст помещен в файл " + _RES_FILE_NAME)
    else:
        print("Неверный ситаксис.\nИспользуйте - decrypt.py <key> <filename>")