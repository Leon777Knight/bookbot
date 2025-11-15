from stats import word_count
from stats import character_count

def get_book_text(filepath):

    # returns contents of the file.
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    num_of_words = word_count(frankenstein)
    print(f"Found {num_of_words} total words")
    num_of_characters = character_count(frankenstein)
    print(num_of_characters)

main()