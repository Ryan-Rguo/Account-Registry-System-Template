import sqlite3


def test():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute('select usernames from user')                               # Select Column
        #cursor.execute('select * from user where usernames=?', ('username',))      # Select Specific Data
        #cursor.execute('delete from user where usernames=?', ('username',))        # Delete Data

        values = cursor.fetchall()
        if not values:
            print('Username not found')
        else:
            print(values)
    finally:
        cursor.close()
        conn.commit()
        conn.close()


if __name__ == '__main__':
    test()
