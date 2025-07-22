from stats import words_count, char_count, to_sorted_list

def get_book_test(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    book = get_book_test("./books/frankenstein.txt")
    num_words = words_count(book)
    print("=======+==== BOOKBOT ===+========")
    print("Analyzing book found at: books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    
    # for key, value in char_count(book).items():
    #     print(f"{key}: {value}")
    dict = char_count(book)
    sorted_list = to_sorted_list(dict)
    # print(sorted_list)
    for key, value in sorted_list:
        if key.isalpha():
            print(f"{key}: {value}")
    print("============ END ==============")

main()    