import allure
from pages.base_page import BasePage

class PromotionsPage(BasePage):
    PROMO_CARD = "a[data-role='promotion']"
    PROMO_BADGE = "[data-role='promotionBadge']"
    PROMO_TITLE = "[data-role='promotionTitle']"
    PROMO_TITLE_LINK = "[data-role='promotionTitleLink']"
    PROMO_DESCRIPTION = "[data-role='promotionDescription']"

    CATEGORY_BUTTONS = "li[data-role='tags'] button"

    @allure.step("Open Promotions page")
    def open_promotions(self):
        self.open("/promotions")

    @allure.step("Apply category filter: {category_name}")
    def apply_category(self, category_name: str):
        buttons = self.page.locator(self.CATEGORY_BUTTONS)
        count = buttons.count()
        for i in range(count):
            text = buttons.nth(i).locator("span").text_content().strip()
            if text.lower() == category_name.lower():
                buttons.nth(i).click()
                self.page.wait_for_timeout(500)
                return
        raise ValueError(f"Category '{category_name}' not found")

    @allure.step("Get all promotion cards")
    def get_promo_cards(self):
        return self.page.locator(self.PROMO_CARD)

    @allure.step("Check promotion card content")
    def check_card_content(self, card):
        title = card.locator(self.PROMO_TITLE).text_content().strip()
        badge = card.locator(self.PROMO_BADGE).text_content().strip()
        assert title, "Title is missing"
        assert badge, "Category badge is missing"

    @allure.step("Open promotion detail page and verify")
    def open_promo_detail(self, card):
        link = card.locator(self.PROMO_TITLE_LINK)
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

        title = self.page.locator("h1, h2").first.text_content().strip()
        description = self.page.locator(self.PROMO_DESCRIPTION).text_content().strip()

        assert title, "Title on detail page is missing"
        assert description, "Description on detail page is missing"

        self.page.go_back()
        self.page.wait_for_load_state("domcontentloaded")
