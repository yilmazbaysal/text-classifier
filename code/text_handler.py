import re
from collections import defaultdict
from os import listdir, path

from nltk.stem import SnowballStemmer


class TextHandler:

    def __init__(self):
        self.stemmer = SnowballStemmer(language='english')

        self.vocabulary = set()
        self.stop_words = self.__get_stop_words()
        self.train_data = self.__read_train_data()

    def __read_train_data(self, folder_path='data/train'):
        """
        Reads all files in the given directory recursively. Stores them in a dict with their folder names.
        :param folder_path: Path of the train data folder.
        :return: A dictionary which stores folder_name, file_name, cleaned_token_list
        """
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

    def get_test_data(self, folder_path='data/test'):
        """
            Reads all files in the given directory in the alphabetical order.
            :param folder_path: Path of the test data folder.
            :return: (Name of the read file, List of the tokens in the read file)
        """
        for file_name in sorted(listdir(folder_path)):

            word_list = list()
            for token in self.__clean(open(path.join(folder_path, file_name)).read()):
                if token not in self.stop_words:
                    word_list.append(token)

            yield file_name, word_list  # Generator (A file at each iteration)

    def __clean(self, text):
        """
        Cleans the given text from punctuations and puts the tokens in a stemmer.
        :param text: A string which it's tokens separated by whitespaces.
        :return: Cleaned and stemmed token list.
        """
        text = re.sub('([^\w\d\s\-])', '', text).lower()

        return [self.stemmer.stem(word) for word in text.split()]
