
import os
import tempfile
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


JOB_DESCRIPTION = (
    "Python Developer. "
    "Requirements: Python, SQL, REST APIs, "
    "FastAPI, Django and database management."
)

FRAME_LOCATOR = (
    By.CSS_SELECTOR,
    'iframe[title="streamlitApp"]'
)

JD_TEXTAREA = (
    By.CSS_SELECTOR,
    'textarea[placeholder="Paste the full job description here..."]'
)


# ----------------------------------
# Navigation Helper
# ----------------------------------

def navigate_to_jd_page(app, wait):

    app.switch_to.default_content()

    # Enter the current Streamlit iframe.
    wait.until(
        EC.frame_to_be_available_and_switch_to_it(FRAME_LOCATOR)
    )

    # Click JD Match.
    button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(., 'JD Match')]"
            )
        )
    )

    # Normal Selenium click first.
    button.click()

    # Streamlit may rerender its iframe after navigation.
    app.switch_to.default_content()

    wait.until(
        EC.frame_to_be_available_and_switch_to_it(FRAME_LOCATOR)
    )

    # Wait for the actual JD Matching page heading.
    wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//h1[contains(., 'JD') and contains(., 'Matching')]"
            )
        )
    )

    # Wait for CV uploader.
    wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                '[data-testid="stFileUploaderDropzone"]'
            )
        )
    )

    # Wait for JD textarea.
    wait.until(
        EC.visibility_of_element_located(JD_TEXTAREA)
    )

    return app


# ----------------------------------
# Sample PDF Generator
# ----------------------------------

def create_sample_pdf():

    content = (
        b"%PDF-1.4\n"
        b"1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
        b"2 0 obj<</Type/Pages/Count 0/Kids[]>>endobj\n"
        b"trailer<</Root 1 0 R>>\n"
        b"%%EOF"
    )

    file = tempfile.NamedTemporaryFile(
        suffix=".pdf",
        delete=False
    )

    file.write(content)
    file.close()

    return file.name


# ----------------------------------
# Test 1: JD Page and Both Inputs
# ----------------------------------

@pytest.mark.functional
def test_jd_page_and_inputs(app, wait):

    navigate_to_jd_page(app, wait)

    heading = app.find_element(
        By.XPATH,
        "//h1[contains(., 'JD') and contains(., 'Matching')]"
    )

    assert heading.is_displayed()

    # Input 1: CV PDF uploader.
    uploader = app.find_element(
        By.CSS_SELECTOR,
        '[data-testid="stFileUploaderDropzone"]'
    )

    assert uploader.is_displayed()

    # Input 2: Job Description textarea.
    textarea = app.find_element(*JD_TEXTAREA)

    assert textarea.is_displayed()

    # Automatically enter Job Description.
    textarea.send_keys(JOB_DESCRIPTION)

    assert textarea.get_attribute("value") == JOB_DESCRIPTION

    print("\nJD Matching page opened successfully!")
    print("Job Description entered successfully!")


# ----------------------------------
# Test 2: Missing CV Validation
# ----------------------------------

@pytest.mark.functional
def test_jd_match_without_cv_shows_warning(app, wait):

    navigate_to_jd_page(app, wait)

    calculate_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(., 'Calculate Match')]"
            )
        )
    )

    calculate_button.click()

    warning = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(text(), 'Please upload your CV first')]"
            )
        )
    )

    assert warning.is_displayed()

    print("\nMissing CV validation works correctly!")


# ----------------------------------
# Test 3: Upload CV and Fill JD
# ----------------------------------

@pytest.mark.functional
def test_cv_upload_and_jd_entry(app, wait):

    navigate_to_jd_page(app, wait)

    path = create_sample_pdf()

    try:
        # Step 1: Locate CV file input.
        file_input = wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    '[data-testid="stFileUploaderDropzone"] input[type="file"]'
                )
            )
        )

        # Step 2: Upload PDF.
        file_input.send_keys(os.path.abspath(path))

        # Step 3: Verify uploaded filename.
        wait.until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, "body"),
                os.path.basename(path)
            )
        )

        # Step 4: Locate JD textarea.
        textarea = wait.until(
            EC.visibility_of_element_located(JD_TEXTAREA)
        )

        # Step 5: Enter Job Description.
        textarea.send_keys(JOB_DESCRIPTION)

        # Step 6: Verify entered JD.
        assert textarea.get_attribute("value") == JOB_DESCRIPTION

        # Step 7: Verify uploaded PDF.
        body = app.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert os.path.basename(path) in body

        print("\nCV uploaded successfully!")
        print("Job Description entered successfully!")
        print("Both JD Matching inputs verified!")

    finally:
        # Keep the temporary file because Edge may still hold it.
        pass
