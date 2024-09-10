import json

countries = [
    {
        "Name": "Ukraine",
        "area": 600000,
        "population": 35000000,
        "continent": "Eurasia"
    },
    {
        "Name": "India",
        "area": 3287000,
        "population": 1393000000,
        "continent": "Asia"
    },
    {
        "Name": "Egypt",
        "area": 1010000,
        "population": 104000000,
        "continent": "Africa"
    }
]

jsonData = json.dumps(countries)
with open("data.json", "w") as file:
    file.write(jsonData)

while True:
    command = input("Enter command (1 - add, 2 - view, 3 - find with Asia or Africa, 4 - quit): ")

    if command == "1":
        with open("data.json", "r+") as file:
            countries = json.load(file)
            
            def add_country(data):
                print("Add: ")
                Name = input("Name: ")
                Area = int(input("Area: "))
                Population = int(input("Population: "))
                Continent = input("Continent: ")
                data.append({
                    "Name": Name,
                    "area": Area,
                    "population": Population,
                    "continent": Continent
                })
                return data
            
            countries = add_country(countries)
            file.seek(0)
            json.dump(countries, file, indent=4)
            file.truncate()

    elif command == "2":
        with open("data.json", "r") as file:
            countries = json.load(file)
            print(*countries, sep='\n')

    elif command == "3":
        with open("data.json", "r") as file:
            countries = json.load(file)
            for country in countries:
                if country["continent"] in ["Asia", "Africa"]:
                    print(country)

    elif command == "4":
        break

    else:
        print("Incorrect command!")
