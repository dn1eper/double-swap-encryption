from sys import argv
from math import ceil
from itertools import permutations
from lib import _MIN_KEY_LENGTH, _MAX_KEY_LENGTH, str_to_table, create_key, str_to_seq
from display import display

_RES_FILE_NAME = "hacked.txt"

def hack(text, vocabulary):
    """
    Подбирает ключ шифрования к зашифрованому сообщению
    """
    # Перебираем возможные размеры ключа
    for n in range(_MIN_KEY_LENGTH, _MAX_KEY_LENGTH + 1):
        print("\tПодбираем ключ длины " + str(n) + " ...", end="")
        m = ceil(len(text) / n)
        # Создаем таблицу нужного размера
        table = str_to_table(text, n, m)
        # Наборы значений для перебора ключа
        key1_set = [i for i in range(n)]
        # Перебираем все возможные перестановки 
        for key1 in permutations(key1_set):
            key2 = str_to_seq(create_key(key1, m))
            # Получаем дешифровку
            res = ""
            for i in key1:
                for j in key2:
                    if table[i][j] == "-":
                        res += " "
                    else:
                        res += table[i][j]
            # Если она верна, возврашаем результат
            if is_decrypted(res, vocabulary):
                return res
            else: display()

def is_decrypted(text, vocabulary):
    """
    Определяет, является ли полученная строка расшифровкой
    """
    num = 2
    count = 0
    # Перебираем первые num слов в тексе
    for word in text.split(" ", num):
        if len(word) < 26:
            # Перебираем все слова в словаре
            for voc in vocabulary.split('\n'):
                if word == voc:
                    count += 1
                    break
    
    if count == num:
        return True
    else: 
        return False

if __name__ == '__main__':
    if len(argv) == 2:
        # Читаем текст
        with open(argv[1], 'r', encoding='utf-8') as file:
            text = file.read()
        # Читаем словарь
        with open('dict.binary', 'r', encoding='utf-8') as file:
            vocabulary = file.read()
        # Взлом перебором
        hacked = hack(text, vocabulary)
        # Запись результата в файл
        with open(_RES_FILE_NAME, "w", encoding='utf-8') as file:
            file.write(hacked)
            print("Подобранный текст помещен в файл " + _RES_FILE_NAME)
    else:
        print("Неверный ситаксис.\nИспользуйте - hack.py <filename>")