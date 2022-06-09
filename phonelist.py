import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="rursus",
   user="rursus",
   password="abc123"
)

def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows

def add_phone(C, name, phone, address):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}', '{address}');")
    cur.close()

def delete_phone(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE id = '{ID}';")
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

def main():
    print_help()
    while True: ## REPL - Read Execute Program Loop
        cmd = input("Command: ").upper().strip()
        if cmd == "LIST":
            for name, phone, addr, id in read_phonelist(conn):
                name = str(name); phone = str(phone); addr = str(addr); id = int(id); 
                print(f"{i:2}: {n:10} {a:15} {p:15}")
        elif cmd == "ADD":
            name = input("  Name: ")
            phone = input("  Phone: ")
            address = input("  Address: ")
            add_phone(conn, name, phone, address)
            print(f"  Added {name} with {phone}, {address}")
        elif cmd == "DELETE":
            ID = input("  ID: ")
            delete_phone(conn, ID)
            print(f"  Deleted {ID}")
        elif cmd == "HELP":
            print_help()
        elif cmd == "QUIT":
            save_phonelist(conn)
            print(f"  Goodbye!")
            exit()
        elif cmd == "SAVE":
            save_phonelist(conn)
            print(f"  Phonelist saved!")
        else:
            print(f"  Unknown command: '{cmd}'")

main()

