def get_book_text(filepath):

    # returns contents of the file.
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    all_words = text.split()
    return len(all_words)

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    num_of_words = word_count(frankenstein)
    print(f"Found {num_of_words} total words")

main()