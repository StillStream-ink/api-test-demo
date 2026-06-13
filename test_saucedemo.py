from playwright.sync_api import sync_playwright

def test_saucedemo():
    with sync_playwright() as p:
        # 仍然使用本地的 Edge 浏览器
        browser = p.chromium.launch(channel="msedge", headless=False)
        page = browser.new_page()
        
        # 1. 打开登录页
        page.goto("https://www.saucedemo.com")
        
        # 2. 登录
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        
        # 3. 等待商品页加载
        page.wait_for_selector(".inventory_list")
        
        # 4. 添加第一个商品到购物车
        page.locator(".btn_inventory").first.click()
        
        # 5. 点击购物车图标
        page.locator(".shopping_cart_link").click()
        
        # 6. 点击 Checkout
        page.locator("#checkout").click()
        
        # 7. 填写收货信息
        page.locator("#first-name").fill("Test")
        page.locator("#last-name").fill("User")
        page.locator("#postal-code").fill("12345")
        page.locator("#continue").click()
        
        # 8. 点击 Finish
        page.locator("#finish").click()
        
        # 9. 验证成功信息
        success = page.locator(".complete-header")
        assert success.is_visible()
        print("测试通过：订单完成")
        
        # 截图保存
        page.screenshot(path="saucedemo_success.png")
        browser.close()

if __name__ == "__main__":
    test_saucedemo()
