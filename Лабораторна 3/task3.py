st = input("Введіть строку:")

words_start_with_N = []

for word in st.split(" "):
    if len(word) != 0 and word[0] == "н":
        words_start_with_N.append(word)

if len(words_start_with_N) != 0:
    print("Слова що починаються з літери \"н\" : " +  ", ".join(words_start_with_N))
else:
    print("Немає слів що починаються з літери \"н\"")
