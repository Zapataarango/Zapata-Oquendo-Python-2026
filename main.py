from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#creamos la clase Reserva como modelo
class Reserva(BaseModel):
    id_reserva: Optional[int] = None
    id_sala: Optional[int] = None
    id_usuario: Optional[int] = None
    fecha: Optional[str] = None
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None
    personas: Optional[int] = None
    estado: Optional[bool] = None

reservas_db = []