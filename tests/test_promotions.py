import allure
from pages.promotions_page import PromotionsPage

@allure.feature("Promotions")
@allure.story("Filtering & Content Validation")
@allure.title("Promotions page – filtering and content validation")
def test_promotions(page, base_url):
    promo_page = PromotionsPage(page, base_url)

    with allure.step("Open Promotions page"):
        promo_page.open_promotions()

    with allure.step("Collect available categories from UI"):
        category_buttons = promo_page.page.locator(PromotionsPage.CATEGORY_BUTTONS)
        categories_count = category_buttons.count()

        categories = [
            category_buttons.nth(i).locator("span").text_content().strip()
            for i in range(categories_count)
        ]

        assert len(categories) > 0, "No promotion categories were found on the page"

    for cat in categories:
        with allure.step(f"Apply category filter: {cat}"):
            promo_page.apply_category(cat)

            cards = promo_page.get_promo_cards()
            count = cards.count()

            assert count > 0, f"Promo list is empty after applying filter '{cat}'"

            with allure.step(f"Validate content of promo cards for category '{cat}'"):
                for i in range(count):
                    card = cards.nth(i)
                    promo_page.check_card_content(card)
