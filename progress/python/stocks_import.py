import sqlite3
import csv
import argparse
from pathlib import Path

def import_stocks(csv_path: str, db_path: str):
    csv_file = Path(csv_path)
    db_file = Path(db_path)

    if not csv_file.exists():
        print(f"❌ CSV file not found: {csv_file}")
        return

    # Connect to SQLite
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Stocks (
        SymbolId TEXT NOT NULL,
        Name TEXT NOT NULL,
        Exchange TEXT NOT NULL,
        Currency TEXT,
        Industry TEXT,
        Sector TEXT,
        PRIMARY KEY (SymbolId, Name, Exchange)
    );
    """)

    # Prepare UPSERT SQL
    upsert_sql = """
        INSERT INTO Stocks (SymbolId, Name, Exchange, Currency, Industry, Sector)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(SymbolId, Name, Exchange)
        DO UPDATE SET
            Currency=excluded.Currency,
            Industry=excluded.Industry,
            Sector=excluded.Sector;
    """

    inserted = 0
    updated = 0

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Try inserting — if conflict, it auto-updates
            cur.execute(upsert_sql, (
                row['SymbolId'],
                row['Name'],
                row['Exchange'],
                row.get('Currency'),
                row.get('Industry'),
                row.get('Sector')
            ))
            
            # SQLite’s “changes()” returns number of rows affected by last statement
            changes = conn.total_changes
            if changes > inserted + updated:
                # We don't know whether it's insert or update directly,
                # so check if the row existed before
                cur.execute("""
                    SELECT 1 FROM Stocks WHERE SymbolId=? AND Name=? AND Exchange=?
                """, (row['SymbolId'], row['Name'], row['Exchange']))
                if cur.fetchone():
                    updated += 1
                else:
                    inserted += 1

    conn.commit()
    conn.close()

    print(f"✅ Import completed.")
    print(f"📦 Inserted: {inserted}")
    print(f"🔁 Updated: {updated}")
    print(f"💾 Database: {db_file}")

def main():
    parser = argparse.ArgumentParser(description="Import stock data from CSV to SQLite with upsert behavior.")
    parser.add_argument("--csv", required=True, help="Path to the input CSV file")
    parser.add_argument("--db", required=True, help="Path to the SQLite database file")
    args = parser.parse_args()

    import_stocks(args.csv, args.db)

if __name__ == "__main__":
    main()
