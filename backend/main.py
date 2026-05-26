from fastapi import FastAPI

# Initialize the application
app = FastAPI()


# Define a basic route
@app.get("/")
def read_root():
    return {"message": "Hello World"}
