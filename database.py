import mysql.connector


con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_db"
)
cursor = con.cursor()

def loginUser(data):
    try:
        cursor.execute('SELECT * FROM `users` WHERE `username` = %s AND `password` = %s', data)
        return cursor.fetchone()    
    except Exception as e:
        print(e)
        return False
    
def addUser(data):
    try:
        cursor.execute('INSERT INTO `users` (`username`, `password`, `city`, `email`) VALUES (%s, %s, %s, %s)', data)
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
    

# def city_autofill(data):
#     try:
#         cursor.execute('SELECT `city` FROM `users` WHERE `username` = %s ', data)
#         con.commit()
#         return cursor.fetchall()
#     except Exception as e:
#         print(e)
        # return False
