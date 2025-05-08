# Import Flask and the API Blueprint
from flask import Flask
from MyBot.API.routes import bp  


def create_app():
    """
    Factory function to create and configure the Flask app.

    - Registers all API routes under the app.
    - Keeps app setup modular and easier to expand later.
    """
    app = Flask(__name__)
    app.register_blueprint(bp)  # Attach API routes to the app
    return app

if __name__ == "__main__":
    # Only run this if the script is executed directly (not imported)
    app = create_app()
    # Start the Flask server on localhost (port 5000 by default)
    app.run(debug=True)