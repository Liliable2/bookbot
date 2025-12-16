import sys

from stats import format_char_dict, get_num_char, get_num_words


def get_book_text(book_path):
    with open(book_path) as f:
        contents = f.read()

    return contents


def main():
    # print help text and exit with error code if not 2 arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    # analyze the text
    contents = get_book_text(book_path)
    num_words = get_num_words(contents)
    num_char = get_num_char(contents)
    formatted_char_list = format_char_dict(num_char)

    # print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in formatted_char_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")


main()
