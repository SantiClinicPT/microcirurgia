from random import choices
from select import select
from wtforms import BooleanField

from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import SubmitField, TextAreaField, EmailField
from wtforms import Form, StringField, validators
from wtforms.validators import DataRequired, Email

partners_list = [
    'Márcia Monteiro Micropigmentação'

]

procedure_list = [
    'Microcirurgia cosmética Consulta',
    'Micro lifting de sobrancelha',
    'Micro blefaroplastia superior',
    'Micro blefaroplastia inferior',
    'Lifting do terço médio e inferior',
    'Micro cervicoplastia (papada e pescoço)'
]

class PartnerShipForm(FlaskForm):
    nome = StringField(
        'Nome',
        [validators.Length(min=4, max=25)],
        render_kw={"class": "input_class", "placeholder": "Introduz o seu Nome"}
    )
    apelido = StringField(
        'Apelido',
        [validators.Length(min=4, max=25)],
        render_kw={"class": "input_class", "placeholder": "Introduz o seu Apelido"}

    )
    
    tel = StringField(
        'Telefone',
        [validators.Length(min=9, max=14)],
        render_kw={"class": "input_class", "placeholder": "Introduz o seu contacto telefonico"}
    )
    
    email = EmailField(
        'Email',
        [validators.Length(min=6, max=35)],
        render_kw={"class": "input_class", "placeholder": "Introduz o seu Email"}
    )
    
    partner_ship_list = SelectField(
        'Partner', choices = [
            (partner, partner) for partner in partners_list],
        render_kw = {"class": "input_class_selection"}
    )

    procedure_list = SelectField(
        'Procedure', choices=[
            (procedure, procedure) for procedure in procedure_list
        ],
        render_kw={"class": "input_class_selection"}
    )

    checkbox = BooleanField('Eu concordo em partilhar minhas informações de contato com o propósito de ser contactado pela Santiclinic',
              default=True,
              render_kw ={'checked':''})


    submit = SubmitField(
        "Submeter", 
        render_kw={"class": "input_class_submit"}
        )
