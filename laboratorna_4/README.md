import os

while True:
    file_path = input("Enter the path to the file: ")

    if not os.path.exists(file_path):
        print("File not found!")
        continue

    with open(file_path, 'r') as file:
        content = file.readlines()

    
    total_lines = len(content)
    empty_lines = content.count('\n')
    lines_with_h = sum('z' in line for line in content)
    h_count = sum(line.count('z') for line in content)
    lines_with_will = sum('and' in line for line in content)

    print(f"\nFile: {file_path}")
    print(f"total lines: {total_lines}")
    print(f"empty lines: {empty_lines}")
    print(f"lines with \"z\": {lines_with_h}")
    print(f"\"z\" count: {h_count}")
    print(f"lines with \"and\": {lines_with_will}")

    answer = input("Do you want to analyze another file? (y/n): ")
    if answer.lower() != 'y':
        break


Даний код виконує наступні дії:
1. import os: Цей рядок імпортує модуль os, який надає функції для взаємодії з операційною системою, зокрема для перевірки існування файлів та роботи з файловою системою.
2. while True:: Цей рядок починає безкінечний цикл, що дозволяє користувачеві аналізувати кілька файлів підряд.
3. file_path = input("Enter the path to the file: "): Користувачеві пропонується ввести шлях до файлу, який він хоче проаналізувати, і введений шлях зберігається у змінній file_path.
4. if not os.path.exists(file_path):: За допомогою os.path.exists(file_path) перевіряється, чи існує файл за вказаним шляхом. Якщо файл не знайдено, виводиться повідомлення "File not found!" і цикл повертається на початок.
5. with open(file_path, 'r') as file:: Відкривається файл за вказаним шляхом у режимі читання ('r'). with гарантує закриття файлу після завершення його використання.
6. content = file.readlines(): Зчитується вміст файлу і зберігається у змінній content. Кожен рядок файлу стає елементом списку content.
7. total_lines = len(content): Обчислюється загальна кількість рядків у файлі за допомогою функції len().
8. empty_lines = content.count('\n'): Рахується кількість порожніх рядків у файлі за допомогою методу count(). В даному випадку, \n представляє порожній рядок.
9. lines_with_h = sum('z' in line for line in content): Рахується кількість рядків, в яких зустрічається символ 'z', за допомогою генератора списку та функції sum().
10. `h_count = sum(line.count('z') for line in content): Обчислюється загальна кількість входжень символу 'z' у всі рядки файлу.
11. lines_with_will = sum('and' in line for line in content): Рахується кількість рядків, в яких зустрічається слово "and".

Виводяться результати аналізу, включаючи шлях до файлу, загальну кількість рядків, кількість порожніх рядків, кількість рядків з символом 'z', кількість входжень символу 'z' та кількість рядків зі словом "and".

answer = input("Do you want to analyze another file? (y/n): "): Користувачеві пропонується вибір продовження аналізування інших файлів. Введена відповідь зберігається у змінній answer.

if answer.lower() != 'y':: Якщо відповідь користувача не є 'y' (або 'Y'), цикл обривається і програма завершується.

Цей код дозволяє користувачеві аналізувати кілька файлів, підряд вводячи шлях до кожного файлу. Він виводить інформацію про загальну кількість рядків, порожніх рядків, кількість рядків з символом 'z', кількість входжень символу 'z' та кількість рядків зі словом "and" для кожного файлу.