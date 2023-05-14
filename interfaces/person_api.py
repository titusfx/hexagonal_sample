from fastapi import APIRouter
from application.create_person import create_person
from infrastructure.person_repository import save_person

router = APIRouter()

@router.post("/persons/")
def create_person_endpoint(name: str):
    person = create_person(name)
    save_person(person)
    return {"message": "Person created"}
