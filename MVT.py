from abc import ABC, abstractmethod

# Model class to manage books
class BooksModel:
    def __init__(self):
        self.books = []

    # Add a new book to the list
    def add_book(self, book):
        self.books.append(book)

    # Get the list of books
    def get_books(self):
        return self.books

# View class to render book information
class BooksView:
    def __init__(self, model):
        self.model = model

    # Render books using the specified template
    def render(self, template):
        books = self.model.get_books()
        return template.render(books)

# Abstract class for book templates
class BooksTemplate(ABC):
    @abstractmethod
    def render(self, books):
        pass

# Template class to render books in a table format
class BooksTemplateTable(BooksTemplate):
    def render(self, books):
        result = "\n&&&&&&&&&&&&&&&&&&&&&&&&&\n"
        result += "\n".join(books) # This was missing the '+=' operator
        result += "\n&&&&&&&&&&&&&&&&&&&&&&&&&\n"
        return result

# Template class to render books in a simple format
class BooksTemplateSimple(BooksTemplate):
    def render(self, books):
        result = " ".join(books)
        return result

# Function to display the user menu and capture choice
def show_menu():
    print("*************************")
    print("1 - Add book")
    print("2 - Show books in table style")
    print("3 - Show books in simple style")
    print("4 - Exit")
    result = int(input("Choose what to do:\n"))
    print("*************************")
    return result

# Initialize the Model-View-Template components
obj_model = BooksModel()
obj_view = BooksView(obj_model)
obj_table = BooksTemplateTable()
obj_simple = BooksTemplateSimple()

# Main loop to interact with the user
while True:
    # Get user choice from the menu
    result = show_menu()

    # Perform action based on user choice
    match result:
        case 1:
            new_book = input("Enter a book to add: ")
            obj_model.add_book(new_book)
        case 2:
            print(obj_view.render(obj_table))
        case 3:
            print(obj_view.render(obj_simple))
        case 4:
            print("Bye!")
            break
        case _:
            print("\nWrong choice. Try again!\n")