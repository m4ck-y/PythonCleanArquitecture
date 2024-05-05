from ...repository.mysql.main import MySQLManager
from domain.entity.pydantic.person import personEntity
from datetime import datetime

class PersonRepositoryMysql():

    def __init__(self, mysqlManager:MySQLManager) -> None:
        self.mysqlManager = mysqlManager

    def Create(self, value: personEntity):
        db = self.mysqlManager.get_connection()
        cursor = db.cursor()
        try:
            cursor.execute("""INSERT INTO `persons`
                           (`id_user`,`name`,`last_name`,`second_last_name`,`email`,`birthdate`)
                           VALUES(%s, %s, %s, %s, %s, %s);""",
                           (value.id_user, value.name, value.last_name, value.second_last_name, value.email, value.birthdate))
        except Exception as e:
            db.rollback()
            print("Error:", e)
        
        db.commit()
        cursor.close()
        self.mysqlManager.close()


    def List():
        pass