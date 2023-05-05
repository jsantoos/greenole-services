from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint

Base = declarative_base()


class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, index=True)
    timestamp = Column(DateTime, index=True)
    variable = Column(String, index=True)
    value = Column(Float)
    unit = Column(String)

    # Adiciona uma restrição única para evitar dados duplicados
    __table_args__ = (
        UniqueConstraint(
            "sensor_id", "timestamp", "variable", name="unique_sensor_data"
        ),
    )
