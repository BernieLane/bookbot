import sys
from stats import get_num_words, get_num_appearance, sorted_list

# book = './books/frankenstein.txt'


def get_book_text(book):
    with open(book) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    word_count = f"Found {get_num_words(get_book_text(book))} total words"
    char_count = get_num_appearance(get_book_text(book))
    sorted_chars = sorted_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for i in range(0, len(sorted_chars)):
        print(f"{sorted_chars[i]["char"]}: {sorted_chars[i]["num"]}")
    print("============= END ===============")

main()