def num_words(text):
    all_words = text.split()
    num_words = len(all_words)

    return num_words

def num_letters(text):
    letters = {}

    for letter in text:
        lowercase = letter.lower()

        if lowercase in letters:
            letters[lowercase] += 1
        else:
            letters[lowercase] = 1

    return letters

def sort_on(letters):
    return letters["num"]

def sorted_list(letters):
    list = []


    for letter in letters:
        specific_letter = {"char": letter, "num": letters[letter]}
        list.append(specific_letter)

    list.sort(reverse=True, key=sort_on)
        

    return list
