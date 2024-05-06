from application.person import PersonApplication
from infrastructure.repository.memory.person import PersonRepositoryMemory
from infrastructure.service.console_click.person import PersonServiceConsoleClick

def main():
    repo = PersonRepositoryMemory()
    application = PersonApplication(repo)
    service = PersonServiceConsoleClick(application)

if __name__ == "__main__":
    main()