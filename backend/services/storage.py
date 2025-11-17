# backend/services/storage.py
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "storage.db")
DB_PATH = os.path.abspath(DB_PATH)

def _get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def _ensure_db():
    if not os.path.exists(DB_PATH):
        conn = _get_conn()
        c = conn.cursor()
        c.execute("""
            CREATE TABLE summaries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT,
                text TEXT,
                summary TEXT
            );
        """)
        conn.commit()
        conn.close()

_ensure_db()

def save_summary(text, summary):
    conn = _get_conn()
    c = conn.cursor()
    now = datetime.utcnow().isoformat()
    c.execute("INSERT INTO summaries (created_at, text, summary) VALUES (?, ?, ?)", (now, text, summary))
    conn.commit()
    last_id = c.lastrowid
    conn.close()
    return str(last_id)

def get_summary_by_id(summary_id):
    conn = _get_conn()
    c = conn.cursor()
    c.execute("SELECT id, created_at, text, summary FROM summaries WHERE id = ?", (summary_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        return None
    return {"id": row["id"], "created_at": row["created_at"], "text": row["text"], "summary": row["summary"]} 