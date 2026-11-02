
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_homepage_title(app):
    assert "CareerVector" in app.title or "Streamlit" in app.title


@pytest.mark.smoke
def test_career_vector_heading(app):
    body = app.find_element(By.TAG_NAME, "body").text

    assert "CAREERVECTOR" in body
    assert "Hello," in body


@pytest.mark.smoke
def test_homepage_content(app):
    body = app.find_element(By.TAG_NAME, "body").text

    expected_content = [
        "Analyze My CV",
        "Analyze CV",
        "Match with JD",
        "Interest Quiz",
    ]

    for item in expected_content:
        assert item in body, f"Missing homepage content: {item}"
