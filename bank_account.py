import sqlite3

class BankAccount:
    def __init__(self, user_id):
        self.user_id = user_id
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                user_id TEXT PRIMARY KEY,
                balance REAL DEFAULT 0.0
            )
        ''')
        self.conn.commit()

    def create_account(self):
        self.cursor.execute('INSERT OR IGNORE INTO accounts (user_id, balance) VALUES (?, ?)', (self.user_id, 0.0))
        self.conn.commit()

    def deposit(self, amount):
        self.cursor.execute('UPDATE accounts SET balance = balance + ? WHERE user_id = ?', (amount, self.user_id))
        self.conn.commit()

    def withdraw(self, amount):
        self.cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.user_id,))
        current_balance = self.cursor.fetchone()[0]
        if amount <= current_balance:
            self.cursor.execute('UPDATE accounts SET balance = balance - ? WHERE user_id = ?', (amount, self.user_id))
            self.conn.commit()
        else:
            print("Insufficient funds.")

    def get_balance(self):
        self.cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else 0.0
