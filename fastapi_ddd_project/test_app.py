from fastapi.testclient import TestClient
from main import app
from dependencies import verify_token

# 1. 创建 FastAPI 官方推荐的测试客户端 (TestClient)
client = TestClient(app)

# ================= 场景 1：未覆盖依赖时发请求 =================
def test_without_mock():
    print("\n--- 1. 未伪造依赖时访问 /users/me ---")
    # 不传 Token，直接发请求
    response = client.get("/users/me")
    print("状态码:", response.status_code) # 401
    print("返回内容:", response.json())    # 提示缺少 Token


# ================= 场景 2：使用 dependency_overrides 零侵入掉包 =================
def test_with_mock():
    print("\n--- 2. 使用 dependency_overrides 掉包依赖 ---")
    
    # 定义一个假依赖函数（测试桩）
    def fake_verify_token():
        return {"user_id": 99999, "username": "测试专用机器人", "role": "admin"}
    
    # 核心动作：把真实的 verify_token 替换为 fake_verify_token
    app.dependency_overrides[verify_token] = fake_verify_token
    
    try:
        # 再次不传 Token 发送请求
        response = client.get("/users/me")
        print("状态码:", response.status_code) # 200 OK！
        print("返回内容:", response.json())    # 成功拿到了假机器人的数据！
    finally:
        # 测试完毕后，必须清空覆盖，还原真实环境！
        app.dependency_overrides.clear()


if __name__ == "__main__":
    test_without_mock()
    test_with_mock()