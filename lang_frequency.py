import argparse
from collections import Counter
import re


def load_data(filepath):

    with open(filepath, 'r') as file_data:
        data_read = file_data.read()
    return data_read

def get_most_frequent_words(text_string):

    list_of_words = re.findall(r'(\w+)', text_string.lower())
    number_of_words = 10
    most_common_words_tuple = Counter(list_of_words).most_common(number_of_words)

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
