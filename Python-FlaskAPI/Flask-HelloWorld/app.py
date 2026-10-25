from flask import Flask  # Import Flask module from flask package
app = Flask(__name__)  # Create a Flask application instance
@app.route('/')  # Define a route for the root URL
def home():
    return "Hello, World!"  # Return a simple response
if __name__ == '__main__': # Check if the script is run directly
    app.run(debug=True)  # Run the application in debug mode