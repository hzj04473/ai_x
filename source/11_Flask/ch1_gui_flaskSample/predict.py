# 가상환경 만들기 : python -m venv .venv
# 가상화경 들어가기 : source .venv/bin/activate
# python -m pip install --upgrade pip
# pip install statsmodels
# pip install joblib
# pip install xlwings
# pip install flask
import joblib

loaded_model = joblib.load('../model/ex1_apt_price_regression.joblib')

def predict_apt_price(year, square, floor) :
    "건축연도, 전용면적, 층을 입력받아 예측가를 return"
    input_data = [[int(year), int(square), int(floor), 1]]
    pred = round(loaded_model.predict(input_data)[0]*10000)
    return format(pred, ",") + "원"

if __name__ == "__main__":
    year = input("몇년 ? : ")
    square = input("전용면적 ? : ")
    floor = input("몇 층 ? : ")

    print("예측한 금액은 : ", predict_apt_price(year, square, floor))

