import openpyxl
import os

# 스크립트 파일의 디렉토리 경로
script_dir = os.path.dirname(os.path.abspath(__file__))
# 워크북 파일 경로
file_path = os.path.join(script_dir, "../1-1_xlwings_test.xlsx")


# 워크북 열기
wb = openpyxl.load_workbook(file_path)

# 활성 시트 가져오기
sheet = wb.active

print("데이터 가져와 연산 수행")
b1 = sheet["B1"].value
b2 = sheet["B2"].value

# b1-b2값을 'B3'셀에 넣기
sheet["B3"].value = b1 - b2

# 변경사항을 원본 파일에 저장
wb.save(file_path)

print("연산 결과 쓰기 완료")
