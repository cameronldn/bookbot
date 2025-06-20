import sys
from stats import get_book_word_count, get_book_character_count, get_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_book_report(sys.argv[1])
    


def print_book_report(book_path):
    contents = get_book_text(book_path)
    word_count = get_book_word_count(contents)
    character_count = get_book_character_count(contents)
    sorted_list = get_sorted_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in range(len(sorted_list)):
        if sorted_list[char]["char"].isalpha() is not True:
            continue
        print(f"{sorted_list[char]["char"]}: {sorted_list[char]["num"]}")
    print("============= END ===============")

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents

main()