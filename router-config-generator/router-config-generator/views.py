from datetime import datetime
from flask import Flask, config, render_template
from . import app
from .forms import configForm

@app.route("/", methods=["GET", "POST"])
def home():
    form = configForm()
    if form.validate_on_submit():
        return render_template(
            "generate.html",
            form=form,
            rtrHostname = form.rtrHostname.data,
            dnsSuffix = form.dnsSuffix.data,
            tzName = form.tzName.data,
            tzOffset = form.tzOffset.data,
            dnsResolverPrimary = form.dnsResolverPrimary.data,
            dnsResolverSecondary = form.dnsResolverSecondary.data,
            rtrAdminUsername = form.rtrAdminUsername.data,
            rtrAdminPassword = form.rtrAdminPassword.data,
            lanIPAddress = form.lanIPAddress.data,
            lanCidrPrefixSize = form.lanCidrPrefixSize.data,
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