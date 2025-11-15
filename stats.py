def word_count(text):
    all_words = text.split()
    return len(all_words)

def character_count(text):
    low_text = text.lower()
    counter = {}
    for character in low_text:
        if character not in counter:
            counter[character] = 1
        elif character in counter:
            counter[character] += 1
    return counter

def order_count(diction):
    return diction["count"]

def listed_count(diction):
    ordered_list = []
    for character in diction:
        ordered_list.append({"character": character, "count": diction[character]})
    ordered_list.sort(reverse=True, key=order_count)
    #print(f"List of dictionaries: {ordered_list}")
    return ordered_list
