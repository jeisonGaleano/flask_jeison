from api.routes.cmc import cmc
from api.routes.chevrolet import chevrolet
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


app.register_blueprint(chevrolet)
app.register_blueprint(cmc)

if __name__ == "__main__":
    app.run()
