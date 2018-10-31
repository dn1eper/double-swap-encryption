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

def str_to_seq(string):
    """
    Преобзаует сроку в сортирующую последовательность по буквам
    """
    dct = {i: string[i] for i in range(len(string))}
    dct = sorted(dct.items(), key = lambda x: x[1])
    return [dct[i][0] for i in range(len(dct))]
