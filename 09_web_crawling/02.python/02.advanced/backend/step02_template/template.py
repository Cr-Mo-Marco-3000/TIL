from flask import Flask, render_template

app = Flask(__name__)


@app.route("/template-basic/<int:page_number>")
def view_template(page_number):
    title = "템플릿"
    nums_list = [1, 2, 3, 4, 5]
    nums_dict = {"one": 1, "two": 2}
    print(page_number)
    return render_template(
        "template.html",
        title=title,
        nums_list=nums_list,
        nums_dict=nums_dict,
        page_number=page_number,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
