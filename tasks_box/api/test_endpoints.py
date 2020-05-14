from __future__ import absolute_import
import pytest
from app import app
from .utils import save_to_file


@pytest.fixture
def client():
    APP_CONFIG = {
        "CACHE_TYPE": "simple",
        "CACHE_DEFAULT_TIMEOUT": 3600,
        "DATA_FILE": "dummy_data.json",
        "STORAGE_FOLDER": "data_storage",
        "TESTING": True
    }

    mock = [
        {"id": 1, "timestamp": 1588673957.929318, "content": "Task 1", "done": False},
        {"id": 2, "timestamp": 1588673960.929318, "content": "Task 2", "done": False}
    ]
    save_to_file(mock)

    app.app.config.from_mapping(APP_CONFIG)
    return app.app.test_client()


def test_creation_of_tasks(client):

    response = client.post('/todo/', json={"content": "Task 3"})
    assert response.status_code == 200

    response_json = response.get_json()
    assert response_json["id"] == "3"
    assert response_json["content"] == "Task 3"
    assert response_json["done"] == "False"


def test_reading_of_individual_tasks(client):

    response = client.get('/task/1')
    assert response.status_code == 200

    response_json = response.get_json()
    assert response_json["id"] == "1"
    assert response_json["content"] == "Task 1"
    assert response_json["done"] == "False"


def test_update_of_individual_tasks(client):

    response = client.put('/update/1', json={"id": 3})
    assert response.status_code == 200

    response_json = response.get_json()
    assert bool(response_json["ErrorOccured"]) == True

    response = client.put('/update/1', json={"content": "Task 1, now important todo"})

    response_json = response.get_json()
    assert response_json["id"] == "1"
    assert response_json["content"] == "Task 1, now important todo"

    response = client.put('/update/2', json={"done": True})
    response_json = response.get_json()
    assert response_json["id"] == "2"
    assert response_json["done"] == "True"


def test_reading_of_a_collection_of_tasks(client):

    response = client.get('/tasks/')
    assert response.status_code == 200

    response_json = response.get_json()
    assert len(response_json) == 2
    assert response_json[0]["id"] == "1"
    assert response_json[0]["content"] == "Task 1"
    assert response_json[0]["done"] == "False"

    assert response_json[1]["id"] == "2"
    assert response_json[1]["content"] == "Task 2"
    assert response_json[1]["done"] == "False"
