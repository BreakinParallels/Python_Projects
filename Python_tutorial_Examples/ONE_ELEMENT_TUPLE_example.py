




import sqlite3
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fname TEXT)")
    conn.commit()

conn = sqlite3.connect('test.db')

# tuple of names
persons_tuple = ('Kelly', 'Sally', 'Kevin', 'Adam')


# loop through each object in the tuple to find the names that end in y.
for x in persons_tuple:
    if x.endswith('y'):
        with conn:
            cur = conn.cursor()
            # The value for each row will be one out of the tuple therefore (x,)
            # will denote a one element tuple for each name ending with y.
            cur.execute("INSERT INTO tbl_persons (col_fname) VALUES (?)", (x,))
            print(x)

conn.close()


