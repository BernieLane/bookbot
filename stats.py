def get_num_words(words):
    word_count = 0
    for word in words.split():
        word_count += 1
    return word_count  

def get_num_appearance(words):
    char_count = {}
    for char in words.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sorted_list(char_count):
    sorted_chars = []
    for char, num in char_count.items():
        if str(char).isalpha():
            char_dict = dict(char=char, num=num)
            sorted_chars.append(char_dict)
    sorted_chars.sort(reverse=True, key=lambda x: x['num'])
    return sorted_chars