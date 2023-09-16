"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():

    with open('referat.txt', encoding='utf-8') as file:
        content = file.read()
        content_in_one_string = content.replace('\n', '')
        print(f"Длина строки: {len(content_in_one_string)}")
        print(f"Кол-во слов: {len(content_in_one_string.split(' '))}")

        new_content = content.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as file_2:
        file_2.write(new_content)


if __name__ == "__main__":
    main()
