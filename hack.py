from sys import argv
from math import ceil
from itertools import permutations
from lib import _MIN_KEY_LENGTH, _MAX_KEY_LENGTH, str_to_table, create_key

def hack(text):
    """
    Подбирает ключ шифрования к зашифрованому сообщению
    """
    # Перебираем возможные размеры ключа
    for n in range(_MIN_KEY_LENGTH, _MAX_KEY_LENGTH + 1):
        m = ceil(len(text) / n)
        # Создаем таблицу нужного размера
        table = str_to_table(text, n, m)
        # Наборы значений для перебора ключа
        key_set = [i for i in range(n)]
        # Перебираем все возможные перестановки
        for key1 in permutations(key_set):
            # Вычилсяем вторую перестановку на основе первой
            key2 = create_key(key1, m)
            # Получаем дешифровку
            res = ""
            for i in key1:
                for j in key2:
                    if table[i][j] != "-":
                        res += table[i][j]
            # Если она верна, возврашаем результат
            if is_decrypted(res):
                return res
    
    return False

def is_decrypted(text):
    """
    Определяет, является ли полученная строка расшифровкой
    """
    #################
    #               #
    #    ??KAK??    #
    #               #
    #################
    return False

if __name__ == '__main__':
    if len(argv) == 2:
        # Считывание входных данных
        with open(argv[2], 'r', encoding='utf-8') as file:
            text = file.read()
        # Взлом
        hacked = hack(text)
        # Запись результата в файл
        with open("hacked.txt", "w", encoding='utf-8') as file:
            file.write(hacked)
    else:
        print("Неверный ситаксис.\nИспользуйте - hack.py <filename>")