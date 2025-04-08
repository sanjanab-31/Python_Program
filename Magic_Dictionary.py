# MAgic Dictionary
class MagicDictionary:
    def __init__(self):
        self.words = []
    def add_word(self, word):
        self.words.append(word)
    def search_word(self, word):
        return word in self.words
magic_dict = MagicDictionary()
magic_dict.add_word("hello")
magic_dict.add_word("world")
print(magic_dict.search_word("hello"))  
print(magic_dict.search_word("python"))  