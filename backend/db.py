import sqlite3

DB = "questions.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE IF NOT EXISTS questions (q TEXT UNIQUE, ts DATETIME DEFAULT CURRENT_TIMESTAMP)")
    conn.close()

def cache_question(q):
    conn = sqlite3.connect(DB)
    conn.execute("INSERT OR REPLACE INTO questions (q) VALUES (?)", (q,))
    conn.commit()
    conn.close()

def get_recent_questions():
    conn = sqlite3.connect(DB)
    rows = conn.execute("SELECT q FROM questions ORDER BY ts DESC LIMIT 5").fetchall()
    conn.close()
    return [r[0] for r in rows]

init_db()
