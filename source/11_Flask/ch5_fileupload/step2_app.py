# pip install flask_wtf : 플라스크에서 폼 관리라는 기능
    # CSRF 보호 정책 설정
    # 쉽고 유연한 폼 적용하여, 유효성 검증, input 태그 생성
from flask import Flask, render_template # ,request.files["file"]
from flask_wtf import FlaskForm # 유효성 검사를 위한 form 객체 생성
from flask_wtf.file import FileField, FileRequired # 파일 업로드 기능 추가
from werkzeug.utils import secure_filename # 업로드한 파일명에 특수문자를 뺴서 저장
from fileinfo import info # 파일 정보 출력
import os
import uuid
# 업로드 폴더 경로 설정 (폴더 없으면 촐더 생생)
UPLOAD_FOLDER = './uploads/'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)  # 없으면 생성


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 5  # 5MB
app.config['SECRET_KEY'] = uuid.uuid4() # CSRF 보호 정책 설정을 하려면 필요

# print(app.config['SECRET_KEY'])

class FileForm(FlaskForm):
    files = FileField(validators=[FileRequired()]) # 업로드한 파일 객체

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FileForm()
    if form.validate_on_submit(): # 폼 데이터가 유효한지 (POST요청이 유효하게 들어왔는지) 체크
        file = form.files.data # 업로드한 파일 객체
        # 파일명에 서버에 영향을 마칠 특수문자 뺴서 저장
        safe_filename = secure_filename(file.filename) # 업로드한 파일명에 특수문자를 뺴서 저장
        file.save(UPLOAD_FOLDER + safe_filename) # 업로드 폴더에 파일 저장

        ctime, mtime, atime, size = info(safe_filename) # 파일 정보 출력
        return render_template('check.html', 
                                fileinfo = {'ctime': ctime,
                                            'size': size})
    else : # GET 방식이거나 POST 요청이 유효하지 않을 경우
        return render_template('upload.html', form=form) # upload.html 수정

if __name__ == '__main__':
    app.run(debug=True)
