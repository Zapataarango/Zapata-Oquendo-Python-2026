from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

ARCHIVO_JSON = 'reservas.json'

class Reserva(BaseModel):
    id_reserva: Optional[int] = None
    id_sala: Optional[int] = None
    id_usuario: Optional[int] = None
    fecha: Optional[str] = None
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None
    personas: Optional[int] = None
    estado: Optional[bool] = None

def leer_datos():
    try:
        with open(ARCHIVO_JSON, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(datos):
    with open(ARCHIVO_JSON, 'w') as file:
        json.dump(datos, file, indent=4)

@app.post("/reservas")
async def reservar_sala(reserva: Reserva):
    lista_datos = leer_datos()
    
    nueva_reserva = reserva.model_dump()
    
    lista_datos.append(nueva_reserva)
    
    guardar_datos(lista_datos)
    
    return {"message": "Reserva guardada con éxito", "data": nueva_reserva}

@app.get("/reservas/listar")
async def obtener_reservas():
    return leer_datos()

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}