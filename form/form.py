from random import choices
from select import select

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
        [validators.Length(min=4, max=25)]
    )
    apelido = StringField(
        'Apelido',
        [validators.Length(min=4, max=25)]
    )
    tel = StringField(
        'Telefone',
        [validators.Length(min=9, max=14)]
    )
    email = EmailField(
        'Email',
        [validators.Length(min=6, max=35)])
    partner_ship_list = SelectField(
        'Partner', choices = [
            (partner, partner) for partner in partners_list

        ],
        render_kw = {"placeholder": "Select a partner"}
    )

    procedure_list = SelectField(
        'Procedure', choices=[
            (procedure, procedure) for procedure in procedure_list
        ],
        render_kw={"placeholder": "Select a procedure"}
    )
    submit = SubmitField("Submit")
