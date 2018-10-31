_MAX_TEXT_LENGTH = 50
_MAX_KEY_LENGTH = 10
_MIN_KEY_LENGTH = 3

def convert_text(text):
    """
    Убирает пробелы, знаки припенания и приводит текст к нижнему регистру.
    Возвращает обрезанный текст, если он слишком длинный.
    """
    res = []
    for char in text.lower():
        for i in range(1072, 1104):
            if char == chr(i):
                res.append(char)
                break
        if len(res) == _MAX_TEXT_LENGTH:
            break
    
    return res

def convert_key(key):
    """
    Убирает пробелы и обрезает ключ при избыточной длине
    """
    res = []
    for char in key:
        if char != " ":
            res.append(char)
        if len(res) == _MAX_KEY_LENGTH:
            break
    if len(res) < _MIN_KEY_LENGTH:
        raise Exception("Ключ слишком короткий, минимальная длина ключа " + str(_MIN_KEY_LENGTH))

    return res

def create_key(key, length):
    """
    Создает ключ заданной длинны на основе исходного ключа
    """
    if len(key) < length:
        return create_key(key * 2, length)
    else:
        return key[:length]

def str_to_sort_seq(string):
    """
    Преобзаует сроку в отсортированную по буквам последовательность цифр,
    соответствующих позициям этих букв в исходной строке.
    Пример: "бва" -> [2,0,1]
    """
    dct = {i: string[i] for i in range(len(string))}
    dct = sorted(dct.items(), key = lambda x: x[1])
    return [dct[i][0] for i in range(len(dct))]

def str_to_seq(string):
    """
    Преобзаует сроку в последовательность цифр,
    соответствующих буквенному порядку.
    Пример: "бва" -> [1,2,0]
    """
    arr = [0 for i in range(len(string))]
    j = 0
    for i in str_to_sort_seq(string):
        arr[i] = j
        j += 1
    return arr

def str_to_table(string, n, m):
    """
    Помещает строку в таблицу размера n на m
    """
    table = [["-"] * m for i in range(n)]
    # Помещаем текст в таблицу
    i = 0
    j = 0
    for char in string:
        table[i][j] = char
        j += 1
        if j == m:
            j = 0
            i += 1

    return table
