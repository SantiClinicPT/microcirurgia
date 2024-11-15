from flask import Flask, render_template, request
from wtforms.validators import email
from wtforms import BooleanField

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from form.secret_CSRF import MAIL_SENDER, MAIL_PASSWORD, TO_EMAIL_PARSERIA

from form.form import PartnerShipForm
from form.secret_CSRF import SECRET_KEY



app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PartnerShipForm()
    if request.method == 'POST':
        nome = form.nome.data
        apelido = form.apelido.data
        tel = form.tel.data
        email = form.email.data
        partner = form.partner_ship_list.data
        procedure = form.procedure_list.data

        msg = MIMEMultipart()

        msg['From'] = MAIL_SENDER
        msg['To'] = TO_EMAIL_PARSERIA
        msg['Subject'] = "Parseria SantiClinic"
        msg_text = f"""
                    Dados de Cliente
                        -Nome: {nome} 
                        -Apelido: {apelido}
                    Contactos
                        -Tel: {tel} 
                        -Email: {email} 
                        -Parceiro: {partner}
                        -Procedure: {procedure}."""
        msg.attach(MIMEText(msg_text, 'plain'))

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(MAIL_SENDER, MAIL_PASSWORD)
            text = msg.as_string()
            server.sendmail(MAIL_SENDER, TO_EMAIL_PARSERIA, text)
            server.quit()
            print("Email has been sended!")
        except Exception as e:
            print(f"Email has not been sended by error: {e}")
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)