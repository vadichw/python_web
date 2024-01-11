from datetime import datetime
from field import Name, Phone

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