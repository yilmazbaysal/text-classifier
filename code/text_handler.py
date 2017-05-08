import re
from collections import defaultdict
from os import listdir, path

from nltk.stem import PorterStemmer


class TextHandler:

    def __init__(self):
        self.stemmer = PorterStemmer()

        self.vocabulary = set()
        self.stop_words = self.__get_stop_words()
        self.train_data = self.__read_train_data()

    def __read_train_data(self, folder_path='data/corpus'):
        result = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

        for directory in listdir(folder_path):
            for file in listdir(path.join(folder_path, directory)):
                for token in self.__clean(open(path.join(folder_path, directory, file)).read()):
                    if token not in self.stop_words:
                        result[directory][file][token] += 1
                        self.vocabulary.add(token)

        return result

    def get_train_data(self):
        return self.train_data

    def get_vocabulary(self):
        return self.vocabulary

    def __get_stop_words(self, file_path='data/stop_words.txt'):
        f = open(file_path, 'r')

        return self.__clean(f.read())

    def __clean(self, text):
        text = re.sub('([^\w\d\s])', '', text)

        return [self.stemmer.stem(word) for word in text.split()]
