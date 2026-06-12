import requests
import pytest

# ========== 基础冒烟测试 ==========
@pytest.mark.smoke
def test_get_single_post_1():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
    assert response.status_code == 200

# ========== 参数化测试（冒烟） ==========
@pytest.mark.smoke
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_single_post(post_id):
    # 已修复：中文逗号 → 英文逗号
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}",
                             timeout=5)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert "title" in data
    assert "body" in data
    assert "userId" in data

# ========== 回归测试用例 ==========
@pytest.mark.regression
def test_get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

@pytest.mark.regression
def test_create_post():
    new_post = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post, timeout=5)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"

@pytest.mark.regression
def test_get_nonexistent_post():
    """测试获取不存在的帖子（返回404）"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/99999", timeout=5)
    assert response.status_code == 404
