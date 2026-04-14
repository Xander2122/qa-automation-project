import requests


def test_create_post():
    payload = {
        "title": "test",
        "body": "hello",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "test"
    assert data["body"] == "hello"
    assert data["userId"] == 1
    assert "id" in data