from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return str(self.value)

class FirstName(Field):
    pass

class LastName(Field):
    pass

class Email(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, first_name, last_name, email = None, phones = None):
        self.first_name = FirstName(first_name)
        self.last_name = LastName(last_name)
        self.email = Email(email)
        self.phones = []
        
        if phones is not None:
            for phone in phones:
                self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = Phone(new_phone)

class AddressBook(UserDict):
    def add_record(self, record: Record):
        key = record.first_name.value
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(record)