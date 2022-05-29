from flask import Flask
from extensions import extensions
from routes.routes import home

db = extensions.db
migrate = extensions.migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fights.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.init_app(app, db, render_as_batch=True)
app.register_blueprint(home)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
