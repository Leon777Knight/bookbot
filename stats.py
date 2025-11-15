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