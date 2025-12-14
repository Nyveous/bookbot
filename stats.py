def get_num_words(contents):
    words = contents.split()
    num_words = len(words)
    return num_words
    
def get_num_char(contents):
    characters = {}
    lower_contents = contents.lower()
    for char in lower_contents:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters



