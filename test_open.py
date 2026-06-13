from playwright.sync_api import sync_playwright

def test_open():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com", timeout=30000)
        print("页面标题:", page.title())
        page.screenshot(path="open_test.png")
        browser.close()

if __name__ == "__main__":
    test_open()
