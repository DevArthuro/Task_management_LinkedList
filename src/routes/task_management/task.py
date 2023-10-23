from fastapi import APIRouter, Request
from fastapi import status
from src.models.task import TaskRegister
from templating_routing import templates
from src.algoritms.linkedlist import LinkedList
from typing import List

database = LinkedList()

app_route_task = APIRouter()

@app_route_task.get("/")
async def show_tasks(request: Request):
    tasks = database.get_values_nodes()
    context = {
        "request": request,
        "title": "Tareas Registradas",
        "tasks": tasks
    }
    return templates.TemplateResponse("/task/task-show.html", context)

@app_route_task.post("/")
async def save_task(request: Request, tasks: List[TaskRegister]):
    for task in tasks:
        database.set_new_node(task)
    tasks = database.get_values_nodes()
    context = {
        "request": request,
        "title": "Tareas Registradas",
        "tasks": tasks,
    }
    
    return templates.TemplateResponse("/task/task-show.html", context)