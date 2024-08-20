word = input("Введіть слово: ")

repeated_letters = []
checked_letters = []

for letter in word:
    if letter in checked_letters:
        if letter not in repeated_letters:
            repeated_letters.append(letter)
    else:
        checked_letters.append(letter)

if repeated_letters:
    print("Повторювані букви: " + ", ".join(repeated_letters))
else:
    print("Немає повторюваних букв")