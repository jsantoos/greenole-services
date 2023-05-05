from datetime import datetime
from microservice.app.models import SensorData


def test_create_sensor_data():
    sensor_data = SensorData(
        sensor_id=1,
        timestamp=datetime.now(),
        variable="temperature",
        value=25.0,
        unit="Celsius",
    )
    assert sensor_data.sensor_id == 1
    assert isinstance(sensor_data.timestamp, datetime)
    assert sensor_data.variable == "temperature"
    assert sensor_data.value == 25.0
    assert sensor_data.unit == "Celsius"


def test_unique_constraint():
    sensor_data1 = SensorData(
        sensor_id=1,
        timestamp=datetime.now(),
        variable="temperature",
        value=25.0,
        unit="Celsius",
    )
    sensor_data2 = SensorData(
        sensor_id=1,
        timestamp=datetime.now(),
        variable="temperature",
        value=30.0,
        unit="Celsius",
    )
    assert sensor_data1 != sensor_data2
