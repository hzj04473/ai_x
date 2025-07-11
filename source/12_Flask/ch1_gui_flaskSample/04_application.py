# 플라스트를 사용하기 위한 패키지 설치 : pip install flask
# Flask라는 micro framework 를 사용하기 위해
from aem.kae import pASPrintLength
from flask import Flask
from predict import loaded_model, predict_apt_price

# 웹 어플리케이션 객체 생성
application = Flask(__name__)

@application.route("/")
def handler_function():
    return "<h1>Hello, Flask</h1>"

# apt/2005/106/8
@application.route("/apt/<year>/<square>/<floor>")
def aptPredictHandler(year, square, floor):
    answer = predict_apt_price(year, square, floor)
    # return "<h1>예측금액은 {} 입니다.</h1>".format(answer).format(answer,",")
    return {'year':year, 'square':'aquare', 'floor':floor, 'price':answer.replace('원','').replace(',','')}
if __name__ == "__main__":
    # debug=True : 코드가 변경될 때 마다 서버 자동 재시작
    application.run(port=5001, debug=True)