countries = {
    "Ukraine": {
        "area": 600000,
        "population": 35000000,
        "continent": "Eurasia"
    },
    "Germany" : {
        "area" : 1200000,
        "population": 5000000,
        "continent": "Eurasia"
    },
    "Canada": {
        "area": 9985000,
        "population": 38000000,
        "continent": "North America"
    },
    "Brazil": {
        "area": 8516000,
        "population": 213000000,
        "continent": "South America"
    },
    "Columbia": {
        "area" : 860000,
        "population" : 330000,
        "continent" : "South America"
    },
    "Australia": {
        "area": 7692000,
        "population": 25600000,
        "continent": "Australia"
    },
    "Germany": {
        "area": 357000,
        "population": 83000000,
        "continent": "Europe"
    },
    "Japan": {
        "area": 377975,
        "population": 125800000,
        "continent": "Asia"
    },
    "Argentina": {
        "area": 2780000,
        "population": 45000000,
        "continent": "South America"
    },
    "South Africa": {
        "area": 1221000,
        "population": 59300000,
        "continent": "Africa"
    }
}

def print_by_key(countries, key):
    print("======================================")
    print(f"Країна: {key}")
    print(f"Площа: {countries[key]['area']} км2")
    print(f"Населення: {countries[key]['population']}")
    print(f"Континент: {countries[key]['continent']}")

def print_all_countries(countries):
    for country in countries:
        print_by_key(countries, country)

def add_country(countries):
    key = input("Введіть назву країни: ")
    area = int(input("Введіть площу країни: "))
    population = int(input("Введіть населення країни: "))
    continent = input("Введіть континент країни: ")
    countries[key] = {"area": area, "population": population, "continent": continent}
    print(f"Країна {key} додана.")

def delete_country(countries):
    key = input("Введіть назву країни, яку бажаєте видалити: ")
    if key in countries:
        del countries[key]
        print(f"Країна {key} видалена.")
    else:
        print(f"Країна {key} не знайдена у словнику.")

def print_sorted_countries(countries):
    for country in sorted(countries.keys()):
        print_by_key(countries, country)

def print_suitable_countries(countries, searched_continents):
    for country, data in countries.items():
        if data["continent"] in searched_continents:
            print_by_key(countries, country)

def main():
    searched_continents = ["Asia", "Africa"]

    while True:
        print("\nОберіть опцію:")
        print("1 - Вивести всі записи у словнику")
        print("2 - Додати новий запис у словник")
        print("3 - Видалити запис зі словника")
        print("4 - Вивести відсортований за назвою країни словник")
        print("5 - Вивести країни, що знаходяться в Африці або Азії")
        print("0 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print_all_countries(countries)
        elif choice == "2":
            add_country(countries)
        elif choice == "3":
            delete_country(countries)
        elif choice == "4":
            print_sorted_countries(countries)
        elif choice == "5":
            print_suitable_countries(countries, searched_continents)
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")


main()
