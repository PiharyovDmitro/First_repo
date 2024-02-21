import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def visualize_directory_structure(directory_path, indent=0, is_last=False):

    directory = Path(directory_path)

    # Перевірка чи існує заданий шлях і чи є це директорія
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + "Помилка: Заданий шлях не існує або не є директорією.")
        return

    # Виведення імені поточної директорії
    print(Fore.BLUE + '    ' * indent + ('└── ' if is_last else '├── ') + f'{directory.name}/')

    # Отримання списку файлів та директорій у поточній директорії
    items = list(directory.iterdir())
    # Позначаємо поточну директорію як останню, якщо це останній елемент списку
    for index, item in enumerate(items[:-1]):
        if item.is_file():
            print(Fore.GREEN + '    ' * (indent + 1) + '├── ' + f'📄 {item.name} ({item.absolute()})')
        elif item.is_dir():
            print(Fore.CYAN + '    ' * (indent + 1) + '├── ' + f'📁 {item.name}/ ({item.absolute()})')
            visualize_directory_structure(item, indent + 1)
    # Викликаємо рекурсію для останнього елементу списку, позначаючи його як останній
    if items:
        item = items[-1]
        if item.is_file():
            print(Fore.GREEN + '    ' * (indent + 1) + '└── ' + f'📄 {item.name} ({item.absolute()})')
        elif item.is_dir():
            print(Fore.CYAN + '    ' * (indent + 1) + '└── ' + f'📁 {item.name}/ ({item.absolute()})')
            visualize_directory_structure(item, indent + 1, is_last=True)

if __name__ == "__main__":
    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: Будь ласка, введіть шлях до директорії як аргумент командного рядка.")
        sys.exit(1)

    # Отримання шляху до директорії з аргументів командного рядка
    directory_path = sys.argv[1]

    # Виклик функції для візуалізації структури директорії
    visualize_directory_structure(directory_path)