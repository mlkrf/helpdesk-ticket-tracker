import sqlite3
from datetime import datetime

DB_NAME = "tickets.db"

def connect():
    return sqlite3.connect(DB_NAME)

def setup():
    with connect() as conn:
        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            '''
        )

def create_ticket():
    title = input("Ticket title: ").strip()
    description = input("Description: ").strip()
    priority = input("Priority (Low/Medium/High): ").strip().title()

    if priority not in {"Low", "Medium", "High"}:
        priority = "Medium"

    with connect() as conn:
        conn.execute(
            "INSERT INTO tickets (title, description, priority, status, created_at) VALUES (?, ?, ?, ?, ?)",
            (title, description, priority, "Open", datetime.now().isoformat(timespec="seconds")),
        )
    print("Ticket created.")

def list_tickets():
    with connect() as conn:
        rows = conn.execute(
            "SELECT id, title, priority, status, created_at FROM tickets ORDER BY id DESC"
        ).fetchall()

    if not rows:
        print("No tickets found.")
        return

    print("\nID | Priority | Status | Title | Created")
    print("-" * 70)
    for ticket_id, title, priority, status, created_at in rows:
        print(f"{ticket_id} | {priority} | {status} | {title} | {created_at}")

def update_ticket():
    ticket_id = input("Ticket ID: ").strip()
    new_status = input("New status (Open/In Progress/Resolved): ").strip().title()

    valid = {"Open", "In Progress", "Resolved"}
    if new_status not in valid:
        print("Invalid status.")
        return

    with connect() as conn:
        cur = conn.execute(
            "UPDATE tickets SET status = ? WHERE id = ?",
            (new_status, ticket_id),
        )

    if cur.rowcount == 0:
        print("Ticket not found.")
    else:
        print("Ticket updated.")

def main():
    setup()

    while True:
        print("\nHelpdesk Ticket Tracker")
        print("1. Create ticket")
        print("2. View tickets")
        print("3. Update ticket status")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_ticket()
        elif choice == "2":
            list_tickets()
        elif choice == "3":
            update_ticket()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
