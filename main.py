from stats import get_num_words
from stats import get_num_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
        return contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    message = f"Found {num_words} total words"
    print(message)
    print(num_char)
    

main()

# Found 75767 total words