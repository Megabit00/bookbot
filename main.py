from stats import count_stings, count_char, chars_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    text = get_book_text(book_path)
    count_stings(text)

    print("--------- Character Count -------")
    chars_dict = count_char(text)
    sorted_chars = chars_to_sorted_list(chars_dict)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
