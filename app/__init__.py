"""ATLAS - Automated Testing and Logging Analysis System.

This package serves as the main entry point for the ATLAS application.
It initializes the Flask application, configures extensions, and registers
all blueprints and routes.
"""

import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def create_app(config_name: str = None) -> Flask:
    """Application factory function.

    Creates and configures the Flask application instance based on the
    provided configuration name or the APP_ENV environment variable.

    Args:
        config_name: The configuration environment to use.
                     Defaults to the APP_ENV env var or 'development'.

    Returns:
        A configured Flask application instance.
    """
    app = Flask(__name__, instance_relative_config=True)

    # Determine configuration environment
    env = config_name or os.getenv("APP_ENV", "development")

    # Load base configuration
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev-secret-key-change-in-production"),
        DATABASE_URL=os.getenv("DATABASE_URL", "sqlite:///atlas.db"),
        DEBUG=env == "development",
        TESTING=env == "testing",
        LOG_LEVEL=os.getenv("LOG_LEVEL", "INFO"),
        MAX_CONTENT_LENGTH=int(os.getenv("MAX_CONTENT_LENGTH", 16 * 1024 * 1024)),
    )

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError as e:
        app.logger.warning("Could not create instance path: %s", e)

    _register_extensions(app)
    _register_blueprints(app)
    _configure_logging(app)

    app.logger.info("ATLAS application initialized in '%s' mode.", env)

    return app


def _register_extensions(app: Flask) -> None:
    """Initialize and register Flask extensions with the application.

    Args:
        app: The Flask application instance.
    """
    # Extensions will be imported and initialized here as they are added
    # e.g., db.init_app(app), migrate.init_app(app, db), etc.
    pass


def _register_blueprints(app: Flask) -> None:
    """Register all application blueprints.

    Args:
        app: The Flask application instance.
    """
    # Blueprints will be registered here as routes are added
    # e.g.:
    # from app.api.v1 import api_v1_bp
    # app.register_blueprint(api_v1_bp, url_prefix="/api/v1")

    @app.route("/health")
    def health_check():
        """Basic health check endpoint."""
        return {"status": "ok", "service": "ATLAS"}, 200


def _configure_logging(app: Flask) -> None:
    """Configure application-level logging.

    Args:
        app: The Flask application instance.
    """
    import logging

    log_level = getattr(logging, app.config.get("LOG_LEVEL", "INFO").upper(), logging.INFO)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    app.logger.setLevel(log_level)
