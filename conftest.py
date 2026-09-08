import json
from pathlib import Path

from playwright.sync_api import sync_playwright
import pytest


ENVIRONMENTS_FILE = Path(__file__).parent / "data" / "environments.json"


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        choices=("dev", "stage"),
        help="Environment to run tests against: dev or stage.",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        choices=("chromium", "firefox", "webkit"),
        help="Browser to run tests in: chromium, firefox, or webkit.",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run the browser without opening a visible window.",
    )


@pytest.fixture(scope="session")
def env_config(pytestconfig):
    environment = pytestconfig.getoption("--env")
    with ENVIRONMENTS_FILE.open(encoding="utf-8") as config_file:
        environments = json.load(config_file)

    return environments[environment]


@pytest.fixture
def page(pytestconfig, request):
    browser_name = pytestconfig.getoption("--browser")
    headless = pytestconfig.getoption("--headless")

    with sync_playwright() as sc:
        browser_type = getattr(sc, browser_name)
        browser = browser_type.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        yield page

        report = getattr(request.node, "rep_call", None)
        if report and report.failed:
            screenshot_dir = Path("test-results") / "screenshots"
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = screenshot_dir / f"{request.node.name}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

@pytest.fixture
def apireq(env_config):
    with sync_playwright() as sc:
        apicontext = sc.request.new_context(
            base_url=env_config["api_base_url"]
        )
        yield apicontext
        apicontext.dispose()
