# python -m pip install --upgrade pip
# pip install flask
from flask import Flask

app = Flask(__name__) # 앱 인스턴스 생성

@app.route("/") #@ : 데코레이터를 통해 요청 가능한 url 등록
def handler_viewFunc():
    return "<h1>Hello, World</h1>"

# 파일명이 app.py 이면, 실행은 flask run --debug --port=5000 (기본)