
import pytest

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


APP_URL = "https://ragapp-mmuhxs8autgvtc7vzxwbcz.streamlit.app/"
TEST_USERNAME = "QA Tester"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    browser = webdriver.Edge(options=options)
    browser.set_page_load_timeout(90)

    yield browser

    browser.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 60)


@pytest.fixture
def app(driver, wait):
    driver.get(APP_URL)

    try:
        # 1. Wait for the actual Streamlit application iframe.
        app_frame = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'iframe[title="streamlitApp"]')
            )
        )

        # 2. Switch Selenium into the application iframe.
        driver.switch_to.frame(app_frame)

        # 3. Wait for the welcome screen input.
        name_input = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[placeholder="e.g. Talha"]')
            )
        )

        # 4. Enter test username.
        name_input.clear()
        name_input.send_keys(TEST_USERNAME)

        # 5. Locate the Get Started button.
        start_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[contains(., 'Get Started')]"
                )
            )
        )

        # 6. Scroll the button into view.
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            start_button
        )

        # 7. Wait until the button is visible and enabled.
        wait.until(
            lambda d: (
                start_button.is_displayed()
                and start_button.is_enabled()
            )
        )

        # 8. Use JavaScript click to avoid intercepted pointer clicks.
        driver.execute_script(
            "arguments[0].click();",
            start_button
        )

        # 9. Wait for the actual dashboard.
        wait.until(
            lambda d: (
                "Analyze CV" in d.find_element(
                    By.TAG_NAME, "body"
                ).text
                and
                "JD Match" in d.find_element(
                    By.TAG_NAME, "body"
                ).text
            )
        )

        print("\nCareerVector dashboard loaded successfully!")

        return driver

    except Exception:
        # Capture failure evidence.
        try:
            driver.save_screenshot("qa_loading_failure.png")

            with open(
                "qa_page_source.html",
                "w",
                encoding="utf-8"
            ) as file:
                file.write(driver.page_source)

            print("\nCurrent URL:", driver.current_url)

        except Exception:
            print("\nCould not capture browser failure evidence.")

        raise
