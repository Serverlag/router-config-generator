from __init__ import app
from flask import render_template
from forms import configForm
import ipaddress
# TODO: #3 Deploy app using gunicorn
@app.route("/", methods=["GET", "POST"])
def home():
    form = configForm()
    if form.validate_on_submit():
        ipInterface = ipaddress.ip_interface(form.lanIPv4Address.data+form.lanIPv4CidrPrefixSize.data)
        ipv4NetworkAddress = str(ipInterface.network).split('/')[0]
        ipv4HostMask = str(ipInterface.hostmask).split('/')[0]
        ipv4SubnetMask = str(ipInterface.netmask)
        return render_template(
            "generate.html",
            form=form,
            rtrHostname = form.rtrHostname.data,
            dnsSuffix = form.dnsSuffix.data,
            tzName = form.tzName.data,
            tzOffset = form.tzOffset.data,
            dnsResolverPrimaryIPv4 = form.dnsResolverPrimaryIPv4.data,
            dnsResolverSecondaryIPv4 = form.dnsResolverSecondaryIPv4.data,
            dnsResolverPrimaryIPv6 = form.dnsResolverPrimaryIPv6.data,
            dnsResolverSecondaryIPv6 = form.dnsResolverSecondaryIPv6.data,
            rtrAdminUsername = form.rtrAdminUsername.data,
            rtrAdminPassword = form.rtrAdminPassword.data,
            lanIPv4Address = form.lanIPv4Address.data,
            lanIPv4CidrPrefixSize = form.lanIPv4CidrPrefixSize.data,
            ipv4NetworkAddress = ipv4NetworkAddress,
            ipv4HostMask = ipv4HostMask,
            ipv4SubnetMask = ipv4SubnetMask,
            wanTechnologyType = form.wanTechnologyType.data,
            wanAuthType = form.wanAuthType.data,
            rtrVendor = form.rtrVendor.data,
            rtrSeries = form.rtrSeries.data
        )
    return render_template(
        "home.html",
        form=form,
        template="form-template"
    )