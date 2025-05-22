#app.py

from models.__init__ import create_app
#from utils.create_db import create_db

app, socketio = create_app()

if __name__ == "__main__":
    #create_db(app)
    socketio.run(app, host='0.0.0.0', port=8080, debug=False)
