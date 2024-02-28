import sys
import re
from collections import Counter

def parse_log_line(line: str) -> dict:
    """Парсинг рядка логу."""
    match = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$', line)
    if match:
        return {'timestamp': match.group(1), 'level': match.group(2), 'message': match.group(3)}
    else:
        return None

def load_logs(file_path: str) -> list:
    """Завантаження логів з файлу."""
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрація логів за рівнем."""
    return [log for log in logs if parse_log_line(log)['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    """Підрахунок логів за рівнями логування."""
    levels = [parse_log_line(log)['level'] for log in logs]
    return dict(Counter(levels))

def display_log_counts(counts: dict):
    """Виведення результатів."""
    print("Рівень логування | Кількість")
    print("-" * 30)
    for level, count in counts.items():
        print(f"{level:<17} | {count}")
    print("-" * 30)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Не вказано шлях до файлу логів.")
        sys.exit(1)
    
    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    
    if len(sys.argv) == 3:
        log_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, log_level.upper())
        counts = count_logs_by_level(filtered_logs)
        display_log_counts(counts)
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)