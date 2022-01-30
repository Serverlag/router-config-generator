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
            ipv4_network_address = ipv4_network_address,
            ipv4_hostmask = ipv4_hostmask,
            ipv4_subnet_mask = ipv4_subnet_mask
        )
    return render_template(
        "home.html",
        form=form
    )