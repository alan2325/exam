l = [
    {"id": 1, "name": "Spider-Man: Into the Spider-Verse", "auth": "Brian Michael Bendis", "dis": "A story about multiple Spider-Men across different universes."},
    {"id": 2, "name": "Batman: The Killing Joke", "auth": "Alan Moore", "dis": "An exploration of the Joker's origin story."},
    {"id": 3, "name": "X-Men: Days of Future Past", "auth": "Chris Claremont", "dis": "A dystopian future where mutants are hunted by Sentinels."}
]

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    ch = get_int_input('1. View details\n2. Add\n3. Update\n4. Search\n5. Remove\n6. Exit\nEnter your choice: ')

    if ch == 1:
        if not l:
            print("No books available.")
        else:
            print(f"{'ID':<5} {'Name':<40} {'Author':<25} {'Description':<50}")
            print("-" * 150)
            for book in l:
                print(f"{book['id']:<5} {book['name']:<40} {book['auth']:<25} {book['dis']:<50}")
                print()

    elif ch == 2:
        id = get_int_input("Enter ID of the book: ")
        name = input("Enter book name: ")
        auth = input("Enter author name: ")
        dis = input("Enter description: ")

        if any(book["id"] == id for book in l):
            print("Book already exists!")
        else:
            l.append({"id": id, "name": name, "auth": auth, "dis": dis})
            print("Book added successfully!")

    elif ch == 3:
        while True:
            old_id = get_int_input("Enter 0 to cancel!\nEnter the book ID needed to update: ")
            if old_id == 0:
                break
            
            found = False
            for book in l:
                if book["id"] == old_id:
                    new_name = input("Enter new name: ")
                    new_auth = input("Enter new author: ")
                    new_dis = input("Enter new description: ")
                    book.update({"name": new_name, "auth": new_auth, "dis": new_dis})
                    print("Book updated successfully!")
                    found = True
                    break
            
            if found:
                break  
            else:
                print("Book not found! Please try again.")

    elif ch == 4:
        while True:
            opt = get_int_input("Enter 0 to cancel!\n1. Search by ID\n2. Search by Name\n3. Search by Author\nEnter choice: ")
            if opt == 0:
                break
            
            found = False
            if opt == 1:
                sid = get_int_input("Enter ID to find: ")
                for book in l:
                    if book["id"] == sid:
                        print(f"{'ID':<5} {'Name':<40} {'Author':<25} {'Description':<50}")
                        print("-" * 150)
                        print(f"{book['id']:<5} {book['name']:<40} {book['auth']:<25} {book['dis']:<50}")
                        found = True
                        break

            elif opt == 2:
                sname = input("Enter book name to find: ")
                for book in l:
                    if book["name"].lower() == sname.lower():
                        print(f"{'ID':<5} {'Name':<40} {'Author':<25} {'Description':<50}")
                        print("-" * 150)
                        print(f"{book['id']:<5} {book['name']:<40} {book['auth']:<25} {book['dis']:<50}")
                        found = True
                        break

            elif opt == 3:
                sauth = input("Enter author to find: ")
                for book in l:
                    if book["auth"].lower() == sauth.lower():
                        print(f"{'ID':<5} {'Name':<40} {'Author':<25} {'Description':<50}")
                        print("-" * 150)
                        print(f"{book['id']:<5} {book['name']:<40} {book['auth']:<25} {book['dis']:<50}")
                        found = True
                        break

            if not found:
                print("No matching book found! Please try again.")

    elif ch == 5:
        rem_id = get_int_input("Enter 0 to cancel!\nEnter the ID of the book to remove: ")
        if rem_id == 0:
            continue 
        
        for i in range(len(l)):
            if l[i]["id"] == rem_id:
                l.pop(i)
                print("Book removed successfully!")
                break
        else:
            print("Book not found!")

    elif ch == 6:
        print("You have exited.")
        break

    else:
        print("Invalid Input!")
