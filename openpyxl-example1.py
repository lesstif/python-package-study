import datetime
import math
import constants

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

wb = Workbook()

## 1번째 워크시트 생성
ws1 = wb.active
ws1.title = constants.EXCEL_TEST_WB_TITLE1

ws1['A1'] = datetime.datetime(2010, 7, 21)

wb.save(filename='example1.xlsx')