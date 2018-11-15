class Tree:
    def __init__(self, words):
        self.__tree = [list() for i in range(1106 - 1071)]

        for word in words:
            self.add(word)

    def add(self, word):
        if not word:
            return
        try:
            self.__tree[ord(word[0]) - 1071].append(word)
        except Exception:
            pass

    def print(self):
        print(self.__tree)  

    def contains(self, word):
        if not word:
            return
        try:
            for string in self.__tree[ord(word[0]) - 1071]:
                if word == string:
                    return True
        except Exception:
            pass
        return False