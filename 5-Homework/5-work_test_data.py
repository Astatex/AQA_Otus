import csv
import json

# Загрузка пользователей
with open("users.json", "r") as json_file:
    users = json.load(json_file)

books = []
with open("books.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        books.append(
            {
                "title": row["Title"],
                "author": row["Author"],
                "pages": int(row["Pages"]),
                "genre": row["Genre"],
            }
        )

# распределение книг
base = len(books) // len(users)
extra = len(books) % len(users)

# финальный список
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
            "books": books[book_index: book_index + count],
        }
    )


# запись результата
with open("result.json", "w") as result_files:
    json.dump(result, result_files, indent=2)

print(f"Распределено {len(books)} книг между {len(users)} пользователями.")
print("Результат сохранён в result.json")
