contacts = {}

# Декоратор для обробки помилок введення
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Contact not found."

    return wrapper

#функція додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#функция зміни номеру
@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return 'Contact updated.'
    else:
        return f'Contact with {name} not found.'

#функція виводу номера телефона за ім'ям
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f'Contact with {name} not found.'

#функція виведення усіх контактів
@input_error
def show_all_contacts(contacts):
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
            if len(args) != 2:
                print("Give me name and phone please")
                continue
            print(add_contact(args, contacts))
        elif command == 'change':
            if len(args) != 2:
                print("Give me name and new phone please")
                continue
            print(change_contact(args, contacts))
        elif command == 'phone':
            if len(args) != 1:
                print("Enter user name")
                continue
            print(show_phone(args, contacts))
        elif command == 'all':
            if len(args) != 0:
                print("Invalid arguments. Usage: all")
                continue
            print(show_all_contacts(contacts))
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()