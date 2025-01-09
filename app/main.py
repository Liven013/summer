from fastapi import FastAPI
from database.database import init_db
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}



if __name__ == "__main__":
    init_db()
    uvicorn.run("main:app", host="localhost", port = 8080, reload = True)
