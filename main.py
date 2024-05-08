from application.person import PersonApplication
from infrastructure.repository.memory.person import PersonRepositoryMemory
from infrastructure.service.fastapi.person import PersonServiceFastApi

def main():
    repo = PersonRepositoryMemory()
    application = PersonApplication(repo)
    service = PersonServiceFastApi(application)

if __name__ == "__main__":
    main()