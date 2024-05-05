from infrastructure.service.console.person import personServiceConsole
from infrastructure.repository.mysql.person import personRepositoryMysql, MySQLManager


def main():

    print("main")

    mysqlManager = MySQLManager() 
    personRepositoryMysql = personRepositoryMysql(mysqlManager)

    personConsole = personServiceConsole(personRepositoryMysql)
    personConsole.Add()
    personConsole.List()
    


if __name__ == "__main__":
    main()