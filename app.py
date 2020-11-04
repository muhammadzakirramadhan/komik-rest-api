from flask import Flask
from lib.route import Router

app = Flask(__name__)
app.config["DEBUG"] = True

Router.run(app)