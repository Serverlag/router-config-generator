from __init__ import app
from flask import render_template
from forms import ConfigForm
import ipaddress

@app.route("/", methods=["GET", "POST"])
def home():
    form = ConfigForm()
    if form.validate_on_submit():
        ip_interface = ipaddress.ip_interface(form.lan_ipv4_address.data+form.lan_ipv4_cidr_prefix_size.data)
        ipv4_network_address = str(ip_interface.network).split('/')[0]
        ipv4_hostmask = str(ip_interface.hostmask).split('/')[0]
        ipv4_subnet_mask = str(ip_interface.netmask)
        return render_template(
            "generate.html",
            form=form,
            rtr_hostname = form.rtr_hostname.data,
            dns_suffix = form.dns_suffix.data,
            tz_name = form.tz_name.data,
            tz_offset = form.tz_offset.data,
            dns_resolver_primary_ipv4 = form.dns_resolver_primary_ipv4.data,
            dns_resolver_secondary_ipv4 = form.dns_resolver_secondary_ipv4.data,
            dns_resolver_primary_ipv6 = form.dns_resolver_primary_ipv6.data,
            dns_resolver_secondary_ipv6 = form.dns_resolver_secondary_ipv6.data,
            rtr_admin_username = form.rtr_admin_username.data,
            rtr_admin_password = form.rtr_admin_password.data,
            lan_ipv4_address = form.lan_ipv4_address.data,
            lan_ipv4_cidr_prefix_size = form.lan_ipv4_cidr_prefix_size.data,
            lan_dhcpv4_server = form.lan_dhcpv4_server.data,
            lan_dhcpv4_exclusions = form.lan_dhcpv4_exclusions.data,
            lan_dhcpv4_excluded_first = form.lan_dhcpv4_excluded_first.data,
            lan_dhcpv4_excluded_last = form.lan_dhcpv4_excluded_last.data,
            ipv4_network_address = ipv4_network_address,
            ipv4_hostmask = ipv4_hostmask,
            ipv4_subnet_mask = ipv4_subnet_mask,
            wan_technology_type = form.wan_technology_type.data,
            wan_auth_type = form.wan_auth_type.data,
            rtr_vendor = form.rtr_vendor.data,
            rtr_series = form.rtr_series.data
        )
    return render_template(
        "home.html",
        form=form
    )