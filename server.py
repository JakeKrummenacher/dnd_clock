from flask_app import app
from flask_app.controllers import worlds, cost_trackers

if __name__ == "__main__":
    app.run(debug=True)