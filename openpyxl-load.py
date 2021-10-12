from openpyxl import load_workbook
import constants

wb = load_workbook(filename=constants.EXCEL_TEST_WOOKBOOK)

ws1 = wb[constants.EXCEL_TEST_WB_TITLE1]

print(ws1['B4'].value)