from pages.amazon import Amazon
def testSearchCount(page):
    amazon= Amazon(page)
    amazon.page.goto(amazon.url)
    amazon.waitForload()
    amazon.SearchItem("Shoes")
    amazon.waitForload()
    amazon.clickEnter()
    amazon.waitForload()
    count=amazon.getCountofItems()
    assert count==60

