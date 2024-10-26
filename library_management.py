from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)  # Khởi tạo ứng dụng Flask

def connect_db():
    connection = mysql.connector.connect(
        host='localhost',        # Địa chỉ máy chủ
        user='your_username',    # Tên người dùng
        password='your_password', # Mật khẩu
        database='library_db'    # Tên cơ sở dữ liệu
    )
    return connection

# Tạo bảng cho sách và thành viên
def create_tables():
    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        date_of_birth DATE NOT NULL,
        address VARCHAR(255) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        year INT NOT NULL
    )
    ''')
    
    connection.commit()
    connection.close()

# Thêm sách
def add_book(title, author, year):
    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute('''
    INSERT INTO books (title, author, year) VALUES (%s, %s, %s)
    ''', (title, author, year))
    
    connection.commit()
    connection.close()
    print("Sách đã được thêm thành công.")

# Thêm thành viên
def add_member(name, date_of_birth, address):
    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute('''
    INSERT INTO members (name, date_of_birth, address) VALUES (%s, %s, %s)
    ''', (name, date_of_birth, address))
    
    connection.commit()
    connection.close()
    print("Thành viên đã được thêm thành công.")

# Tạo route cho trang chính
@app.route('/')
def index():
    connection = connect_db()
    cursor = connection.cursor()

    # Lấy danh sách sách
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()

    # Lấy danh sách thành viên
    cursor.execute('SELECT * FROM members')
    members = cursor.fetchall()

    connection.close()
    return render_template('index.html', books=books, members=members)

# Hàm chính để chạy chương trình
def main():
    create_tables()  # Tạo bảng nếu chưa tồn tại
    
    # Thêm sách và thành viên
    add_book('Python Cơ Bản', 'Nguyễn Văn A', 2021)
    add_book('Lập Trình C++', 'Trần Thị B', 2020)
    
    add_member('Lê Văn C', '2000-01-01', 'Hà Nội')
    add_member('Trần Thị D', '1995-05-10', 'TPHCM')

if __name__ == '__main__':
    main()  # Chạy hàm tạo bảng và thêm dữ liệu
    app.run(debug=True)  # Chạy ứng dụng Flask
