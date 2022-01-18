
# calling python to use SQLite3 Library
import sqlite3

# Create database
conn = sqlite3.connect('fileList.db')


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMove.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
# connect to database
with conn:
    cur = conn.cursor()
    # creating a table
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT)")
    # iterating through the file list
    for file in fileList:
        # checking to see if file ends with ".txt"
        if file.endswith('.txt'):
            # inserting files that end in .txt into the database
            cur.execute("INSERT INTO tbl_fileList(col_filename) VALUES (?)", \
                        (file,))
            print(file)
    
    conn.commit()
# Closing database
conn.close()
