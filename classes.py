from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        if len(phone) != 10:
            raise ValueError("Phone number must have 10 digits.")
        super().__init__(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return self.phones

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        return self.phones

    def edit_phone(self, phone, new_phone):
        if phone in self.phones:
            index = self.phones.index(phone)
            self.phones[index] = new_phone
        return self.phones

    def find_phone(self, phone):
        if phone in self.phones:
            return phone
        else:
            return "This phone is not in the contact list."

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.book_list = []

    def add_record(self, name, phone):
        record_data = {
            "Contact name": Record(name),
            "phones": Record(phone)
        }
        self.book_list.append(record_data)

    def find(self, name):
        for user in self.book_list:
            if name in user:
                return user
            else:
                return "User was not found."

    def delete(self, name):
        for user in self.book_list:
            if name in user:
                self.book_list.remove(user)
                return self.book_list
