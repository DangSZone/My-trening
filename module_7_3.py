import string
from re import split


class WordsFinder:
    '''
    Принимает при создании неограниченное количество названий файлов,
    И записывает их в атрибут file_names в виде списка.
    '''

    file_names = []

    def __init__(self, *name_file):
        for nam in name_file:
            self.file_names.append(nam)

    def get_all_words(self):

        '''
        Возвращает словарь all_words, где:
        ключ = имя файла,
        значение = все cлова, разбитые на элементы списка с помощью split(), без пунктуации
        '''

        all_words = {}
        for f_n in self.file_names:
            with open(f_n, 'r', encoding='Utf-8') as file:
                for words in file:
                    words = words.lower()
                    table = str.maketrans("", "", string.punctuation)
                    new_words = words.translate(table)
                    new_words = new_words.split()
                    all_words.setdefault(f_n, 'default_value')
                    if all_words[f_n] == 'default_value':
                        all_words[f_n] = new_words
                    else:
                        all_words[f_n].extend(new_words)
        return all_words

    def find(self, word):

        '''
        word - искомое слово.
        Возвращает словарь, где:
        ключ - название файла,
        значение - позиция первого такого слова в списке слов этого файла.
        '''

        x = self.get_all_words().items()
        word = word.lower()
        find_word = {}
        for key, value in x:
            if word in value:
                find_word[key] = value.index(word)
        return find_word

    def count(self, word):

        '''
        word - искомое слово.
        Возвращает словарь, где:
        ключ - название файла
        значение - количество слова word в списке слов этого файла.
        '''

        x = self.get_all_words().items()
        word = word.lower()
        find_word = {}
        for key, value in x:
            if word in value:
                find_word[key] = value.count(word)
        return find_word


word = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
word.get_all_words()

print(word.find('TEXT'))
print(word.count("TEXT"))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
