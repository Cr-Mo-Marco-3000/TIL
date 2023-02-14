from flask import Flask, render_template
from flask import request

# 1. 플라스크 객체 생성
# 원래 __name__은 자기 모듈의 이름(hello.py)를 의미한다.
# python 명령어로 실행 되면 이름이 main으로 바뀜

app = Flask(__name__)

# 서버 구동시, 개발 정의 URL값과 플라스크에서 정의된 함수를 연결
# 뷰 함수
@app.route("/hello")
def hello_flask():
	return "Hello, 파이썬"

@app.route("/login", methods=['GET', 'POST'])
def print_id_pw():
	if request.method == 'GET':
		print('GET Method')
		# 파라미터 => request.args
		id = request.args.get('id')
		pw = request.args.get('pw')
	elif request.method == 'POST':
		print('POST Method')
		# 전송 form => request.form
		id = request.form['id']
		pw = request.form['pw']
	return id + ' ' + pw


# 해당 파일 실행시 플라스크 서버 실행
if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 5000, debug = True)