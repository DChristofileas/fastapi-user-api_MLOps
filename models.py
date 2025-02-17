from pydantic import BaseModel

# Modelo para el usuario
class User(BaseModel):
    name: str
    email: str
