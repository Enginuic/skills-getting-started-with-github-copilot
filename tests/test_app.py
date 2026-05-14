import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_read_root():
    # Arrange
    expected_url_suffix = "/static/index.html"

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert str(response.url).endswith(expected_url_suffix)


def test_get_activities():
    # Arrange
    expected_key = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert expected_key in response.json()