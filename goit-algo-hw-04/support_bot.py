#словарь для зберігання контактів
contacts = {}

#функція додавання контакту
def add_contact(name, phone):
    contacts[name] = phone
    return 'Contact added.'

#функция зміни номеру
def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return 'Contact updated.'
    else:
        return f'Contact with {name} not found.'

#функція виводу номера телефона за ім'ям
def show_phone(name):
    if name in contacts:
        return contacts[name]
    else:
        return f'Contact with {name} not found.'

#функція виведення усіх контактів
def show_all_contacts():
    if contacts:
        all_contacts = 'All contacts:\n'
        for name, phone in contacts.items():
            all_contacts += f'{name}: {phone}\n'
        return all_contacts
    else:
        return 'No contacts saved.'

    

    
