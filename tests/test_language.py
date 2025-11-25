import allure
from pages.main_page import MainPage

LANGUAGES = ["lv", "en", "ru"]  # sequence

@allure.feature("Language Switcher")
@allure.story("UI-based Language Switching")
@allure.title("Switch language via header buttons: LV → EN → RU")
def test_language(page, base_url):
    main_page = MainPage(page, base_url)

    with allure.step("Open main page"):
        main_page.open_main()

    for lang in LANGUAGES:
        with allure.step(f"Switch language to {lang.upper()} using header button"):
            main_page.switch_language(lang)
            main_page.wait()

        with allure.step("Verify active language in UI"):
            active_lang = main_page.get_active_language()
            assert active_lang == lang, (
                f"Active language is {active_lang}, expected {lang}"
            )

        with allure.step("Verify URL corresponds to selected language"):
            assert main_page.url_contains_lang(lang), f"URL does not match language {lang}: {page.url}"

        with allure.step("Attach screenshot for current language"):
            allure.attach(
                page.screenshot(),
                name=f"{lang}_after_switch",
                attachment_type=allure.attachment_type.PNG
            )
