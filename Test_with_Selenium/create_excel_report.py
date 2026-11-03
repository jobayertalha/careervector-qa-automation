
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter


XML_FILE = Path("qa/test-results.xml")
OUTPUT_FILE = Path("qa/test_report.xlsx")

if not XML_FILE.exists():
    raise FileNotFoundError(
        "Test results not found. Run pytest first."
    )

root = ET.parse(XML_FILE).getroot()

testcases = root.findall(".//testcase")

results = []

for case in testcases:
    failure = case.find("failure")
    error = case.find("error")
    skipped = case.find("skipped")

    if failure is not None:
        status = "FAILED"
        details = failure.get("message", "") + "\n" + (
            failure.text or ""
        )
    elif error is not None:
        status = "ERROR"
        details = error.get("message", "") + "\n" + (
            error.text or ""
        )
    elif skipped is not None:
        status = "SKIPPED"
        details = skipped.get("message", "")
    else:
        status = "PASSED"
        details = ""

    results.append({
        "test": case.get("name", ""),
        "file": case.get("classname", ""),
        "time": float(case.get("time", 0)),
        "status": status,
        "details": details.strip()
    })

total = len(results)
passed = sum(r["status"] == "PASSED" for r in results)
failed = sum(r["status"] == "FAILED" for r in results)
errors = sum(r["status"] == "ERROR" for r in results)
skipped = sum(r["status"] == "SKIPPED" for r in results)

wb = Workbook()

# Summary sheet
ws = wb.active
ws.title = "Test Summary"

ws.append(["CAREERVECTOR - QA TEST REPORT"])
ws.append(["Generated", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
ws.append([])
ws.append(["Metric", "Count"])
ws.append(["Total Tests", total])
ws.append(["Passed", passed])
ws.append(["Failed", failed])
ws.append(["Errors", errors])
ws.append(["Skipped", skipped])
ws.append([
    "Pass Rate",
    f"{(passed / total * 100):.2f}%" if total else "N/A"
])

# Detailed results sheet
detail = wb.create_sheet("Test Details")

detail.append([
    "Test File",
    "Test Case",
    "Status",
    "Duration (seconds)",
    "Failure / Error Details"
])

for result in results:
    detail.append([
        result["file"],
        result["test"],
        result["status"],
        result["time"],
        result["details"]
    ])

# Formatting
header_fill = PatternFill(
    "solid", fgColor="1F4E78"
)

for sheet in wb.worksheets:
    sheet.freeze_panes = "A2"

    for cell in sheet[1]:
        cell.font = Font(
            bold=True,
            color="FFFFFF",
            size=14
        )
        cell.fill = header_fill
        cell.alignment = Alignment(
            horizontal="center"
        )

for cell in ws[4]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = header_fill

for cell in detail[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = header_fill
    cell.alignment = Alignment(
        horizontal="center",
        vertical="center",
        wrap_text=True
    )

for row in range(2, detail.max_row + 1):
    status_cell = detail.cell(row, 3)
    status = status_cell.value

    if status == "PASSED":
        status_cell.font = Font(color="008000", bold=True)
    elif status in ("FAILED", "ERROR"):
        status_cell.font = Font(color="FF0000", bold=True)
    elif status == "SKIPPED":
        status_cell.font = Font(color="CC8800", bold=True)

    for cell in detail[row]:
        cell.alignment = Alignment(
            vertical="top",
            wrap_text=True
        )

for sheet in wb.worksheets:
    for column in sheet.columns:
        max_length = max(
            len(str(cell.value or ""))
            for cell in column
        )
        column_letter = get_column_letter(
            column[0].column
        )
        sheet.column_dimensions[column_letter].width = min(
            max(max_length + 3, 15), 65
        )

detail.column_dimensions["E"].width = 65

wb.save(OUTPUT_FILE)

print("\nQA REPORT GENERATED SUCCESSFULLY")
print(f"File: {OUTPUT_FILE}")
print(f"Total: {total}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Errors: {errors}")
print(f"Skipped: {skipped}")
print(
    f"Pass Rate: {(passed / total * 100):.2f}%"
    if total else "Pass Rate: N/A"
)
