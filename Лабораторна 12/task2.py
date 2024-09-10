import json

def load_countries_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Створюємо новий.")
        return {}
    except json.JSONDecodeError:
        print("Помилка декодування JSON.")
        return {}

def save_countries_to_file(filename, countries):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(countries, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Помилка запису у файл: {e}")

def print_by_key(countries, key):
    print("======================================")
    print(f"Країна: {key}")
    print(f"Площа: {countries[key]['area']} км2")
    print(f"Населення: {countries[key]['population']}")
    print(f"Континент: {countries[key]['continent']}")

def print_all_countries(countries):
    if countries:
        for country in countries:
            print_by_key(countries, country)
    else:
        print("Список країн порожній.")

def add_country(countries):
    key = input("Введіть назву країни: ")
    if key in countries:
        print(f"Країна {key} вже існує.")
        return
    area = int(input("Введіть площу країни: "))
    population = int(input("Введіть населення країни: "))
    continent = input("Введіть континент країни: ")
    countries[key] = {"area": area, "population": population, "continent": continent}
    print(f"Країна {key} додана.")

def print_suitable_countries(countries, searched_continents):
    for country, data in countries.items():
        if data["continent"] in searched_continents:
            print_by_key(countries, country)

def main():
    filename = 'data.json'
    searched_continents = ["Asia", "Africa"]

    countries = load_countries_from_file(filename)
 
    while True:
        print("\nОберіть опцію:")
        print("1 - Вивести всі записи з JSON файлу")
        print("2 - Додати новий запис у JSON файл")
        print("3 - Вивести країни, що знаходяться в Африці або Азії")
        print("0 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print_all_countries(countries)
        elif choice == "2":
            add_country(countries)
            save_countries_to_file(filename, countries)  # Зберігаємо зміни після додавання
        elif choice == "3":
            print_suitable_countries(countries, searched_continents)
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
