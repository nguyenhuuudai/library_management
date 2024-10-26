import sqlite3

# Kết nối đến cơ sở dữ liệu
def connect_db():
    connection = sqlite3.connect('library.db')
    return connection

# Tạo bảng cho sách và thành viên
def create_tables():
    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date_of_birth DATE NOT NULL,
        address TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL
    )
    ''')
    
    connection.commit()
    connection.close()

# Thêm sách
def add_book(title, author, year):
    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute('''
    INSERT INTO books (title, author, year) VALUES (?, ?, ?)
    ''', (title, author, year))
    
    connection.commit()
    connection.close()
    print("Sách đã được thêm thành công.")

# Thêm thành viên
def add_member(name, date_of_birth, address):
    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute('''
    INSERT INTO members (name, date_of_birth, address) VALUES (?, ?, ?)
    ''', (name, date_of_birth, address))
    
    connection.commit()
    connection.close()
    print("Thành viên đã được thêm thành công.")

# Hàm chính để chạy chương trình
def main():
    create_tables()  # Tạo bảng nếu chưa tồn tại
    
    # Thêm sách và thành viên
    add_book('Python Cơ Bản', 'Nguyễn Văn A', 2021)
    add_book('Lập Trình C++', 'Trần Thị B', 2020)
    
    add_member('Lê Văn C', '2000-01-01', 'Hà Nội')
    add_member('Trần Thị D', '1995-05-10', 'TPHCM')

    # Lấy và in ra sách
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    print("Danh sách sách trong thư viện:")
    for book in books:
        print(book)

    # Lấy và in ra thành viên
    cursor.execute('SELECT * FROM members')
    members = cursor.fetchall()
    print("Danh sách thành viên trong thư viện:")
    for member in members:
        print(member)
    
    connection.close()

if __name__ == '__main__':
    main()
