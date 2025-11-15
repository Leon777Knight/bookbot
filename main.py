def get_book_text(filepath):

    # returns contents of the file.
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    print(frankenstein)

main()