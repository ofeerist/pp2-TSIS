import psycopg2
import csv
import re

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone_number VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()

def insert_from_csv():
    file_path = input("Enter CSV file path: ")
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("CSV data inserted successfully.")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Contact added.")

def insert_many():
    entries = int(input("How many contacts to insert? "))
    incorrect = []

    for _ in range(entries):
        name = input("Name: ")
        phone = input("Phone: ")
        if re.match(r'^\+?\d{10,15}$', phone):
            cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
            if cur.fetchone():
                cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (phone, name))
            else:
                cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
        else:
            incorrect.append((name, phone))

    conn.commit()
    if incorrect:
        print("Incorrect entries:")
        for item in incorrect:
            print(item)
    else:
        print("All contacts inserted successfully.")

def insert_or_update():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
    if cur.fetchone():
        cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (phone, name))
        print("Phone updated.")
    else:
        cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
        print("New contact added.")
    conn.commit()

def update_user():
    old_name = input("Enter the name of the user to update: ")
    update_name = input("Enter new name (or press Enter to skip): ")
    update_phone = input("Enter new phone number (or press Enter to skip): ")

    if update_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (update_name, old_name))
    if update_phone:
        cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (update_phone, update_name or old_name))
    conn.commit()
    print("Contact updated.")

def query_data():
    filter_type = input("Filter by (n)ame, (p)hone, or show (a)ll? ").lower()
    if filter_type == 'n':
        name = input("Enter name to search: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", ('%' + name + '%',))
    elif filter_type == 'p':
        phone = input("Enter phone number to search: ")
        cur.execute("SELECT * FROM phonebook WHERE phone_number = %s", (phone,))
    else:
        cur.execute("SELECT * FROM phonebook")
    results = cur.fetchall()
    for row in results:
        print(row)

def paginated_query():
    limit = int(input("Limit per page: "))
    offset = int(input("Offset: "))
    cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    results = cur.fetchall()
    for row in results:
        print(row)

def delete_user():
    choice = input("Delete by (n)ame or (p)hone? ").lower()
    if choice == 'n':
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    elif choice == 'p':
        phone = input("Enter phone number to delete: ")
        cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
    conn.commit()
    print("Contact deleted.")

def menu():
    create_table()
    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("--- Lab 11 ---")
        print("6. Insert or Update contact")
        print("7. Insert many contacts")
        print("8. Paginated query")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_user()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            insert_or_update()
        elif choice == '7':
            insert_many()
        elif choice == '8':
            paginated_query()
        elif choice == '9':
            break
        else:
            print("Invalid option.")

    cur.close()
    conn.close()

if __name__ == '__main__':
    menu()
