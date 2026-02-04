def make_acronym(phrase):
    words = phrase.split()
    acronym = ""
    index = 0

    while index < len(words):
        acronym += words[index][0].upper()
        index += 1

    return acronym


# ===== TEST =====
user_input = input("Enter a phrase: ")
result = make_acronym(user_input)
print("Acronym:", result)
