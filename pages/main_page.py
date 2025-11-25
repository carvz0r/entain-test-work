import allure
from pages.base_page import BasePage

class MainPage(BasePage):
    LOGO = "#topBar a.logo___KOtFY--scss"
    MENU_ITEMS = "nav a"

    LANGUAGE_BUTTON = "header a.language-menu__label___Wutxr--scss"
    LANG_ITEM = "header a#langMenuItem-{}"

    @allure.step("Open main page")
    def open_main(self):
        self.open("/")

    @allure.step("Check if logo is visible")
    def is_logo_visible(self):
        return self.page.locator(self.LOGO).is_visible()

    @allure.step("Get navigation menu items")
    def get_menu_items(self):
        return self.page.locator(self.MENU_ITEMS)

    @allure.step("Get href attributes of menu items")
    def get_menu_hrefs(self):
        locator = self.get_menu_items()
        count = locator.count()

        hrefs = []
        for i in range(count):
            href = locator.nth(i).get_attribute("href")
            if href:
                hrefs.append(href)
        return hrefs

    @allure.step("Get active language from UI")
    def get_active_language(self):
        label = self.page.locator(self.LANGUAGE_BUTTON)
        label.wait_for(state="visible")
        text = label.text_content().strip().lower()
        return text

    def url_contains_lang(self, lang: str):
        url = self.page.url.lower()

        if lang == "lv":
            return not ("/en/" in url or "/ru/" in url)

        return f"/{lang}/" in url

    @allure.step("Switch language to {lang}")
    def switch_language(self, lang: str):
        self.page.locator(self.LANGUAGE_BUTTON).click()

        option = self.page.locator(f"header a[data-id='langMenuItem-{lang}']")
        option.wait_for(state="visible")
        option.click()

        self.page.wait_for_load_state("domcontentloaded")
