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

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    print("Welcome to the assistant bot!")
    print("Available commands:\nhello - greet\nadd [name] [phone] - add a contact\nchange [name] [new phone] - update a contact\nphone [name] - show phone number\nall - show all contacts\nclose or exit - close the bot")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == 'add':
            print(add_contact(*args))
        elif command == 'change':
            print(change_contact(*args))
        elif command == 'phone':
            print(show_phone(*args))
        elif command == 'all':
            print(show_all_contacts())
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
