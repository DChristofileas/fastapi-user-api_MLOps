from fastapi import APIRouter, HTTPException
from models import User
import uuid

router = APIRouter()

# Lista para almacenar usuarios temporalmente
users_db = {}

# Endpoint POST para crear un nuevo usuario
@router.post("/users/")
async def create_user(user: User):
    user_id = str(uuid.uuid4())  # Genera un ID único
    users_db[user_id] = {"name": user.name, "email": user.email}
    return {"message": "Usuario registrado exitosamente", "user_id": user_id, "data": users_db[user_id]}

# Endpoint GET para obtener un usuario por ID
@router.get("/users/{user_id}")
async def get_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"user_id": user_id, "data": users_db[user_id]}
