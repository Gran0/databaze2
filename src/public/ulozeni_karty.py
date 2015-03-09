import os
# We require 're' module for validating email address with regular expression
import re
import datetime

# Using Flask since Python doesn't have built-in session management
# 'request' provides access to the incoming request data
# 'render_template' renders the template with the given parameters

from flask import Flask, session, request, render_template

app = Flask(__name__)

@app.route('/karty', methods=['GET','POST'])
def index():
    data = {'id' : '',
            'id_karty' : '',
            'datum_pristupu' : '',
            'datum_pridani_zaznamu' : '',
            }

    if request.method == "GET": # If the request is GET, render the form template.
          return render_template("public/formular.html")
    else:
        data['id_karty'] = request.form['cislo_karty'].strip()
        data['datum_pristupu'] = request.form['datum'].strip()
        cas = datetime.datetime.now()
        data['datum_pridani_zaznamu']= cas.strftime("%d.%m.%Y %H:%M")
        return render_template("public/formular.html")