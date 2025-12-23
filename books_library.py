import random

book_list = ["Deitel-Java", "Wonder-woman","Super-man", "Thing-fall-apart"]

def sugest_book():
    if not book_list:
    print("Book not available at the momet")
    
    while True:
    book = random.choice(book_list)
    page = random.choice(1, 100)
    print("The book available today is ",book ," on page", page)

    next_round = input("Would you like to read another book? (yes/no)").lower()
    if next_round == "no":
        break
    

def add_book():
    new_book = input("Enter the book title: ").strip()

    if new_book in book_list:
        print("Book already exist in the library")
    else:
        book_list.append(new_book)
        print("Book added to library successfully")

    
def remove_book():
    title = input("Which book would you like to remove").strip()
    if title in book_lists:
        book_lists.remove(title)
        print("Book removed successfully!")
    else:
        print("Book not availbale!")

def update_book():  
    replace = input("Enter the title of the book you would like to replace:").strip()
    if replace in book_lists:
        new = input ("Enter the title of the book you want to replace")
        index = book_list.index(replace)
        book_lists[index] = new
        print("Replaced successfully")
    else:
        print("Book not found")



def main():
    while True:
        print""" Welcome to Book Suggestion
            1. Get suggestion
            2. Add book
            3. Remove book
            4. Update book
            5. Show all books
            6. Quit

        """

        choice = input("Select from the above options: ")
        if choice == 1:
            suggest_book()
        elif choice == 2:
            add_book()
        elif choice == 3:
            remove_book()
        elif choice == 4:
            update_book()
        elif choice == 5:
            show_books()
        elif choice == 6:
            break
        else:
            print("Invalid option, try again.")

main()
        
        
    
    
    

        

