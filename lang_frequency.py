import argparse
from collections import Counter
import re

def load_data(filepath):
    file = open(filepath, 'r')
    return file.read()

def get_most_frequent_words(text):
    text = re.findall(r'(\w+)', text.lower())
    most_common_words_tuple = Counter(text).most_common(10)
    return [word for word,quantity in most_common_words_tuple]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    file_name = parser.parse_args().file_name
    print('Ваш файл c данными: {}'.format(file_name))
    text_data = load_data(file_name)
    print('Десять самых часто встречающихся слов в тексте {}:'.format(file_name))
    for number,word in enumerate(get_most_frequent_words(text_data)):
        print('{} - {}'.format(number+1,word))
