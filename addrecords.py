import sqlite3

# Connect to SQLite
connection = sqlite3.connect("book.db")

# Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

# Insert some records into the table
cursor.execute('''INSERT INTO BOOK VALUES("The Hitchhiker's Guide to the Galaxy",
 'Science Fiction Comedy', 'Douglas Adams', 224)''')
cursor.execute('''INSERT INTO BOOK VALUES('To Kill a Mockingbird', 
'Coming-of-Age', 'Harper Lee', 320)''')
cursor.execute('''INSERT INTO BOOK VALUES('One Hundred Years of Solitude',
 'Magical Realism', 'Gabriel Garcia Marquez', 464)''')
cursor.execute('''INSERT INTO BOOK VALUES('The Power of Now', 
'Self-Help', 'Eckhart Tolle', 224)''')
cursor.execute('''INSERT INTO BOOK VALUES('Murder on the Orient Express',
 'Mystery', 'Agatha Christie', 304)''')
cursor.execute('''INSERT INTO BOOK VALUES('Daring Greatly',
 'Self-Help', 'Brené Brown', 336)''') 
cursor.execute('''INSERT INTO BOOK VALUES('The Love Hypothesis',
 'Romance', 'Ali Hazelwood', 384)''')
cursor.execute('''INSERT INTO BOOK VALUES('1984', 'Dystopian Fiction', 'George Orwell', 328)''')
cursor.execute('''INSERT INTO BOOK VALUES('The Catcher in the Rye', 'Bildungsroman', 'J.D. Salinger', 224)''')
cursor.execute('''INSERT INTO BOOK VALUES('The Great Gatsby', 'Tragedy', 'F. Scott Fitzgerald', 180)''')
cursor.execute('''INSERT INTO BOOK VALUES('Lord of the Rings', 'Fantasy', 'J.R.R. Tolkien', 1178)''')
cursor.execute('''INSERT INTO BOOK VALUES('The Alchemist', 'Philosophical Fiction', 'Paulo Coelho', 208)''')
cursor.execute('''INSERT INTO BOOK VALUES('Sapiens: A Brief History of Humankind', 'Non-Fiction', 'Yuval Noah Harari', 464)''')
cursor.execute('''INSERT INTO BOOK VALUES('The Da Vinci Code', 'Mystery Thriller', 'Dan Brown', 454)''')
cursor.execute('''INSERT INTO BOOK VALUES("Harry Potter and the Philosopher's Stone", 'Fantasy', 'J.K. Rowling', 336)''')


# Display all the records
print("The inserted records are: ")

data = cursor.execute('''SELECT * FROM book''')

for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close