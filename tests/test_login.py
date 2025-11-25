import allure
from pages.main_page import MainPage


@allure.feature("Login")
@allure.story("Negative Login")
@allure.title("Login with non-existent username/password should fail")
def test_login(page, base_url):
    main_page = MainPage(page, base_url)

    with allure.step("Open main page"):
        main_page.open_main()

    with allure.step("Open login modal"):
        page.locator('button[data-role="loginHeaderButton"]').click()

    with allure.step("Fill login form with invalid credentials"):
        page.locator('input[data-role="loginEmailInput"]').fill(
            "nonexistent_user_example@example.com"
        )
        page.locator('input[data-role="password"]').fill("WrongPass123")

    with allure.step("Submit login form"):
        page.locator('button[data-role="loginSubmit"]').click()
        page.wait_for_timeout(1500)

    with allure.step("Verify error message is visible"):
        error_message = page.locator(
            'div[data-role="profileDialogWindow"] div[data-role="validationError"]'
        )
        error_message.wait_for(state="visible", timeout=5000)
        assert error_message.is_visible(), "Error message is not displayed"
