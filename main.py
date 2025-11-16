import sys
from stats import word_count
from stats import character_count
from stats import listed_count

def get_book_text(filepath):

    # returns contents of the file.
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    #frankenstein = get_book_text("books/frankenstein.txt")
    #num_of_words = word_count(frankenstein)
    #print(f"Found {num_of_words} total words")
    #num_of_characters = character_count(frankenstein)
    #print(num_of_characters)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_of_words = word_count(book)
    num_of_characters = character_count(book)
    ordered_count = listed_count(num_of_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in ordered_count:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")
    print("============= END ===============")
    sys.exit(0)
    
#print(sys.argv)
main()