from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

url = "https://jsonplaceholder.typicode.com/"


def test_infourl():
    resp = client.get("/info-url/", params={"url": url})

    assert resp.status_code == 200
    assert list(resp.json().keys()) == ["title", "urls"]
    assert resp.json()["title"] == "JSONPlaceholder - Free Fake REST API"


def test_error_infourl():
    url = "htts://jsonplaceholder.typicode.com/"
    resp = client.get("/info-url/", params={"url": url})
    assert resp.status_code == 422

