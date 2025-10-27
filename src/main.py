from fastapi import FastAPI

import uvicorn

from api.controllers import TasksController
from api.controllers import UsersController

def main():
    app = FastAPI(
        title="summer",
        version="0.0.1"
    )

    app.include_router(TasksController.router)
    app.include_router(UsersController.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    