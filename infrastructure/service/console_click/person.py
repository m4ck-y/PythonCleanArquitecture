from application.person import PersonApplication
from domain.entity.base.person import PersonEntity
from datetime import datetime
import click

__app:PersonApplication = None

@click.group()
def cli():
    pass

@cli.command()
@click.option("--n", help="Name", required=True, type=str)
@click.option("--ln", help="Last Name", required=True, type=str)
@click.option("--sln", help="Second LastName", required=True, type=str)
@click.option("--p", help="PhotoURL", required=True, type=str)
@click.option("--e", help="Email", required=True, type=str)
@click.option("--d", help="Birthdate", required=True, type=str)
def Create(name,
           last_name,
           second_last_name,
           photo_url,
           birthdate,
           email):
    data = PersonEntity()
    data.name=name
    data.last_name=last_name
    data.second_last_name=second_last_name
    data.photo_url=photo_url
    data.birthdate=birthdate
    data.email=email
    global __app
    __app.Create(data)
    print(data)

@cli.command()
def List():
    global __app
    list = __app.List()
    for person in list:
        print(f"{person.id} - {person.name} - {person.email}")

def PersonServiceConsoleClick(app:PersonApplication):
        global __app
        __app = app

        cli()
    