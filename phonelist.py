# import sqlite3
# conn = sqlite3.connect("phone.db")
import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="rursus",
   user="rursus",
   password="abc123"
)

# the rest of the file exactly as before

def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.close()
def delete_phone(C, name):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()
def print_help():
    print("""Hello and welcome to the phone list, available commands:
  add    - add a phone number
  delete - delete a contact
  help   - print the help
  list   - list all phone numbers
  quit   - quit the program
  save   - save the phone list""")

print_help()
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").upper().strip()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        add_phone(conn, name, phone)
        print(f"  Added {name} with {phone}")
    elif cmd == "DELETE":
        name = input("  Name: ")
        delete_phone(conn, name)
        print(f"  Deleted {name}")
    elif cmd == "HELP":
        print_help()
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
        print(f"  Goodbye!")
    elif cmd == "SAVE":
        save_phonelist(conn)
        print(f"  Phonelist saved!")
    else:
        print(f"  Unknown command: '{cmd}'")

