import sqlite3

def load_inventory(rows, db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            product_id TEXT,
            location TEXT,
            qty_on_hand REAL,
            last_updated TEXT
        )
    """)

    cur.execute("DELETE FROM inventory")

    for r in rows:
        cur.execute("""
            INSERT INTO inventory (product_id, location, qty_on_hand, last_updated)
            VALUES (?, ?, ?, datetime('now'))
        """, (
            r.get("ProductID"),
            r.get("Location"),
            r.get("QtyOnHand"),
        ))

    conn.commit()
    conn.close()
