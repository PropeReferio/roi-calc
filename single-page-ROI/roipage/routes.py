from addpage import app
from flask import render_template, request, url_for
from addpage.forms import AddForm


#I may need to import redirect on line 2 and
#print the sum on a different page
@app.route("/roi", methods=["GET", "POST"])
def roi():
    roiForm = ROIForm()
    if request.method == "POST":
        rent = roiForm.rent.data
        mortgage = roiForm.mortgage.data
        #Continue assigning form data to variables, adjust HTML to reflect
    return render_template("add.html", addform = addForm, result = result)
