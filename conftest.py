import os
import pytest  # pyright: ignore[reportMissingImports]
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright  # pyright: ignore[reportMissingImports]

load_dotenv()


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url") or os.getenv("BASE_URL")


@pytest.fixture()
def context(browser):
    return browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        viewport={"width": 1366, "height": 768},
        locale="lv-LV",
    )


STEALTH_JS = """
Object.defineProperty(navigator, 'webdriver', { get: () => undefined });

window.chrome = {
    runtime: {},
};

Object.defineProperty(navigator, 'plugins', {
    get: () => [1, 2, 3],
});

Object.defineProperty(navigator, 'languages', {
    get: () => ['lv-LV', 'lv'],
});
"""


@pytest.fixture
def page(request):
    headed = request.config.getoption("--headed")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=not headed, slow_mo=400)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36",
            locale="lv-LV",
            geolocation=None,
            permissions=[],
        )
        # stealth для anti-bot
        context.add_init_script(STEALTH_JS)
        page = context.new_page()
        yield page
        context.close()
        browser.close()
