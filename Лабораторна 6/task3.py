def compare_vowels_and_consonants(text):
    vowels = set("aeiouy")
    consonants = set("bcdfghjklmnpqrstvwxyz")
    
    text = text.lower()
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    print(f"Кількість голосних : {vowel_count}")
    print(f"Кількість приголосних : {consonant_count}")

    if vowel_count > consonant_count:
        print("Голосних більше.")
    elif consonant_count > vowel_count:
        print("Приголосних більше.")
    else:
        print("Кількість голосних і приголосних однакова.")


text = input("Введіть текст: ")
compare_vowels_and_consonants(text)
