from collections import UserDict
import pickle

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
    
    