from infrastructure.service.fastapi.main import app
from domain.entity.pydantic.person import personEntity

from infrastructure.repository.mysql import person as personDB

@app.post("/person/create")
def Create(person:personEntity):
    personDB.create(person)