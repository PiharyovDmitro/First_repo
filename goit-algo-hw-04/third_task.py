import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для підтримки кольорового виведення
init(autoreset=True)

def visualize_directory_structure(directory_path, indent=0):
    """
    Функція для візуалізації структури директорії з використанням кольорів.
    :param directory_path: Шлях до директорії
    :param indent: Відступ для форматування виводу
    """
    directory = Path(directory_path)

    # Перевірка чи існує заданий шлях і чи є це директорія
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + "Помилка: Заданий шлях не існує або не є директорією.")
        return

    # Виведення імені поточної директорії
    print(Fore.BLUE + '    ' * indent + f'{directory.name}/')

    # Обробка файлів у директорії
    for item in directory.iterdir():
        if item.is_file():
            print(Fore.GREEN + '    ' * (indent + 1) + f'{item.name}')
        elif item.is_dir():
            # Виведення імені директорії та рекурсивний виклик для її структури
            visualize_directory_structure(item, indent + 1)

if __name__ == "__main__":
    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: Будь ласка, введіть шлях до директорії як аргумент командного рядка.")
        sys.exit(1)

    # Отримання шляху до директорії з аргументів командного рядка
    directory_path = sys.argv[1]

    # Виклик функції для візуалізації структури директорії
    visualize_directory_structure(directory_path)
