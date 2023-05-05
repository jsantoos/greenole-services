
# Sensor data - Microservice

This is a Python-based microservice that uses FastAPI and SQLAlchemy to provide a simple API for managing sensor data. This microservice also includes a watchdog that checks the status of other services and sends notifications to a Discord channel if any of the services go down.

## Installation

To run the microservice, you need to have Docker and Docker Compose installed on your system. After installing Docker and Docker Compose, clone the repository and navigate to the root directory of the project. 

Then run the following command:

```python
docker-compose up
```

This command will build the Docker image and start the container.
Usage
After starting the container, you can access the API by navigating to <a href="http://localhost:5000/docs" target="_new">http://localhost:5000/sensor_data</a>. Where you can test the different endpoints of the API.

## Running Tests
To run the tests, you can use the following command:
```python
pytest
```
This command will run all the tests in the tests/ directory.
References
<li><a href="https://fastapi.tiangolo.com/" target="_new">FastAPI documentation</a></li><li><a href="https://www.sqlalchemy.org/" target="_new">SQLAlchemy documentation</a></li><li><a href="https://docs.docker.com/" target="_new">Docker documentation</a></li><li><a href="https://docs.docker.com/compose/" target="_new">Docker Compose documentation</a></li>
