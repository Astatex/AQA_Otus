import csv
import json

# Загрузка пользователей из файла users.json (в PR файла нет)
with open("users.json", "r") as users_data:
    users = json.load(users_data)

# Загрузка книг из файла books.csv (в PR файла нет)
books = []
with open("books.csv", "r") as books_data:
    reader = csv.DictReader(books_data)
    for row in reader:
        books.append(
            {
                "title": row["Title"],
                "author": row["Author"],
                "pages": int(row["Pages"]),
                "genre": row["Genre"],
            }
        )

# Распределение книг
num_users = len(users)
num_books = len(books)

base = num_books // num_users
extra = num_books % num_users

# Создание финального списка пользователей с книгами
result = []
book_index = 0
for i, user in enumerate(users):
    count = base + 1
    book_index += count
    result.append(
        {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": books[book_index : book_index + count],
        }
    )

# Сохранение результата в файле result.json
with open("result.json", "w") as result_data:
    json.dump(result, result_data, indent=2)

print(f"Распределено {num_books} книг между {num_users} пользователями.")
print("Результат сохранён в файле result.json")
