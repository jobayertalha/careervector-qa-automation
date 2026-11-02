# CareerVector QA Defect and Automation Issue Log

## Current Defect Status
No confirmed application defects have been documented from the available test evidence.

## Automation Issue: TC-NAV-03 — JD Match Navigation

| Field | Details |
|---|---|
| Reference | TC-NAV-03 |
| Category | Test automation / WebDriver stability |
| Affected test | `qa/tests/test_navigation.py::test_jd_match_navigation` |
| Initial status | Failed |
| Latest retest status | Passed |
| Confirmed application defect | No |

### Initial observed behavior
During an earlier execution, Selenium failed while waiting for the JD Matching heading after clicking the JD Match navigation control. Reported errors included `target frame detached` and, in a later execution, `InvalidSessionIdException` stating that the browser had closed its DevTools connection.

### Expected behavior
The JD Match navigation control opens the JD Matching page and displays its heading.

### Analysis
The exception indicates that Selenium's browser session or frame context became unavailable during navigation. This alone is not sufficient evidence to classify the application navigation as defective.

### Corrective action and verification
The Selenium navigation test/iframe handling was revised during troubleshooting. The user subsequently reported a full-suite result of 17 passed, 0 failed, and 0 errors. The collection output confirmed that `test_jd_match_navigation` is among the 17 collected tests.

### Final status
**Retest passed** in the latest reported full-suite execution. No application bug is confirmed from this incident.

## Bug Report Template
Use this template when a reproducible application defect is observed:

- Bug ID:
- Title:
- Severity:
- Environment:
- Preconditions:
- Steps to Reproduce:
- Expected Result:
- Actual Result:
- Screenshot / Evidence:
- Status:
