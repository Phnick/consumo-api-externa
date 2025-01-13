from fastapi import FastAPI
from main.routes import starships_routes

app = FastAPI()

app.include_router(starships_routes.router)
