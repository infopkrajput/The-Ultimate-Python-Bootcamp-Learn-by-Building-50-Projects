import sqlite3

DB_NAME = 'url_shortener.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT NOT NULL UNIQUE,
                visit_count INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        
def insert_url(original_url, short_code):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)', (original_url, short_code))
        conn.commit()

def get_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.execute('SELECT * FROM urls WHERE short_code = ?', (short_code,))
        return c.fetchone()
    
def increment_visit_count(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.execute('UPDATE urls SET visit_count = visit_count + 1 WHERE short_code = ?', (short_code,))
        
def get_all_urls():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.execute('SELECT original_url, short_code, visit_count FROM urls ORDER BY id DESC')
        return c.fetchall()
    
def delete_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('DELETE FROM urls WHERE short_code = ?', (short_code,))