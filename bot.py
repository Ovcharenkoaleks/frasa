import json

def load_phrases():
    # Убедимся, что файл phrases.json находится в той же папке
    try:
        with open('phrases.json', 'r', encoding='utf-8') as file:
            data = json.load(file)  # Загружаем содержимое файла в переменную
        return data['phrases']  # Возвращаем список фраз
    except FileNotFoundError:
        print("Файл 'phrases.json' не найден.")
    except json.JSONDecodeError:
        print("Ошибка при чтении JSON. Проверьте структуру файла.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

phrases = load_phrases()  # Загрузим фразы

if phrases:
    print("Фразы загружены успешно!")
    print(phrases)  # Выведем фразы для проверки
else:
    print("Не удалось загрузить фразы.")
