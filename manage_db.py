import sqlite3



def create_db():
    conn = sqlite3.connect('Data.db')

    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expense_limit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        limit_expense INTEGER NOT NULL,
        count_expenses INTEGER NOT NULL,
        now_date DATE NOT NULL
    )
            ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expense (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        expenses INTEGER NOT NULL,
        now_date DATE NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    )
            ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
            ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_db()
