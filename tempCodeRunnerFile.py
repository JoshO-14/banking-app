 def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                user_id TEXT PRIMARY KEY,
                balance REAL DEFAULT 0.0
            )
        ''')
        self.conn.commit()

    def transaction_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                transaction_type TEXT,
                amount REAL DEFAULT 0.0,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES accounts (user_id)
            )   
        ''')
