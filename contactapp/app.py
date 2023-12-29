from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

@app.route("/contact", methods=["POST"])
def contact_form():
    email = request.form.get('email')
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')

    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=[email])



    return render_template('templates/contact_snippet.html', context={'email': email})