
def test_01(page):
    page.goto("https://example.com")
    print(page.title)