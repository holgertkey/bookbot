def words_count(text):
    splited = text.split()
    return len(splited)

def char_count(text):
    low_text = text.lower()
    dict = {}
    for char in list(low_text):
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def to_sorted_list(dict):
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)