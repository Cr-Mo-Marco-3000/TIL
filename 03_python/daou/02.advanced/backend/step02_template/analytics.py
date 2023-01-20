from flask import Flask, render_template

app = Flask(__name__)


@app.route("/analytics/<name>")
def view_template(name):
    class_list = ["파이썬 프로그래밍 기초", "데이터 수집", "백엔드 프로그래밍 기초"]
    return render_template("analytics.html", name=name, class_list=class_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
