book_library : dict = {
    "Physics":{
        "Author":"Einstein",
        "Publish_year":"1956",
        "Available":True
    },
    "Math":{
        "Author":"Muhammad ibn Musa al-Khwarizmi",
        "Publish_year":"1862",
        "Available":True
    },
    "Chemistry":{
        "Author":"Jabir ibn Hayyan",
        "Publish_year":"1555",
        "Available":True
    },
    "English":{
        "Author":"MR.chips",
        "Publish_year":"2023",
        "Available":False
    },
}
returned_books = []
borrowed_books = []



def view_books():
   for name, book_details in book_library.items():
    author = book_details["Author"]
    year = book_details["Publish_year"]
    available = book_details["Available"]
    print(f"book_name:\t{name.capitalize()},\nAuthor:\t\t{author},\nPublish_year:\t{year},\nAvailable:\t{available}")
def borrow_book():
  book_name = input("enter the book name you want to borrow:").capitalize()
  if book_name in book_library:
    if book_library[book_name]["Available"] == True:
      borrowed_books.append(book_name)
    else:
      print("book is not available")
  else:
    print("book not found")

def add_new_book():
  user_want_to_add_book = int(input("how many books you want to add:"))
  for i in range(user_want_to_add_book):
    book_name = input("enter the book name:").capitalize()
    author = input("enter the author name:")
    publish_year = input("enter the publish year:")
    book_library[book_name] = {
        "Author":author,
        "Publish_year":publish_year,
        "Available":True
    }

def return_book():
  user_want_to_return_book = int(input("how many books you want to return:"))
  for i in range(user_want_to_return_book):
    return_book_name = input("enter the book name:").capitalize()
    returned_books.append(return_book_name)
  print(f"return book:\t{returned_books}")

while True:
  print("""
1.View all books
2.Borrow a book (check if available)
3.Return a book
4.Add a new book
5.View borrowed books
6.Exit
""")
  user_input = int(input("enter the number:"))
  if user_input == 1:
    view_books()
  elif user_input == 2:
    borrow_book()
  elif user_input == 3:
    return_book()
  elif user_input == 4:
    add_new_book()
  elif user_input == 5:
    print(borrowed_books)
  elif user_input == 6:
    print("exit")
    break
  else:
    print("invalid input")
