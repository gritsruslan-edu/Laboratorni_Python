import string

def create_file_tf4_1():
    content = """Один два три чотири пять шість сім вісім девять десять 1 12 33 52 148"""
    
    try:
        with open("TF4_1.txt", "w") as file:
            file.write(content)
        print("Файл TF4_1.txt створено.")
    
    except Exception as e:
        print(f"Помилка при створенні файлу: {e}")

def analyze_words():
    word_length_count = {}
    
    try:
        with open("TF4_1.txt", "r") as file:
            content = file.read()
        
        words = content.split()

        for word in words:
            length = len(word)
            if length in word_length_count:
                word_length_count[length] += 1
            else:
                word_length_count[length] = 1

        with open("TF4_2.txt", "w") as file:
            for length in sorted(word_length_count):
                file.write(f"Кількість слів з {length} символів: {word_length_count[length]}\n")
        
        print("Аналіз слів завершено. Результати записані у файл TF4_2.txt.")
    
    except FileNotFoundError:
        print("Помилка: файл TF4_1.txt не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

def print_file_tf4_2():
    try:
        with open("TF4_2.txt", "r") as file:
            content = file.readlines()
            for line in content:
                print(line.strip())
    except FileNotFoundError:
        print("Помилка: файл TF4_2.txt не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

def main():
    create_file_tf4_1()
    analyze_words()
    print("Вміст файлу TF4_2.txt:")
    print_file_tf4_2()

main()
