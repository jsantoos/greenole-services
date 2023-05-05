from datetime import datetime
from sqlalchemy.orm import Session
from . import models


def create_sensor_data(db: Session, sensor_data: dict):
    db_data = models.SensorData(
        sensor_id=sensor_data["sensor_id"],
        timestamp=sensor_data["timestamp"],
        variable=sensor_data["variable"],
        value=sensor_data["value"],
        unit=sensor_data["unit"],
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)


def get_sensor_data(db: Session, sensor_id: int, timestamp: datetime, variable: str):
    return (
        db.query(models.SensorData)
        .filter(
            models.SensorData.sensor_id == sensor_id,
            models.SensorData.timestamp == timestamp,
            models.SensorData.variable == variable,
        )
        .first()
    )
