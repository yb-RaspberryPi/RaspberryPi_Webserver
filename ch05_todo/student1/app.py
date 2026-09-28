from flask import Flask, render_template, request, redirect
import config
from model.todo_db import TodoDB


app = Flask(__name__)
todo_db = TodoDB()


@app.route("/")
def home():
    tasks = todo_db.get_all()
    return render_template("task.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    # 폼에서 content 를 받아 비어 있지 않으면 저장한 뒤 / 로 이동
    @app.route("/add", methods=["POST"])
    def add():
        content = request.form.get("content", "").strip()
        if content:
            todo_db.add(content)
        return redirect("/")
    pass


@app.route("/complete/<int:todo_id>", methods=["POST"])
def complete(todo_id):
    # 완료 여부를 뒤집은 뒤 / 로 이동
    @app.route("/complete/<int:todo_id>", methods=["POST"])
    def complete(todo_id):
        todo_db.toggle(todo_id)
        return redirect("/")
    pass


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    # 삭제한 뒤 / 로 이동
    @app.route("/delete/<int:todo_id>", methods=["POST"])
    def delete(todo_id):
        todo_db.delete(todo_id)
        return redirect("/")
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=True)
