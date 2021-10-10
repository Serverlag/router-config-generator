from datetime import datetime
from flask import Flask, config, redirect, render_template, url_for
from . import app
from .forms import configForm

@app.route("/", methods=["GET", "POST"])
def home():
    form = configForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "home.html",
        form=form,
        template="form-template"
    )