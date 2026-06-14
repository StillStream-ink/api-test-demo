import requests
import pytest

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_single_post(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert "title" in data
    assert "body" in data
    assert "userId" in data

def test_get_nonexistent_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
    assert response.status_code == 404