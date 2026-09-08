from playwright.sync_api import Page

class Amazon:
    def __init__(self, page:Page, base_url="https://www.amazon.in/"):
        self.page=page
        self.url=base_url
        # self.iframe = page.locator("")
        self.searchBar= self.page.locator(".nav-search-field #twotabsearchtextbox")
        self.enter = self.page.locator('[aria-label="Go"]')
    def waitForload(self):
        self.page.wait_for_load_state("domcontentloaded")

    def SearchItem(self, itemname):
        self.searchBar.fill(itemname)

    def clickEnter(self):
        self.enter.click()

    def getCountofItems(self):
        return self.page.locator('//*[@data-component-type="s-search-result"]').count()

    
