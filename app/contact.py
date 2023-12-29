from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/contact", methods=["POST"])
def contact_form():
    email = request.form.get('email')
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    return render_template('templates/contact_snippet.html')