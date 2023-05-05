from datetime import datetime
from sqlalchemy.orm import Session
from typing import Dict
from fastapi import FastAPI, HTTPException, Depends
from app import models, database, crud, watchdog

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# Inicializa o banco de dados e cria a tabela
models.Base.metadata.create_all(bind=database.engine)


# Middleware para gerenciar a sessão do banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/sensor_data/")
async def create_sensor_data(sensor_data: Dict, db: Session = Depends(get_db)):
    sensor_id = sensor_data.get("sensor_id")
    timestamp = sensor_data.get("timestamp")
    variable = sensor_data.get("variable")

    if sensor_id is None or timestamp is None or variable is None:
        raise HTTPException(status_code=400, detail="Dados incompletos.")

    timestamp = datetime.fromisoformat(timestamp)

    # Verifica se o dado do sensor já existe no banco de dados
    existing_data = crud.get_sensor_data(db, sensor_id, timestamp, variable)
    if existing_data:
        raise HTTPException(status_code=400, detail="Dados já existentes.")

    # Insere os dados do sensor no banco de dados
    crud.create_sensor_data(db, sensor_data)

    return {"message": "Dados inseridos com sucesso"}


@app.get("/health_check")
async def health_check():
    return {"status": "OK"}


@app.on_event("startup")
async def startup_event():
    # Configura e inicia o sistema de watchdog para monitorar os serviços
    watchdog.start()
