from playwright.sync_api import sync_playwright

def test_saucedemo():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page()
        
        print("1. 打开登录页")
        page.goto("https://www.saucedemo.com", timeout=30000)
        
        print("2. 输入用户名")
        page.locator("#user-name").fill("standard_user")
        
        print("3. 输入密码")
        page.locator("#password").fill("secret_sauce")
        
        print("4. 点击登录")
        page.locator("#login-button").click()
        
        print("5. 等待商品页加载")
        page.wait_for_selector(".inventory_list", timeout=15000)
        
        print("6. 添加第一个商品到购物车")
        page.locator(".btn_inventory").first.click()
        
        print("7. 点击购物车图标")
        page.locator(".shopping_cart_link").click()
        
        print("8. 点击 Checkout")
        page.locator("#checkout").click()
        
        print("9. 填写姓名、邮编")
        page.locator("#first-name").fill("Test")
        page.locator("#last-name").fill("User")
        page.locator("#postal-code").fill("12345")
        
        print("10. 点击 Continue")
        page.locator("#continue").click()
        
        print("11. 点击 Finish")
        page.locator("#finish").click()
        
        print("12. 验证完成信息")
        success = page.locator(".complete-header")
        assert success.is_visible()
        print("测试通过：订单完成")
        
        page.screenshot(path="saucedemo_success.png")
        print("13. 截图已保存")
        browser.close()

if __name__ == "__main__":
    test_saucedemo()
