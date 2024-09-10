import csv


try:
    csvfile = open("D:\\все\\уник\\Python\\Лаба 11\\gdp_per_capita.csv", "r")

    reader = csv.DictReader(csvfile, delimiter = ",")

    print("Countries 2016: ")

    for row in reader:
        print(row["Country Name"], ': ', row["2016"])

    csvfile.seek(0)
    
    min_gpd = float(input("Введіть мінімальне значення GDP для пошуку: "))

    try:
        
        filtered_csvfile = open("D:\\все\\уник\\Python\\Лаба 11\\filtered_gpd_per_capita.csv", "w")
        writer = csv.DictWriter(filtered_csvfile, reader.fieldnames)
        writer.writeheader()

        print("Результат: ")
        
        for row in reader:
            if row["2016"] == "":
                continue
            elif float(row["2016"]) > min_gpd:
                print(row["Country Name"], ': ', row["2016"])
                writer.writerow(row)
         

        print("Відфільтровані дані було успішно записано у файл filtered_gpd_per_capita.csv ! ")
    except FileNotFoundError:
        print("Файл filtered_gpd_per_capita.csv не знайдено!")

except FileNotFoundError:
    print("Файл gdp_per_capita.csv не знайдено!")
    
except Exception as e:
    print(f"Помилка у виконанні програми {e}")

