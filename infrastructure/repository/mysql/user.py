from repository.mysql import repository

class user_db():

    def __init__(self, id:int, username:str, email:str, type:int, password:str):
        self.id = id
        self.username = username
        self.email = email
        self.type = type
        self.password = password


def create( value:user_db):
    db = repository.get_connection()
    cursor = db.cursor()

    try:
        cursor.execute("""INSERT INTO `users`
        (`id`,`username`,`email`,`type`,`password`)
                       VALUES
        (%s, %s, %s, %s, %s);""",
        (value.id, value.username, value.email, value.type, value.password))

    except Exception as e:
        db.rollback()
        print("Error:", e)

    db.commit()
    cursor.close()

def get(username:str, password:str) -> object:#-1 NOT FOUND
    db = repository.get_connection()
    cursor = db.cursor()

    try:
        cursor.execute("""SELECT id FROM users WHERE username = %s AND password = %s;""",
                       (username, password))
    except Exception as e:
        print(e)
        cursor.close()
        return None

    row = cursor.fetchone()

    if row == None:
        print("NOT FOUND on Users Table:", username)
        cursor.close()
        return None
    
    print("ROW:", row)
    
    user_uuid = row[0]

    try:
        cursor.execute("""SELECT id, name, last_name, second_last_name, email, birthdate From persons WHERE id_user = %s""",
                       (user_uuid))
    except Exception as e:
        print(e)
        cursor.close()
        return None
    
    row_info = cursor.fetchone()
    cursor.close()

    if row_info == None:
        print("NOT FOUND on persons TABLE")
        return None
    
    r = {
        "id":row_info[0],
        "id_user": user_uuid,
        "name":row_info[1],
        "last_name": row_info[2],
        "second_last_name":  row_info[3],
        "email": row_info[4],
        "birthdate": row_info[5]
        }
    
    return r