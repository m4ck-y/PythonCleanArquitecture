from application.person import PersonApplication
from infrastructure.repository.file.person import PersonRepositoryFile
from infrastructure.service.fastapi.person import PersonServiceFastApi

def main():
    repo = PersonRepositoryFile()
    application = PersonApplication(repo)
    service = PersonServiceFastApi(application)

if __name__ == "__main__":
    main()