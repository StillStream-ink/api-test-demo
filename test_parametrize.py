import requests
import pytest

# 参数化测试：测试获取多个不同的单个帖子
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_single_post(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}"，
                             timeout=5)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert "title" in data
    assert "body" in data
    assert "userId" in data

    
def test_get_nonexistent_post():
    """测试获取不存在的帖子（返回404）"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
    assert response.status_code == 404
    # 对于不存在的资源，响应体通常为空或包含错误信息，这里不深入断言
