from datetime import datetime
from sqlalchemy.orm import Session
from microservice.app import crud, models
from microservice.app.database import SessionLocal


def clear_sensor_data(db: Session):
    db.query(models.SensorData).delete()
    db.commit()


def test_create_sensor_data():
    db = SessionLocal()
    sensor_data = {
        "sensor_id": 1,
        "timestamp": datetime.now(),
        "variable": "temperature",
        "value": 25.0,
        "unit": "Celsius",
    }
    crud.create_sensor_data(db, sensor_data)
    db_data = db.query(crud.models.SensorData).filter_by(sensor_id=1).first()
    assert db_data.sensor_id == sensor_data["sensor_id"]
    assert db_data.variable == sensor_data["variable"]
    assert db_data.value == sensor_data["value"]
    assert db_data.unit == sensor_data["unit"]
    db.close()


def test_get_sensor_data():
    db = SessionLocal()
    sensor_data = {
        "sensor_id": 2,
        "timestamp": datetime.now(),
        "variable": "humidity",
        "value": 50.0,
        "unit": "Percent",
    }
    crud.create_sensor_data(db, sensor_data)
    db_data = crud.get_sensor_data(
        db,
        sensor_id=sensor_data["sensor_id"],
        timestamp=sensor_data["timestamp"],
        variable=sensor_data["variable"],
    )
    assert db_data.sensor_id == sensor_data["sensor_id"]
    assert db_data.variable == sensor_data["variable"]
    assert db_data.value == sensor_data["value"]
    assert db_data.unit == sensor_data["unit"]
    db.close()
