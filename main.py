from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)
    # реалізація класу

class Phone(Field):
    def __init__(self, phone_number):
        if phone_number.isnumeric() and len(phone_number) == 10:
            super().__init__(phone_number)
        else:
            raise ValueError('Phone is not valid')
    # реалізація класу

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        valid_number = Phone(phone_number)
        if not valid_number is None:
            self.phones.append(valid_number)
        else:
            return 'Phone is not valid'
        
    def remove_phone(self, phone_number):
        valid_number = Phone(phone_number)
        self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        valid_number = Phone(old_phone_number)
        if bool(Phone(new_phone_number)):
            if valid_number is self.phones:
                self.phones.replace(old_phone_number, new_phone_number)
            else:
                raise ValueError('Phone not found')
        else:
            raise ValueError('Phone not found')

    def find_phone(self, phone):
        valid_number = Phone(phone)
        for ph in self.phones:
            if ph.value == valid_number.value:
                return ph
    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        if isinstance(record, Record):
            self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Not found")