import requests
import pytest

def test_get_all_posts():
    """测试获取所有帖子（GET /posts）"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    # 验证返回的数据是列表，且长度大于0
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_create_post():
    """测试创建新帖子（POST /posts）"""
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
    assert response.status_code == 201  # 创建成功通常返回201
    data = response.json()
    assert data["title"] == "foo"
    assert data["body"] == "bar"
    assert data["userId"] == 1
    # 注意：jsonplaceholder 不会真正保存数据，但会返回一个带 id 的响应
    assert "id" in data
