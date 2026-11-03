# CareerVector QA Test Plan

## 1. Objective
Verify the availability, rendering, navigation, and selected basic workflows of CareerVector using automated browser tests.

## 2. Application
- **Application:** CareerVector — AI Career Analysis Application
- **URL:** https://ragapp-mmuhxs8autgvtc7vzxwbcz.streamlit.app/

## 3. Testing Framework and Tools
- Python 3.12
- Selenium WebDriver 4.52.0
- pytest 9.2.0
- pytest-html 4.2.0
- Microsoft Edge (recorded execution browser)

## 4. Testing Types
1. Smoke testing
2. Functional testing
3. UI testing
4. Negative validation testing

The suite can be rerun after changes as regression checking, but it does not provide exhaustive regression coverage.

## 5. Scope

### In scope
- Application launch and homepage rendering
- Onboarding and dashboard visibility
- Sidebar navigation and JD Match navigation
- CV upload control and PDF file selection
- Validation when a CV is not uploaded
- JD description input and missing-CV validation
- Presence of CV analysis, JD matching, and quiz feature content
- Basic page visibility and theme toggle behavior

### Out of scope / not verified
- Correctness or quality of AI-generated CV analysis and job-match results
- Successful end-to-end processing of a valid CV through external AI services
- Load, stress, security, accessibility, and cross-browser testing
- Exhaustive testing of different PDF formats and file sizes

## 6. Environment
- Operating system: Windows environment
- Python: 3.12
- Browser: Microsoft Edge
- Automation: Selenium WebDriver
- Test runner: pytest

## 7. Test Data
- Onboarding name: `QA Tester`
- Sample job description: Python Developer role mentioning Python, SQL, REST APIs, FastAPI, Django, and database management
- Sample PDF: generated minimal PDF used to verify file selection; it is not evidence of successful PDF text extraction or AI analysis

## 8. Execution

Run the full suite from the repository root:

```powershell
python -m pytest qa/tests -v --junitxml=qa/test-results.xml
```

Collect tests without executing them:

```powershell
python -m pytest qa/tests --collect-only -q
```

Generate the Excel report from the JUnit XML:

```powershell
python qa/create_excel_report.py
```

The Excel report is saved to `qa/test_report.xlsx`.

## 9. Latest Recorded Execution
- Tests collected: 17
- Passed: 17
- Failed: 0
- Errors: 0
- Skipped: 0
- Pass rate: 100%

This result reflects the user's reported full-suite execution and the subsequent collection output confirming 17 tests. It applies only to the test cases and environment described in this plan.
