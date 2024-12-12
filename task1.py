class Publication:
    def __init__(self,name):
        self.name = name

    def info(self):
        print(f"Name: {self.name}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        self.page_count = page_count
        self.author = author
        super().__init__(name)
    def print_information(self):
        super().info()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}\n")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)
    def print_information(self):
        super().info()
        print(f"Chief Editor: {self.chief_editor}\n")

publications = []
publications.append(Magazine("Donald Duck", "Aki Hyyppä"))
publications.append(Book("Compartment No. 6", "Rosa Liksom", 192))

for p in publications:
    p.print_information()