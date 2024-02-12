import sqlite3

conn = sqlite3.connect('example.db')
print("opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (01,'FAITH KARIMI',23,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (02,'CURTIS KIHAMA',25,300000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (03,'MARK MUUTE',33,275000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (04,'JAMES OBUONG',37,255000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (05,'JANET KIBET',29,200000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()

# Run this file once