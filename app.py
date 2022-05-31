from flask import Flask
from extensions import extensions
from routes.routes import home
from flask_socketio import SocketIO, emit
import os

db_dir = os.path.abspath(os.path.dirname(__file__)) + "/database"
print(db_dir)

db = extensions.db
migrate = extensions.migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fights.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(db_dir, 'fights.db')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.init_app(app, db, render_as_batch=True)
app.register_blueprint(home)
socketio = SocketIO(app, cors_allowed_origins='*')

# Handler for a message received over 'connect' channel
@socketio.on('connect')
def test_connect():
    emit('after connect', {'data': 'Lets dance'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
