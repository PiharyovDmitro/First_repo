import re

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        if not re.match(r'^\d{10}$', self.value):
            raise ValueError("Invalid phone number format")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                p.validate()
                break

    def find_phone(self, phone):
        return [p for p in self.phones if p.value == phone]

class AddressBook:
    def __init__(self):
        self.data = []

    def add_record(self, record):
        self.data.append(record)

    def find(self, name):
        return [record for record in self.data if record.name.value == name]

    def delete(self, name):
        self.data = [record for record in self.data if record.name.value != name]


# Приклад використання
if __name__ == "__main__":
    address_book = AddressBook()

    # Додавання записів
    record1 = Record("John Doe")
    record1.add_phone("1234567890")
    address_book.add_record(record1)

    record2 = Record("Jane Smith")
    record2.add_phone("9876543210")
    record2.add_phone("5554443333")
    address_book.add_record(record2)

    # Пошук записів за іменем
    search_result = address_book.find("John Doe")
    for record in search_result:
        print("Name:", record.name.value)
        print("Phones:", [phone.value for phone in record.phones])

    # Видалення записів за іменем
    address_book.delete("Jane Smith")
