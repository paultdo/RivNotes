from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import Base, engine
import models

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Building DB tables...")
    Base.metadata.create_all(bind=engine)
    print("DB tables synchronized!")

    yield

    print("Shutting down.")

# uv run uvicorn main:app --reload --env-file .env
# Initialize the application
app = FastAPI(lifespan=lifespan)


# Define a basic route
@app.get("/")
def read_root():
    return {"message": "Hello World"}
