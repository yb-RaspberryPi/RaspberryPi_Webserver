from flask import Flask
import config  # <--- 이 줄을 반드시 추가하세요!

app = Flask(__name__)


# 이전 질문에서 요청하셨던 hello 라우트
@app.route("/hello/<vino>")
def hello_name(vino):
    return f"Hello, {vino}!"


@app.route("/sum/<int:a>/<int:b>")
def sum_two(a, b):
    return "{0} + {1} = {2}".format(a, b, a + b)


@app.route("/greet/<name>")
def greet(name):
    return "안 녕 하 세 요 , {0}님 ".format(name)


@app.route("/info")
def info():
    return "포 트 : {0} / 데 이 터 베 이 스 : {1}".format(
        config.PORT, config.DB_NAME
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
