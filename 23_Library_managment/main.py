from .services.library_services import Services



library = Services()
library.load_members()
library.loads_books()                                   

print(library.books)


while True:
    choise = input("Enter the Choice...")

    if choise == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        book_id = input("Book ID: ")

        book = library.add_book(title , author , book_id)
        print(book)

    elif choise == "2":
        name = input("Member Name: ")
        member_id = input("Member ID: ")
        member = library.add_member(name, member_id)
        print(member)

    elif choise == "3":
        book_id = input("Book ID: ")
        member_id = input("Member ID: ")
        print(library.issue_book(book_id, member_id))
    
    elif choise == "4":
        book_id = input("Book ID: ")
        print(library.return_book(book_id))

    elif choise == "5":
        library.view_books()

    elif choise == "6":
        library.view_members()

    elif choise == "7":
        print("Exiting...")
        break

    else:
        print("Invalid option. Try again.")
