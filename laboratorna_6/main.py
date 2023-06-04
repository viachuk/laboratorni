import math

# Функція для розрахунку оцінки (E) та стандартного відхилення (SD) для кожного завдання
def calculate_task_scores(a, m, b):
    E = (a + 4 * m + b) / 6
    SD = (b - a) / 6
    return E, SD

# Запитуємо користувача про оцінки завдань
a = float(input("Введіть оцінку a: "))
m = float(input("Введіть оцінку m: "))
b = float(input("Введіть оцінку b: "))

# Розраховуємо оцінку (E) та стандартне відхилення (SD) для кожного завдання
E_task, SD_task = calculate_task_scores(a, m, b)

# Розраховуємо оцінку (E) та стандартне відхилення (SE) для проекту
E_project = E_task
SE_project = math.sqrt(sum([SD_task**2 for _ in range(3)])) / math.sqrt(3)

# Розраховуємо 95% довірчий інтервал (CI) для проекту
CI_min = E_project - 2 * SE_project
CI_max = E_project + 2 * SE_project

# Виводимо результат
print("Project's 95% confidence interval: {:.2f} ... {:.2f} points".format(CI_min, CI_max))
