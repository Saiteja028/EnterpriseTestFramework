from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture
def page():
    with sync_playwright() as sc:
        browser = sc.chromium.launch(headless=False)
        context = browser.new_context()
        page=context.new_page()
        yield page
        browser.close()

@pytest.fixture
def apireq():
    with sync_playwright() as sc:
        apicontext = sc.request.new_context(
            base_url="https://automationexercise.com/api/"
        )
        yield apicontext
        apicontext.dispose()
        