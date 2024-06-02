import sqlite3

def initialize_database():
    # Connect to SQLite
    connection = sqlite3.connect("book.db")
    
    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()
    
    # Create the table
    table_info = """ 
    CREATE TABLE IF NOT EXISTS BOOK(
        NAME VARCHAR(100), 
        GENRE VARCHAR(25),
        AUTHOR VARCHAR(100), 
        PAGES INT
    );
    """
    cursor.execute(table_info)
    
    # Insert some records into the table
    books = [
        ('Atomic Habits', 'Self-Help', 'James Clear', 320),
        ('Pride and Prejudice', 'Romance', 'Jane Austen', 328),
        ('Angels & Demons', 'Mystery', 'Dan Brown', 768),
        ("Gulliver's Travels", 'Satire', 'Jonathan Swift', 336),
        ('Wings of Fire', 'Autobiography', 'APJ Abdul Kalam', 180)
    ]
    
    cursor.executemany('INSERT INTO BOOK VALUES (?, ?, ?, ?)', books)
    
    # Display all the records
    print("The inserted records are: ")
    
    data = cursor.execute('SELECT * FROM BOOK')
    
    for row in data:
        print(row)
    
    # Commit the transaction
    connection.commit()
    
    # Close the connection
    connection.close()

if __name__ == '__main__':
    initialize_database()
