from flask import Flask, render_template, request, jsonify
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("flask_blog_secretkey")

my_email = os.environ.get("my_gmail_email")
my_password = os.environ.get("my_gmail_temppass")


@app.route("/", methods=["GET", "POST"])
def main_page():
    name = request.form.get("name", False)
    email = request.form.get("email", False)
    subject = request.form.get("subject", False)
    msg = request.form.get("message", False)
    if name and email and subject and msg:
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                    msg=f"Subject: {subject}\n\n"
                                        f"Name: {name}\n"
                                        f"Email: {email}\n"
                                        f"Message: {msg}\n")
            return jsonify({"success": "Email submitted successfully!"})
        except:
            return jsonify({"error": "An error occurred while sending the email!"})
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
