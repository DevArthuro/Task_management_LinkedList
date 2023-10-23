from fastapi import FastAPI
from src.routes.task_management.task import app_route_task
from uvicorn import run

app = FastAPI()


app.include_router(app_route_task, prefix="/manage-task")

if __name__ == "__main__":
    run(app)