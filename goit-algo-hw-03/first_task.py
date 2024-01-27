from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        days_difference = (input_date - current_date).days
        
        return days_difference
    except ValueError:
        print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'")
        return None


# Приклад виклику функції
today = "2024-01-27"  # поточна дата для прикладу
result = get_days_from_today("2021-10-09")

if result is not None:
    print(f"Кількість днів між {today} та 2021-10-09: {result}")
