#Path to book to be analyzed
path_to_book = "books/frankenstein.txt"

#Function that return the total word count for the book
def words_counter(book_path):

    with open(book_path) as file:
        file_contents = file.read()

        words = file_contents.split()
        return len(words)

#Function that returns dictionary with the count of each character
def letter_instances(book_path):

    with open(book_path) as file:
        file_contents = file.read()
        file_contents = file_contents.lower()

        letter_count_dict = {}
        for letter in file_contents:
            if letter in letter_count_dict:
                letter_count_dict[letter] += 1
            else:
                letter_count_dict[letter] = 1
        
        return letter_count_dict

total_words = words_counter(path_to_book)
letter_count = letter_instances(path_to_book)

#Print book report to console
print(f"--- Begin report of {path_to_book} ---")
print(f"{total_words} words found in the document")

for key in letter_count:
    print(f"The {key} character was found {letter_count[key]} times")

print("--- End report ---")