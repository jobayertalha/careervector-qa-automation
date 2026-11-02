# CareerVector QA Automation

**Automated UI and Functional Testing | Selenium WebDriver | Python | Pytest**

An independent QA automation project developed to validate the core functionality, navigation, input handling, and user interface of CareerVector, an AI-powered career analysis application.

<p align="center">
  <a href="https://github.com/jobayertalha/careervector-qa-automation">
    <img src="https://img.shields.io/badge/QA%20Automation-Selenium-green?style=for-the-badge&logo=selenium" alt="Selenium QA Automation">
  </a>
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/Pytest-9.2.0-orange?style=for-the-badge&logo=pytest" alt="Pytest">
  <img src="https://img.shields.io/badge/Tests-17%20Passed-success?style=for-the-badge" alt="17 tests passed">
</p>

---

## 1. Project Overview

CareerVector is an AI-powered career analysis application that helps users analyze their CVs, match their profiles against job descriptions, and explore career opportunities.

This repository contains an independent Selenium-based automation suite developed to test the deployed CareerVector application through its browser interface.

**Application Under Test:**  
https://ragapp-mmuhxs8autgvtc7vzxwbcz.streamlit.app/

**Original Application Repository:**  
https://github.com/jobayertalha/rag_app

**QA Automation Repository:**  
https://github.com/jobayertalha/careervector-qa-automation

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Automation programming |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution and organization |
| pytest-html | HTML test reporting |
| OpenPyXL | Excel report generation |
| Microsoft Edge | Browser under test |
| Git & GitHub | Version control |

## 3. Test Coverage

The automation suite contains 17 test cases organized into six test modules.

| Module | Test Cases | Coverage |
|---|---:|---|
| Homepage | 3 | Page title, heading, homepage content |
| Navigation | 1 | JD Match sidebar navigation |
| CV Upload | 3 | Uploader visibility, PDF selection, missing-CV validation |
| JD Matching | 3 | Page elements, JD input, CV validation |
| Results Interface | 3 | CV analysis, JD matching, quiz feature visibility |
| UI Testing | 4 | Page visibility, sidebar, theme toggle |
| **Total** | **17** | |

### Testing Categories

- **Smoke Testing:** Verifies basic application availability and essential page content.
- **Functional Testing:** Checks navigation, file selection, and user interactions.
- **UI Testing:** Validates visibility of interface components and theme controls.
- **Negative Testing:** Checks application responses to missing required inputs.

## 4. Project Structure

```text
careervector-qa-automation/
│
├── qa/
│   ├── tests/
│   │   ├── test_home.py
│   │   ├── test_navigation.py
│   │   ├── test_cv_upload.py
│   │   ├── test_jd_matching.py
│   │   ├── test_results.py
│   │   └── test_ui.py
│   │
│   ├── conftest.py
│   ├── create_excel_report.py
│   │
│   ├── TEST_PLAN.md
│   ├── TEST_CASES.md
│   ├── BUG_REPORTS.md
│   │
│   ├── test-results.xml
│   └── test_report.xlsx
│
├── pytest.ini
├── requirements-qa.txt
├── qa_report.html
└── README.md
```

## 5. Test Automation Architecture

The test suite uses a shared Pytest fixture to initialize the Selenium WebDriver, open the deployed application, complete onboarding, and prepare the application dashboard.

Individual test modules then interact with the application to validate specific functionality.

```text
             Pytest Test Runner
                     |
                     v
             Shared conftest.py
                     |
                     v
             Selenium WebDriver
                     |
                     v
              CareerVector App
                     |
          +----------+----------+
          |          |          |
          v          v          v
       Homepage   CV Upload   JD Matching
          |          |          |
          +----------+----------+
                     |
                     v
              Test Assertions
                     |
                     v
              Test Execution
                     |
          +----------+----------+
          |          |          |
          v          v          v
        HTML       JUnit       Excel
       Report      XML        Report
```

## 6. Installation and Setup

### Prerequisites

- Python 3.12 or compatible version
- Git
- Microsoft Edge browser
- Internet connection to access the deployed application

### Clone the Repository

```bash
git clone https://github.com/jobayertalha/careervector-qa-automation.git

cd careervector-qa-automation
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements-qa.txt
```

## 7. Running the Tests

### Run the Complete Test Suite

```bash
python -m pytest qa/tests -v
```

### Run a Specific Test Module

```bash
python -m pytest qa/tests/test_home.py -v
```

```bash
python -m pytest qa/tests/test_cv_upload.py -v
```

### Run Tests by Marker

```bash
python -m pytest qa/tests -m smoke -v
```

```bash
python -m pytest qa/tests -m functional -v
```

## 8. Test Reporting

The project supports three test reporting formats.

### HTML Report

Generate a self-contained HTML report:

```bash
python -m pytest qa/tests -v --html=qa_report.html --self-contained-html
```

Open `qa_report.html` in a browser to review the execution results.

### JUnit XML Report

```bash
python -m pytest qa/tests -v --junitxml=qa/test-results.xml
```

The XML report provides structured test execution data.

### Excel Report

After generating the JUnit XML report, run:

```bash
python qa/create_excel_report.py
```

The Excel workbook is generated at:

```text
qa/test_report.xlsx
```

It contains:
- Test execution summary
- Total test count
- Passed and failed tests
- Errors and skipped tests
- Pass percentage
- Individual test results
- Execution duration
- Failure and error details

## 9. Latest Recorded Test Results

The latest reported complete execution produced the following results:

| Metric | Result |
|---|---:|
| Total Tests | 17 |
| Passed | 17 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| **Pass Rate** | **100%** |

<p align="center">
  <img src="https://img.shields.io/badge/Execution-17%2F17%20Passed-brightgreen?style=for-the-badge" alt="17 of 17 tests passed">
</p>

The test collection was independently checked and confirmed 17 test cases.

See the committed HTML, XML, and Excel reports for execution evidence.

*Note: These figures represent the recorded test execution. Results may vary with application availability, network conditions, browser versions, and subsequent application changes.*

## 10. Defect Tracking and Test Documentation

The repository includes dedicated QA documentation:

| Document | Description |
|---|---|
| `TEST_PLAN.md` | Testing objectives, scope, environment, and strategy |
| `TEST_CASES.md` | Test case descriptions, steps, and expected results |
| `BUG_REPORTS.md` | Defect tracking and automation issue analysis |

During test development, the JD Match navigation test encountered Selenium iframe and browser-session issues during Streamlit rerendering.

The automation handling was revised, and the navigation test subsequently passed in the recorded full-suite execution.

This issue was tracked as an automation stability issue rather than a confirmed application defect.

## 11. Testing Limitations

The current suite focuses on browser-level functionality and basic input validation.

The following areas are not covered by the recorded tests:

- Validation of AI-generated CV analysis quality
- Accuracy of job matching scores
- Full end-to-end AI processing with valid CV documents
- Load and performance testing
- Security and penetration testing
- Accessibility testing
- Cross-browser compatibility testing

These areas can be added as future testing improvements.

## 12. Future Improvements

- Expand positive end-to-end CV analysis testing.
- Validate actual JD matching results.
- Add automated screenshots on test failures.
- Integrate tests into GitHub Actions CI/CD.
- Introduce API-level testing.
- Expand browser compatibility testing.
- Add performance and regression testing.

## 13. Author

**Talha Jobayer Zihan**

CSE Graduate | QA Automation | AI/ML Engineering

- GitHub: https://github.com/jobayertalha
- LinkedIn: https://linkedin.com/in/talha-jobayer

---

<p align="center">
  <b>CareerVector QA Automation</b><br>
  Automated Testing • Quality Assurance • Continuous Improvement
</p>
