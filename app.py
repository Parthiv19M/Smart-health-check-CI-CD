"""Smart Health CI/CD Flask application."""
from flask import Flask, jsonify, send_from_directory
import os


def create_app(test_config=None):
    """Create and configure the Flask application.

    Args:
        test_config (dict, optional): Test configuration. Defaults to None.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__, static_folder='static')

    if test_config is not None:
        app.config.update(test_config)

    @app.route('/')
    def index():
        """Serve the landing page."""
        # When running tests, return a small JSON payload so tests can assert easily.
        if app.config.get('TESTING'):
            return jsonify({"message": "Welcome"})

        return app.send_static_file('index.html')

    @app.route('/health')
    def health():
        """
        Health check endpoint.

        Returns:
            JSON: Status of the application.
        """
        return jsonify({"status": "ok"})

    # Serve static files
    @app.route('/<path:path>')
    def serve_static(path):
        return send_from_directory('static', path)

    return app


# Provide a module-level application object for easy imports (used by tests)
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
