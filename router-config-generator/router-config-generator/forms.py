from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, IPAddress

class configForm(FlaskForm):
    rtrHostname = StringField(
        'Router Hostname',
        [DataRequired()]
    )
    dnsSuffix = StringField(
        'DNS Suffix',
        [DataRequired()]
    )
    tzName = SelectField(
        'Timezone Name', choices=[('ACST'), ('AEST'), ('AWST')]
    )
    tzOffset = StringField(
        'Timezone offset from UTC',
        [DataRequired()]
    )
    dnsResolverPrimary = StringField(
        'Primary DNS Server',
        [IPAddress(ipv4=True, ipv6=True, message='Please enter a valid IPv4 or IPv6 address')]
    )
    generate = SubmitField('Generate Config')
