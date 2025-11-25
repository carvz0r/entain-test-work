class BasePage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def open(self, path=""):
        self.page.goto(
            self.base_url + path, timeout=8000
        )
        try:
            self.page.locator(".select-region__flags___e5QCA--scss").first.wait_for(state="visible", timeout=2000)
        except TimeoutError:
            pass
        
        self._close_initial_modals()
        self.wait()

    def _close_initial_modals(self):
        cookie = self.page.locator("button#CybotCookiebotDialogBodyButtonDecline")
        if cookie.is_visible():
            cookie.click()

        region_lv = self.page.locator(".select-region__flag-content___txj3D--scss").first
        if region_lv.is_visible():
            region_lv.click()

    def wait(self):
        self.page.wait_for_load_state("load")
