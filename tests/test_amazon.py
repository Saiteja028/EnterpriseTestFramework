from pages.amazon import Amazon


def test_search_count(page, env_config):
    amazon = Amazon(page, env_config["web_base_url"])
    amazon.page.goto(amazon.url)
    amazon.waitForload()
    amazon.SearchItem("Shoes")
    amazon.waitForload()
    amazon.clickEnter()
    amazon.waitForload()
    count=amazon.getCountofItems()
    assert count==60

