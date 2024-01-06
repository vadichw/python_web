from datetime import datetime
from collections import UserDict
import pickle
from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def display(self, data):
        pass


class ConsoleView(View):

    def display(self, data):
        for item in data:
            print(item)


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value

    def validate(self, value):
        pass

    def __str__(self):
        return str(self._value)


class Name(Field):
    pass


class Phone(Field):
    def validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.birthday = birthday
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            phone_to_edit.value = new_phone
        else:
            raise ValueError(f"Phone {old_phone} not found in record")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = datetime.now()
        current_birthday = datetime(today.year, self.birthday.month, self.birthday.day)
        if current_birthday < today:
            current_birthday = current_birthday.replace(year=today.year + 1)
        return (current_birthday - today).days

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}{birthday_str}, phones: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterator(self, n=5):
        records = list(self.data.values())
        for i in range(0, len(records), n):
            yield records[i:i + n]

    def save_to_file(self, filename="address_book.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.data, file)

    def load_from_file(self, filename="address_book.pkl"):
        try:
            with open(filename, "rb") as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            print("Файл з адресною книгою не знайдено.")

    def search(self, query):
        return [record for record in self.data.values() if
                query.lower() in record.name.value.lower() or any(query in phone.value for phone in record.phones)]


class AddressBookApp:

    def __init__(self, view):
        self.book = AddressBook()
        self.view = view

    def run(self):
        record1 = Record("Vadim", datetime.strptime("2001-09-04", "%Y-%m-%d"))
        record1.add_phone("1234567890")
        record2 = Record("Vika", datetime.strptime("2002-05-14", "%Y-%m-%d"))
        record2.add_phone("0987654321")
        self.book.add_record(record1)
        self.book.add_record(record2)


        self.book.save_to_file("address_book.pkl")


        self.book.load_from_file("address_book.pkl")


        search_results = self.book.search("o")
        self.view.display(search_results)

        search_results = self.book.search("h")
        self.view.display(search_results)


if __name__ == "__main__":
    console_view = ConsoleView()
    app = AddressBookApp(console_view)
    app.run()
