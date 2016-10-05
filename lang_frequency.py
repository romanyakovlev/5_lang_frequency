

def load_data(filepath):
    file = open(filepath, 'r')
    return file.read()

def get_most_frequent_words(text):
    text = ' '.join(text.split('\n')).split(' ')
    arr = sorted([x for x in list(set(text)) if x != ''])
    mx = max(text.count(x) for x in arr)
    for x in arr:
        if text.count(x) == mx:
            return x
            break

if __name__ == '__main__':
    text = load_data('1.txt')
    print(get_most_frequent_words(text))
