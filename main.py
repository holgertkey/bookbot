from stats import words_count, char_count, to_sorted_list

import sys

def get_book_test(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]    
    book = get_book_test(book_path)
    num_words = words_count(book)
    print("=======+==== BOOKBOT ===+========")
    print(f"Analyzing book found at: {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    
    dict = char_count(book)
    sorted_list = to_sorted_list(dict)

    for key, value in sorted_list:
        if key.isalpha():
            print(f"{key}: {value}")
    print("============ END ==============")

main()    