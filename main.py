from fastapi import FastAPI
from src.routes.task_management.task import app_route_task
from uvicorn import run
from environ import Env
from fastapi.middleware.cors import CORSMiddleware

env = Env()
Env.read_env()



app = FastAPI()
app.middleware(CORSMiddleware(
    app,
    allow_credentials=["*"],
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
))

app.include_router(app_route_task, prefix="/manage-task")

if __name__ == "__main__":
    run(app, host = env("HOST_SERVER"), port = int(env("PORT_SERVER")))