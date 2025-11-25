import pytest
import allure
from pages.main_page import MainPage


@pytest.mark.parametrize(
    "email,password,error_field",
    [
        ("test_without_at.com", "ValidPass1", "email"),
        ("test@example.com", "123", "password"),
        ("test@example.com", "", "password"),
    ]
)
@allure.feature("User Registration")
@allure.story("Form Validation & Submission")
@allure.title("Registration form negative scenarios")
def test_registration(page, base_url, email, password, error_field):
    main_page = MainPage(page, base_url)

    with allure.step("Open main page"):
        main_page.open_main()

    with allure.step("Open registration form"):
        main_page.page.locator("button[data-role='signupHeaderButton']").click()
        main_page.page.locator("div[data-role='signupDefaultInitial'] form").wait_for(
            state="visible"
        )

    with allure.step("Fill registration form"):
        main_page.page.locator(
            "div[data-role='tnc-checkbox'] label[data-role='checkboxText']"
        ).click()

        main_page.page.locator("input[data-role='signupEmail']").fill(email)
        main_page.page.locator("input[data-role='signupPassword']").fill(password)

        # Trigger validation by switching focus
        main_page.page.locator("input[data-role='signupEmail']").click()

    with allure.step(f"Validate {error_field} field error message appears"):
        error_locator = main_page.page.locator(
            "div[data-role='signupDefaultInitial'] div[data-role='validationError']"
        )

        assert error_locator.is_visible(), (
            f"Validation error for field '{error_field}' is not visible"
        )

    with allure.step("Attach screenshot with validation error"):
        allure.attach(
            main_page.page.screenshot(),
            name=f"registration_error_{error_field}",
            attachment_type=allure.attachment_type.PNG
        )
