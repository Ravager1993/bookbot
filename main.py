import sys
from stats import count_words
from stats import count_characters
from stats import sort_dictionary

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    
    file_contents = get_book_text(sys.argv[1])
    num_words = count_words(file_contents)
    characters = count_characters(file_contents)
    sorted_list = sort_dictionary(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()