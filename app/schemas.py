from pydantic import BaseModel

class TodoBase(BaseModel):
    title:  str
    description: str | None = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: int

    class config:
        from_attributes = True
        
