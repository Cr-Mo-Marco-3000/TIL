from flask import Flask, render_template
from flask import request

import pymysql

import time
import atexit

app = Flask(__name__)


# @app.route("/db")
# def view_template():
#     return render_template("db.html")


# @app.route("/dept-search")
# def search_dept():
#     dept_no = request.args.get("deptno")
#     print(dept_no)
#     print("---")

#     conn = pymysql.connect(
#         host="localhost", user="root", password="root1234", db="scott", charset="utf8"
#     )

#     cur = conn.cursor()

#     sql = f"select * from emp where deptno = {dept_no}"
#     cur.execute(sql)

#     # result = list(cur)
#     result = []
#     for record in cur:
#         result.append([record[0], record[1]])
#     print("--------------------------------------------")

#     return render_template("result.html", result=result)


from apscheduler.schedulers.background import BackgroundScheduler


def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=10)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
