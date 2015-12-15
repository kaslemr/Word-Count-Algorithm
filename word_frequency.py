def word_count(book):
    book = book.lower()
    new_book = ""
    for letter in book:
        if letter in string.ascii_lowercase:
            new_book += letter
        if letter not in string.ascii_lowercase:
            new_book += " "
    new_book = new_book.split()
    word_list = {}
    for word in new_book:
        if word in word_list.keys():
            word_list[word] += 1
        else:
            word_list[word] = 1
    word_list = sorted(word_list.items(), key=operator.itemgetter(1), reverse=True)
    return word_list

def word_count_ranking(word_list, ranking_length):
    count = 0
    for item in word_list:
        print("{} {}".format(item[0], item[1]))
        count += 1
        if count == ranking_length:
            break
