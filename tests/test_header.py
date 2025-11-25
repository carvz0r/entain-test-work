import allure
from pages.main_page import MainPage

@allure.feature("Header")
@allure.story("Navigation & UI")
@allure.title("Header menu visibility and navigation links")
def test_header(page, base_url):
    main_page = MainPage(page, base_url)

    with allure.step("Open main page"):
        main_page.open_main()

    with allure.step("Check that the logo is visible"):
        assert main_page.is_logo_visible(), "Logo is not visible"

    with allure.step("Check header navigation menu links"):
        expected_paths = [
            "/casino",
            "/live-casino",
            "/sport",
            "/sport/wcg",
            "/poker",
            "/promotions",
        ]
        hrefs = main_page.get_menu_hrefs()
        for path in expected_paths:
            assert any(path in href for href in hrefs), f"Menu link with href '{path}' not found"
