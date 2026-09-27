
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status

api = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

class TodoCreate(BaseModel):
    title: str
    completed: bool

todos = [
    Todo(id=1, title="Buy groceries", completed=False),
    Todo(id=2, title="Read a book", completed=False),
    Todo(id=3, title="Go for a walk", completed=False)
]

@api.get("/todos")
def getTodos():
    return {"todos": todos}


@api.get("/todos/{id}", response_model=Todo, status_code=status.HTTP_200_OK)
def get_todo(id:int):
    print(f"todo_id: {id}")
    for todo in todos:
        if todo.id == id:
            print(todo)
            return todo
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found")    

@api.post("/todos", status_code= status.HTTP_201_CREATED)
def create_todo(todo:TodoCreate):
    id = max(todo.id for todo in todos) + 1
    # id = 10
    print(f"New id: {id}")
    
    new_todo:Todo = Todo(id= id, title=todo.title, completed=todo.completed)
    print(f"new_todo: ${new_todo}")

    todos.append(new_todo)
    return new_todo

@api.put("/todos/{id}")
def update_todo(id:int, newTodo:TodoCreate):
    for todo in todos:
        if todo.id == id:
            todo.title = newTodo.title
            todo.completed = newTodo.completed
            print("udpated")
            return {
                    "status" : status.HTTP_200_OK,
                    "message": f"Todo updated successfully."
                }
    return {
        "status" : status.HTTP_404_NOT_FOUND,
        "message": f"Update Failed. Todo not found"
    }

@api.delete("/todos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id:int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos.pop(index)
            print("removed")
            return 
            
    return {
        "status" : status.HTTP_404_NOT_FOUND,
        "message": f"Delete Failed. Todo not found"
    }