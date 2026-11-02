# CareerVector QA Test Cases

## Execution Summary
The latest reported full-suite run recorded **17 passed, 0 failed, 0 errors, and 0 skipped**. A subsequent collection-only run confirmed 17 test cases.

| Test file | Test case | Type | Expected result |
|---|---|---|---|
| `test_cv_upload.py` | `test_cv_uploader_exists` | Functional | CV uploader is displayed on the CV analysis page. |
| `test_cv_upload.py` | `test_pdf_can_be_selected` | Functional | Selected PDF filename appears in the uploader. |
| `test_cv_upload.py` | `test_analysis_without_cv_shows_warning` | Negative validation | Starting analysis without a CV displays the upload warning. |
| `test_home.py` | `test_homepage_title` | Smoke | Browser title contains CareerVector or Streamlit. |
| `test_home.py` | `test_career_vector_heading` | Smoke | Homepage displays the CareerVector heading and greeting. |
| `test_home.py` | `test_homepage_content` | Smoke | Homepage contains expected CV, JD Match, and quiz content. |
| `test_jd_matching.py` | `test_jd_page_and_inputs` | Functional | JD Matching page, CV uploader, and JD text area are visible; JD text can be entered. |
| `test_jd_matching.py` | `test_jd_match_without_cv_shows_warning` | Negative validation | Calculating a match without a CV displays the upload warning. |
| `test_jd_matching.py` | `test_cv_upload_and_jd_entry` | Functional | A PDF can be selected and a job description can be entered. |
| `test_navigation.py` | `test_jd_match_navigation` | Functional | Selecting JD Match opens the JD Matching page. |
| `test_results.py` | `test_cv_analysis_feature_exists` | Smoke/UI | CV analysis feature content is present on the dashboard. |
| `test_results.py` | `test_jd_matching_feature_exists` | UI | JD matching feature content is present on the dashboard. |
| `test_results.py` | `test_interest_quiz_feature_exists` | UI | Interest quiz feature content is present on the dashboard. |
| `test_ui.py` | `test_page_body_is_visible` | UI | Main page body is displayed. |
| `test_ui.py` | `test_sidebar_navigation_is_visible` | UI | Sidebar is displayed. |
| `test_ui.py` | `test_theme_toggle_exists` | UI | Theme toggle is present and visible. |
| `test_ui.py` | `test_theme_toggle_changes_label` | Functional/UI | Theme toggle changes its displayed label. |

## Detailed Case: TC-NAV-03 — JD Match Navigation

| Field | Details |
|---|---|
| Test ID | TC-NAV-03 |
| Module | Navigation |
| Test Type | Functional |
| Priority | High |
| Feature | JD Match sidebar navigation |

**Objective:** Verify that selecting JD Match from the sidebar opens the JD Matching page.

**Preconditions:**
- CareerVector application is accessible.
- User has completed onboarding.
- Dashboard is displayed.

**Test Steps:**
1. Locate the JD Match navigation button.
2. Click the button.
3. Wait for Streamlit navigation to complete.
4. Verify that the JD Matching heading is displayed.

**Expected Result:** The JD Matching page opens and displays its heading.

**Initial execution:** Failed during automation with a `target frame detached` / browser-session disconnection error. This did not establish a confirmed application defect.

**Analysis:** Selenium lost its frame context or browser session during navigation and rerendering.

**Corrective action:** Selenium navigation/iframe handling was revised during troubleshooting, and the full suite was subsequently rerun.

**Latest retest:** Passed in the reported 17-test full-suite run.

## Test Execution Notes
- The PDF upload test verifies file selection, not successful PDF parsing.
- The JD input test verifies text entry, not successful AI match generation.
- Dynamic scores and analysis results are not asserted on the initial homepage because they appear only after the relevant analysis workflow.
