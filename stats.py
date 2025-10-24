def count_words(file_contents):
    words = file_contents.split()

    return len(words)

def count_characters(file_contents):
    characters = {}
    lower_case_file_contents = file_contents.lower()

    for i in range(len(file_contents)):
        if not lower_case_file_contents[i] in characters:
            characters[lower_case_file_contents[i]] = 1
        else:
            characters[lower_case_file_contents[i]] +=1

    return characters

def sort_dictionary(characters):
    char_list = []
    for ch, count in characters.items():
        char_list.append({"char":ch,"num":count})

    def get_num(list):
        return list["num"]

    char_list.sort(key=get_num,reverse=True)

    return char_list
