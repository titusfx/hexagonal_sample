from fastapi import FastAPI
from interfaces.person_api import router as person_router

app = FastAPI()

app.include_router(person_router)
