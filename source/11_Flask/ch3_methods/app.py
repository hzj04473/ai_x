from flask import Flask, render_template, request, abort
from models import Member
from filters import mask_password

app = Flask(__name__)
app.template_filter("mask_pw")(mask_password)


@app.errorhandler(404)  # 예외처리
def errorhandler(error):
    return render_template("404_pageNotFound.html"), 404


@app.route("/", methods=["GET"])
def index():
    return render_template("2_postetc/index.html")


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "GET":  # GET 방식
        return render_template("2_postetc/join.html")
    elif request.method == "POST":  # POST 방식
        # 예전방식
        # name = request.form.get("name")
        # id = request.form.get("id") # id를 type="number" 보내옴
        # print(type(id)) # <class 'str'>
        # pw = request.form.get("pw")
        # addr = request.form.get("addr")
        # member = Member(name=name, id=id, pw=pw, addr=addr)

        # 요즘방식
        # print(request.form.to_dict())
        member = Member(**request.form.to_dict())  # 파라미터를 dict으로 변환
        # print(type(member.id))
        return render_template("2_postetc/result.html", member=member)


@app.route("/update/<name>/<id>/<pw>/<addr>", methods=["PATCH"])
def update(name, id, pw, addr):
    return f"{name}님의 정보가 수정되었습니다."

@app.route("/delete/<id>", methods=['DELETE'])
def delete(id):
    # delete from 테이블명 where id = id 를 DBMS에 전송하기
    return f"id가 {id}님의 정보가 삭제되었습니다."

if __name__ == "__main__":
    app.run(debug=True)
