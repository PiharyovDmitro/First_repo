def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": int(cat_data[2])
                }
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as e:
        print("Помилка при обробці файлу:", e)
    
    return cats_info

# Приклад виклику функції:
cats = get_cats_info("cats.txt")
print(cats)
