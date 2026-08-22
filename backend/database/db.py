import sqlite3
from pathlib import Path


# --------------------------------------------------
# Database location
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(
    exist_ok=True
)

DATABASE_PATH = DATA_DIR / "watcher.db"


# --------------------------------------------------
# Get database connection
# --------------------------------------------------

def get_connection():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    return connection


# --------------------------------------------------
# Initialize database
# --------------------------------------------------

def init_database():

    connection = get_connection()

    cursor = connection.cursor()

    # Competitors
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS competitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            pricing_url TEXT,
            changelog_url TEXT,
            careers_url TEXT
        )
    """)

    # Snapshots
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            competitor_id INTEGER NOT NULL,
            competitor_name TEXT NOT NULL,
            page_type TEXT NOT NULL,
            url TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL,

            FOREIGN KEY (competitor_id)
            REFERENCES competitors(id)
        )
    """)

    # Changes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS changes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            competitor_id INTEGER NOT NULL,
            competitor_name TEXT NOT NULL,
            page_type TEXT NOT NULL,
            url TEXT NOT NULL,
            change_type TEXT NOT NULL,
            added TEXT,
            removed TEXT,
            detected_at TEXT NOT NULL,

            FOREIGN KEY (competitor_id)
            REFERENCES competitors(id)
        )
    """)

    connection.commit()

    connection.close()


# --------------------------------------------------
# Execute query
# --------------------------------------------------

def execute_query(
    query,
    parameters=(),
    fetch=False
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        query,
        parameters
    )

    if fetch:

        result = cursor.fetchall()

    else:

        result = None

    connection.commit()

    connection.close()

    return result


# --------------------------------------------------
# Insert data
# --------------------------------------------------

def insert(
    query,
    parameters=()
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        query,
        parameters
    )

    connection.commit()

    inserted_id = cursor.lastrowid

    connection.close()

    return inserted_id