def count_stings(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")
    return num_words


def count_char(teksti):
    teksti_low_case = teksti.lower()
    dict = {}
    for char in teksti_low_case:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def sort_on(item):
    return item["num"]


def chars_to_sorted_list(chars_dict):
    list_of_dicts = []
    for char, count in chars_dict.items():
        if char.isalpha():  # keep only letters
            list_of_dicts.append({"char": char, "num": count})

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

    

