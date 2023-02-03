# Excel, CSV(Comma Separated Value) 파일 다루기

# 미디어 타입 => MIME Type
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

import csv

'''
CSV 1
'''
# with open('./resource/sample1.csv', 'r') as f:
#     contents = csv.reader(f)
#     print(dir(contents))
#     # next(contents)
#     # => 입력과 출력 커서를 하나 미룬다
#     for content in contents:
#         print(content)

'''
CSV 2 => 구분자가 , 가 아닐 경우
'''
# with open('./resource/sample2.csv', 'r') as f:
#     contents = csv.reader(f, delimiter='|') # 구분자
#     for content in contents:
#         print(content)

'''
CSV 3 
csv => dict
'''
# with open('./resource/sample1.csv', 'r') as f:
#     contents = csv.DictReader(f)
#     for content in contents:
#         for k, v in content.items():
#             print(k, v)

'''
CSV 4
list => csv
'''
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# # with open('./resource/sample3.csv', 'w') as f:
# with open('./resource/sample3.csv', 'w', newline='') as f:
#     wt = csv.writer(f)

#     # 한 줄씩 넣기
#     for content in data:
#         wt.writerow(content)

#     # 여러 줄 다 넣기
#     wt.writerows(data)

# xlsx, xls 파일 다루기
# pip install pandas
# pip install xlrd
# pip install openpyxl
import pandas as pd

sample = pd.read_excel('./resource/sample.xlsx')
# 앞부분 살펴보기
# print(sample.head())

# 마지막 부분 살펴보기
# print(sample.tail())

# 파일의 속성값
# print(sample.shape)

# 파일 변환
# 다만 파일 변환용으로 사용하기에는 pandas는 한계가 있다.
# 엑셀 파일을 다룰 때는 대용으로 openpyxl을 쓴다.
# sample.to_excel('./resource/result.xlsx')
# sample.to_csv('./resource/result.csv', index=False)

from openpyxl import Workbook

wb = Workbook()

# 현재 작업중 워크시트
ws = wb.active

# 워크시트 이름 바꾸기
ws.title = 'daou'

wb.save('./resource/openpy.xlsx')

wb.close()