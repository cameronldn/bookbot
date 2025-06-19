def sort_on(dict):
    return dict["num"]

def get_book_word_count(bookText):
    words = bookText.split()
    return len(words)
    # print(f"{len(words)} words found in the document")

def get_book_character_count(bookText):
    # print(f"Character Count: {len(bookText)}")
    character_count = {}
    for char in bookText.lower():
        if char in character_count:
             character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def get_sorted_list(dictionary):
    new_list = []
    for entry in dictionary:
        new_list.append({"char": entry, "num": dictionary[entry]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list