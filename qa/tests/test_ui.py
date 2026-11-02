import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_theme_button(driver):
    buttons = driver.find_elements(
        By.CSS_SELECTOR,
        '[data-testid="stSidebar"] button'
    )

    for button in buttons:
        if (
            "Light Mode" in button.text
            or "Dark Mode" in button.text
        ):
            return button

    return None


@pytest.mark.ui
def test_page_body_is_visible(app):
    body = app.find_element(
        By.TAG_NAME, "body"
    )

    assert body.is_displayed()


@pytest.mark.ui
def test_sidebar_navigation_is_visible(app):
    sidebar = app.find_element(
        By.CSS_SELECTOR,
        '[data-testid="stSidebar"]'
    )

    assert sidebar.is_displayed()


@pytest.mark.ui
def test_theme_toggle_exists(app):
    theme_button = get_theme_button(app)

    assert theme_button is not None, (
        "Theme toggle was not found"
    )

    assert theme_button.is_displayed()


@pytest.mark.functional
def test_theme_toggle_changes_label(app, wait):
    theme_button = get_theme_button(app)

    assert theme_button is not None, (
        "Theme toggle was not found"
    )

    old_label = theme_button.text

    expected_label = (
        "Dark Mode"
        if "Light Mode" in old_label
        else "Light Mode"
    )

    theme_button.click()

    wait.until(
        lambda driver: (
            expected_label in driver.find_element(
                By.CSS_SELECTOR,
                '[data-testid="stSidebar"]'
            ).text
        )
    )

    updated_button = get_theme_button(app)

    assert updated_button is not None
    assert expected_label in updated_button.text