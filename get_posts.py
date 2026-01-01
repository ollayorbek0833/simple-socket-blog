import sqlite3

DB_NAME = "posts.db"


def get_posts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, description, created_at
        FROM posts
        ORDER BY created_at DESC
    """)

    posts = cursor.fetchall()
    conn.close()
    return posts


def create_post(title, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO posts (title, description) VALUES (?, ?)",
        (title, description)
    )

    conn.commit()
    conn.close()


def get_post_by_id(post_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, description, created_at
        FROM posts
        WHERE post_id = ?
    """, (post_id,))

    post = cursor.fetchone()
    conn.close()
    return post
