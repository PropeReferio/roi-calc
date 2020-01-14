from addpage import app
from flask import render_template, request, url_for
from addpage.forms import AddForm


#I may need to import redirect on line 2 and
#print the sum on a different page
@app.route("/add", methods=["GET", "POST"])
def add():
    addForm = AddForm()
    if request.method == "POST":
        num1 = addForm.num1.data
        num2 = addForm.num2.data
        result = int(num1) + int(num2)
    return render_template("add.html", addform = addForm, result = result)
