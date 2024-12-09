from flask import Flask
from routes import api_routes  # Import blueprint
from database import init_db

app = Flask(__name__)

# Register blueprint once with a URL prefix '/api'
app.register_blueprint(api_routes, url_prefix='/api')

@app.route("/")  # Root route
def home():
    return "Welcome to the Library Management System!"

if __name__ == "__main__":
    init_db()  # Initialize the database
    app.run(debug=True)  # Start the server
