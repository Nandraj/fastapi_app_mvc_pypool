from fastapi.testclient import TestClient
from app.main import app

test_client = TestClient(app)


def test_process():
    response = test_client.post(
        "/api/process", json={"batchid": "id0101", "payload": [[1, 2], [3, 4]]}
    )
    assert response.status_code == 200
    assert response.json()["batchid"] == "id0101"
    assert response.json()["response"] == [3, 7]


def test_invalid_payload():
    response = test_client.post(
        "/api/process", json={"batchid": "id0102", "payload": [[1, 2], ["a", 4]]}
    )
    assert response.status_code == 422
