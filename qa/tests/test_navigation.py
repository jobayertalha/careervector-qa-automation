import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


@pytest.mark.functional
def test_jd_match_navigation(app, wait):
    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'JD Match')]")
        )
    )

    print("\nBefore click:", app.current_url)
    print("Browser windows:", app.window_handles)

    button.click()

    print("\nJD Match button clicked.")

    try:
        print("After click URL:", app.current_url)
        print("Browser windows:", app.window_handles)

        heading = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(normalize-space(.), 'JD') "
                    "and contains(normalize-space(.), 'Matching')]"
                )
            )
        )

        assert heading.is_displayed()
        print("\nJD Matching navigation successful!")

    except WebDriverException as error:
        print("\nBrowser/WebDriver failed after navigation click:")
        print(type(error).__name__)
        print(str(error))
        raise