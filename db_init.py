import sqlite3

conn = sqlite3.connect("posts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# test data
cursor.execute("INSERT INTO posts (title, description) VALUES (?, ?)",
               ("First post", "This is my first post"))
cursor.execute("INSERT INTO posts (title, description) VALUES (?, ?)",
               ("Second post", "Socket + DB example"))

conn.commit()
conn.close()

print("Database ready ✅")
