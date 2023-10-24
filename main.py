import locale
import string


def is_ukrainian_word(word):
    # Перевірка, чи містить слово хоча б одну букву із українського алфавіту
    ukrainian_letters = set('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
    return any(letter in ukrainian_letters for letter in word.lower())


def read_and_sort_words(filename):
    try:
        locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
        # Встановлення локалі для українського алфавіту

        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            # Вивести перше речення
            first_sentence = text.split('.')[0] + '.'
            print(first_sentence)

            # Створити список слів без знаків пунктуації та перетворити їх до маленьких літер
            words = text.split()

            # Створення таблиці для видалення пунктуації
            translator = str.maketrans('', '', string.punctuation)

            # Видалення пунктуації та перетворення до маленьких літер
            clean_words = [word.translate(translator).lower() for word in words]

            # Розділити слова на українські та англійські, а потім відсортувати їх окремо
            ukrainian_words = sorted([word for word in clean_words if is_ukrainian_word(word)], key=locale.strxfrm)
            english_words = sorted([word for word in clean_words if not is_ukrainian_word(word)])


            # Вивести українські слова, а потім англійські
            print("Українські слова по алфавіту:")
            print(ukrainian_words + english_words)

            print("Довжина тексту")
            print(f"{len(ukrainian_words) + len(english_words)}")


    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    read_and_sort_words('text.txt')
