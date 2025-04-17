import sqlite3

class BankAccount:
    def __init__(self, user_id):
        self.user_id = user_id
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        self.transaction_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                user_id TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                balance REAL DEFAULT 0.0
            )
        ''')
        self.conn.commit()

    def transaction_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                user_id TEXT,
                transaction_type TEXT,
                amount REAL DEFAULT 0.0,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP 
            )  
        ''')
        self.conn.commit()

    def create_account(self, password):
        self.cursor.execute('INSERT OR IGNORE INTO accounts (user_id, password, balance) VALUES (?,?,?)', (self.user_id, password, 0.0))
        self.conn.commit()

    def verify_password(self, password):
        self.cursor.execute('SELECT password FROM accounts WHERE user_id = ?', (self.user_id,))
        result = self.cursor.fetchone()
        return result[0] == password if result else False



    def deposit(self, amount):
        self.cursor.execute('UPDATE accounts SET balance = balance + ? WHERE user_id = ?', (amount, self.user_id))
        self.cursor.execute('INSERT INTO transactions (user_id, amount, transaction_type) VALUES (?, ?, ?)', (self.user_id, amount, 'deposit'))
        self.conn.commit()

    def withdraw(self, amount):
        self.cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.user_id,))
        current_balance = self.cursor.fetchone()[0]
        if amount <= current_balance:
            self.cursor.execute('UPDATE accounts SET balance = balance - ? WHERE user_id = ?', (amount, self.user_id))
            self.cursor.execute('INSERT INTO transactions (user_id, amount, transaction_type) VALUES (?, ?, ?)', (self.user_id, amount, 'withdraw'))
            self.conn.commit()
        else:
            print("Insufficient funds.")

    def get_balance(self):
        self.cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else 0.0
    
    def transaction_history(self):
        self.cursor.execute('SELECT * FROM transactions WHERE user_id = ?', (self.user_id,))
        return self.cursor.fetchall()
    
    def delete_account(self):
        self.cursor.execute('DELETE FROM accounts WHERE user_id = ?', (self.user_id,))
        self.cursor.execute('DELETE FROM transactions WHERE user_id = ?', (self.user_id,))
        self.conn.commit()
        self.conn.close()