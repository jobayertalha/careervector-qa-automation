
import pytest

from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_cv_analysis_feature_exists(app):
    body = app.find_element(
        By.TAG_NAME, "body"
    ).text

    assert "Analyze My CV" in body
    assert "Analyze CV" in body


@pytest.mark.ui
def test_jd_matching_feature_exists(app):
    body = app.find_element(
        By.TAG_NAME, "body"
    ).text

    assert "Match with JD" in body
    assert "Match %" in body
    assert "Skill Gaps" in body


@pytest.mark.ui
def test_interest_quiz_feature_exists(app):
    body = app.find_element(
        By.TAG_NAME, "body"
    ).text

    assert "Interest Quiz" in body
    assert "Interest Score" in body
    assert "Role Fit" in body
    assert "Career Path" in body
