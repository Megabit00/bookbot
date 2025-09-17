

def count_stings(text):
    num_words = len(text.split())
    print(f"{num_words} words found in the document")





def count_char(teksti):
    teksti_low_case = teksti.lower()
    dict = {}
    for char in teksti_low_case:

        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
        

    return dict

    
    
