with open ("sample.txt") as infile:
    book = infile.read()

def clean_sentence(sentence):
    new_sentence = ""
    for letter in sentence:
        if letter not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            new_sentence += letter
    return new_sentence

def strip_book(text):
    text = clean_sentence(text)
    text = text.lower()
    text = text.split()
    return text

book_dictionary = {}
def count_words(book):
    for word in book:
        if word in book_dictionary.keys():
            book_dictionary[word] += 1
        else:
            book_dictionary[word] = 1
    print(book_dictionary)

book = clean_sentence(book)
book = strip_book(book)
book = count_words(book)
print(book)
