import random 

def get_numbers_ticket(minimum, maximum, quantity):

    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        return print('Ваші числа не відповідають вимогам.')
    
    unique_numbers = set()

    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(minimum, maximum))

    return sorted(list(unique_numbers))

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
