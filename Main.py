# mini library system project

my_books = []
# adding some default books
my_books.append({"id": "1", "title": "harry potter", "writer": "jk rowling", "taken": False})
my_books.append({"id": "2", "title": "rich dad poor dad", "writer": "robert kiyosaki", "taken": False})
my_books.append({"id": "3", "title": "atomic habits", "writer": "james clear", "taken": False})
my_books.append({"id": "4", "title": "Freedom From Known", "writer": "J. Krishnamurti", "taken": False})
my_books.append({"id": "5", "title": "Thus Spoke Zarathustra", "writer": "Fredrick Neitzsche", "taken": False})
my_books.append({"id": "6", "title": "Crime and Punishment", "writer": "Fydoor Dostoevsky", "taken": False})
my_books.append({"id": "7", "title": "Fame,Fortune and Success", "writer": "Osho", "taken": False})
my_books.append({"id": "8", "title": "Critics of Pure Reason", "writer": "Immanuel Kant", "taken": False})
my_books.append({"id": "9", "title": "Meatmorphosis", "writer": "Franz Kafka", "taken": False})
my_books.append({"id": "10", "title": "The Stranger", "writer": "Albert Camus", "taken": False})





run = True

while run == True:
    print("\n--- WELCOME TO LIBRARY ---")
    print("1. see all books")
    print("2. add a new book")
    print("3. find book")
    print("4. issue a book")
    print("5. return a book")
    print("6. exit")
    
    ch = input("enter ur choice: ")
    
    if ch == '1':
        print("\nList of books:")
        for b in my_books:
            if b["taken"] == False:
                st = "Available"
            else:
                st = "Issued"
            print(b["id"], "-", b["title"], "by", b["writer"], "(", st, ")")
            
    elif ch == '2':
        b_id = input("enter book id: ")
        b_name = input("enter book name: ")
        b_auth = input("enter author: ")
        
        # save to our list
        my_books.append({"id": b_id, "title": b_name, "writer": b_auth, "taken": False})
        print("book added !!")
        
    elif ch == '3':
        name = input("type book name to search: ")
        found = 0
        
        for b in my_books:
            if name in b["title"]:
                print("Book found! ID is", b["id"], "and name is", b["title"])
                found = 1
                
        if found == 0:
            print("sorry book not found")
            
    elif ch == '4':
        req_id = input("enter id to issue: ")
        check = 0
        
        for b in my_books:
            if b["id"] == req_id:
                check = 1
                if b["taken"] == True:
                    print("someone already took this book")
                else:
                    b["taken"] = True
                    print("book issued to u")
                    
        if check == 0:
            print("wrong id")
            
    elif ch == '5':
        ret_id = input("enter id to return: ")
        check2 = 0
        
        for b in my_books:
            if b["id"] == ret_id:
                check2 = 1
                if b["taken"] == False:
                    print("this book is already in library")
                else:
                    b["taken"] = False
                    print("book returned safely")
                    
        if check2 == 0:
            print("wrong id")
            
    elif ch == '6':
        print("bye bye")
        run = False
        
    else:
        print("wrong option try again")