from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
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
    dnsResolverPrimaryIPv4 = StringField(
        'Primary IPv4 DNS Server',
        [IPAddress(ipv4=True, ipv6=False, message='Please enter a valid IPv4 or IPv6 address')]
    )
    dnsResolverSecondaryIPv4 = StringField(
        'Secondary IPv4 DNS Server',
        [IPAddress(ipv4=True, ipv6=False, message='Please enter a valid IPv4 or IPv6 address')]
    )
    rtrAdminUsername = StringField(
        'Router Root Username',
        [DataRequired()]
    )
    rtrAdminPassword = PasswordField(
        'Router Root Password',
        [DataRequired()]
    )
    lanIPv4Address = StringField(
        'LAN IPv4 address',
        [IPAddress(ipv4=True, ipv6=True, message='Please enter a valid IPv4 or IPv6 address')]
    )
    lanIPv4CidrPrefixSize = SelectField(
        'LAN IPv4 Prefix Size (CIDR)', choices=[('/31'), ('/30'), ('/29'), ('/28'), ('/27'), ('/26'), ('/25'), ('/24'), ('/23'), ('/22'), ('/21'), ('/20'), ('/19'), ('/18'), ('/17'), ('/16')]
    )
    wanTechnologyType = SelectField(
        'Service Technology Type', choices=[('FTTP'), ('FTTC'), ('FTTN'), ('HFC')]
    )
    wanAuthType = SelectField(
        'Service Authentication Type', choices=[('IPoE'), ('PPPoE')]
    )
    rtrVendor = SelectField(
        'Router Vendor', choices=[('Cisco')]
    )
    rtrSeries = SelectField(
        'Router Series', choices=[('880'), ('890'), ('1100'), ('1900'), ('2900'), ('4000')]
    )
    generate = SubmitField('Generate Config')
