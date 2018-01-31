import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("create table IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("insert into contacts (name, phone, email) VALUES ('Tim', 6545678, 'tim@email.com')")
db.execute("insert into contacts VALUES ('Brian', 4567, 'brian@myemail.com')")
db.commit()
cursor = db.cursor()
cursor.execute("select * from contacts")
# for row in cursor:
#     print(row)

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

# for name, phone, email in cursor:
#     print(name)
#     print(phone)
#     print(email)
#     print("-" * 20)

cursor.close()
db.close()

