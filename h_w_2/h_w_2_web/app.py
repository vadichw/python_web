from datetime import datetime
from abstract_view import ConsoleView
from record import Record
from address_book import AddressBook


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
