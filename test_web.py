from playwright.sync_api import sync_playwright

def test_edge_search():
    with sync_playwright() as p:
        # 关键：使用 channel="msedge" 来启动已安装的 Edge
        browser = p.chromium.launch(channel="msedge", headless=False)
        page = browser.new_page()
        page.goto("https://www.baidu.com")
        page.locator("#kw").fill("自动化测试")
        page.locator("#su").click()
        page.wait_for_selector(".result", timeout=10000)
        page.screenshot(path="edge_result.png")
        browser.close()
