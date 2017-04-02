import string
with open('text.txt', 'rt') as f:
    text = f.read().lower()

text = text.translate({ord(char): ' ' for char in string.punctuation})

words = text.split()
word_counter = {}

for word in words:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] +=1

counter_words = [(number, word) for word, number in word_counter.items()]
counter_words.sort(reverse=True)

with open('word_counter.txt', 'wt') as f:
    for number,word in counter_words:
        f.write('{:<20}{:>20}\n'.format(word, number))