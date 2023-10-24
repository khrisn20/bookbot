path_to_book = "books/frankenstein.txt"

def words_counter(book_path):

    with open(book_path) as f:
        file_contents = f.read()

        words = file_contents.split()
        print(len(words))

words_counter(path_to_book)
