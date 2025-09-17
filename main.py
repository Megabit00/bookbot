from stats import count_stings
from stats import count_char


def get_book_text(path):
    with open(path) as f:
        return f.read()



def main():
    
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    
    the_dict = count_char(text)


    count_stings(text)
    print(the_dict)
    

main()