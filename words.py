# words

file = open(r'C:\Users\hp\Pygame\Hangman\word_w', 'r')
raw = file.read()
file.close()

words = raw.split(', ')
words.remove(words[-1])
words.remove(words[-1])

final_words = []
for i in words:
    if len(i) <= 9:
        final_words.append(i)
