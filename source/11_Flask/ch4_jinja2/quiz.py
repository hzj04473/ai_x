from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index(no = None):
    # if request.method == 'GET':
        # no = None
    # elif request.method == 'POST':
    if request.method == 'POST':
        # no = request.form.get('no') # 전달받은 파라미터 값 (str)
        no = int(request.form.get('no')) # 전달받은 파라미터 값 (int)
    return render_template('quiz.jinja.html', no=no)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

