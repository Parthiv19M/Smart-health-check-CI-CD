"""Smart Health CI/CD Flask application."""
from flask import Flask, jsonify


def create_app(test_config=None):
    """Create and configure the Flask application.

    Args:
        test_config (dict, optional): Test configuration. Defaults to None.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)

    if test_config is not None:
        app.config.update(test_config)

    @app.route('/')
    def index():
        ""
        Return a welcome message.

        Returns:
            JSON: A welcome message.
        """
        return jsonify({"message": "Smart Health CI/CD — Hello!"})

    @app.route('/health')
    def health():
        ""
        Health check endpoint.

        Returns:
            JSON: Status of the application.
        """
        return jsonify({"status": "ok"})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5001)
