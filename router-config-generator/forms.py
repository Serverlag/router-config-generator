from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired, IPAddress, StopValidation

class ValidateIfDHCPExclusionsEnabled():
    def __init__(self, required_field_name):
        self.required_field_name = required_field_name

    def __call__(self, form, field):
        required_field = form._fields.get(self.required_field_name)

        if required_field is not None:
            if not bool(required_field.data):
                raise StopValidation()

class ConfigForm(FlaskForm):
    rtr_hostname = StringField(
        'Router Hostname',
        [DataRequired()]
    )
    dns_suffix = StringField(
        'DNS Suffix',
        [DataRequired()]
    )
    tz_name = SelectField(
        'Timezone Name', choices=[('ACST'), ('AEST'), ('AWST')]
    )
    tz_offset = StringField(
        'Timezone offset from UTC',
        [DataRequired()]
    )
    dns_resolver_primary_ipv4 = StringField(
        'Primary IPv4 DNS Server',
        [IPAddress(ipv4=True, ipv6=False, message='Please enter a valid IPv4 address')]
    )
    dns_resolver_secondary_ipv4 = StringField(
        'Secondary IPv4 DNS Server',
        [IPAddress(ipv4=True, ipv6=False, message='Please enter a valid IPv4 address')]
    )
    dns_resolver_primary_ipv6 = StringField(
        'Primary IPv6 DNS Server',
        [IPAddress(ipv4=False, ipv6=True, message='Please enter a valid IPv6 address')]
    )
    dns_resolver_secondary_ipv6 = StringField(
        'Secondary IPv6 DNS Server',
        [IPAddress(ipv4=False, ipv6=True, message='Please enter a valid IPv6 address')]
    )
    rtr_admin_username = StringField(
        'Router Root Username',
        [DataRequired()]
    )
    rtr_admin_password = PasswordField(
        'Router Root Password',
        [DataRequired()]
    )
    lan_ipv4_address = StringField(
        'LAN IPv4 address',
        [IPAddress(ipv4=True, ipv6=True, message='Please enter a valid IPv4 or IPv6 address')]
    )
    lan_ipv4_cidr_prefix_size = SelectField(
        'LAN IPv4 Prefix Size (CIDR)', choices=[('/31'), ('/30'), ('/29'), ('/28'), ('/27'), ('/26'), ('/25'), ('/24'), ('/23'), ('/22'), ('/21'), ('/20'), ('/19'), ('/18'), ('/17'), ('/16')], default=('/24')
    )
    lan_dhcpv4_server = BooleanField(
        'Enable DHCPv4 Server'
    )
    lan_dhcpv4_exclusions = BooleanField(
        'Configure DHCPv4 Exclusions',
    )
    lan_dhcpv4_excluded_first = StringField(
        'DHCPv4 Exclusion Start',
        [ValidateIfDHCPExclusionsEnabled('lan_dhcpv4_exclusions'), IPAddress(ipv4=True, ipv6=False, message='Please enter a valid IPv4 address')]
    )
    lan_dhcpv4_excluded_last = StringField(
        'DHCPv4 Exclusion End',
        [ValidateIfDHCPExclusionsEnabled('lan_dhcpv4_exclusions'), IPAddress(ipv4=True, ipv6=False, message='Please enter a valid IPv4 address')]
    )
    wan_technology_type = SelectField(
        'Service Technology Type', choices=[('FTTP'), ('FTTC'), ('FTTN'), ('HFC')]
    )
    wan_auth_type = SelectField(
        'Service Authentication Type', choices=[('IPoE'), ('PPPoE')]
    )
    rtr_vendor = SelectField(
        'Router Vendor', choices=[('Cisco')]
    )
    rtr_series = SelectField(
        'Router Series', choices=[('880'), ('890'), ('1100'), ('1900'), ('2900'), ('4000')]
    )
    generate = SubmitField('Generate Config')
