from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_pj"

from app import views
