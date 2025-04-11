from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def contact_form():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('first_name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    message = request.form.get('message')
    subject = request.form.get('subject')
    Preferred_Contact = request.form.get('Preferred_Contact')
    Agreement = request.form.get('Agreement')


    return render_template(
        'Confirmation.html',
        name=name,
        email=email,
        phone_number=phone_number,
        message=message,
        subject=subject,
        Preferred_Contact=Preferred_Contact,
        Agreement=Agreement,
    )

if __name__ == '__main__':
    app.run(debug=True)