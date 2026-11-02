
import os
import tempfile
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def navigate_to_cv_analysis(app, wait):
    analyze_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Analyze CV')]")
        )
    )
    analyze_button.click()

    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="stFileUploaderDropzone"]')
        )
    )


def create_sample_pdf():
    content = (
        b"%PDF-1.4\n"
        b"1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
        b"2 0 obj<</Type/Pages/Count 0/Kids[]>>endobj\n"
        b"trailer<</Root 1 0 R>>\n"
        b"%%EOF"
    )

    file = tempfile.NamedTemporaryFile(
        suffix=".pdf", delete=False
    )
    file.write(content)
    file.close()

    return file.name


@pytest.mark.functional
def test_cv_uploader_exists(app, wait):
    navigate_to_cv_analysis(app, wait)

    uploader = app.find_element(
        By.CSS_SELECTOR,
        '[data-testid="stFileUploaderDropzone"]'
    )

    assert uploader.is_displayed()


@pytest.mark.functional
def test_pdf_can_be_selected(app, wait):
    navigate_to_cv_analysis(app, wait)

    uploader = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                '[data-testid="stFileUploaderDropzone"] input[type="file"]'
            )
        )
    )

    path = create_sample_pdf()

    uploader.send_keys(os.path.abspath(path))

    wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),
            os.path.basename(path)
        )
    )

    body = app.find_element(By.TAG_NAME, "body").text

    assert os.path.basename(path) in body


@pytest.mark.functional
def test_analysis_without_cv_shows_warning(app, wait):
    navigate_to_cv_analysis(app, wait)

    start_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Start Analysis')]")
        )
    )
    start_button.click()

    warning = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(text(), 'Please upload your CV first')]"
            )
        )
    )

    assert warning.is_displayed()
