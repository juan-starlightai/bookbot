from stats import num_letters, num_words, sorted_list
import sys


def get_book_text(path):
    with open(path) as book:
        file_contents = book.read()
        return file_contents

def main():

    sys_list = sys.argv
    
   
    if len(sys_list) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys_list[1]

    book = get_book_text(book_path)
    count = num_words(book)
    count_letter = num_letters(book)
    sorted_letters = sorted_list(count_letter)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    length = len(sorted_letters)

    for i in range(0,length):
            line = sorted_letters[i]

            char = line["char"]
            nums = line["num"] 

            if char.isalpha() == True:
                print(f"{char}: {nums}")


main()
