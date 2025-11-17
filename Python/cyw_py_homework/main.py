# Flask Microservice Inventory Management System
# AI Assisted Lab Project
from flask import Flask, render_template, redirect, url_for, request
from flask_cors import CORS

def create_app():
    """Application factory function"""
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # Configuration
    app.config['SECRET_KEY'] = 'dev-secret-key-2023'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Enable CORS
    CORS(app)

    # Initialize database
    from models import db
    db.init_app(app)

    # Register error handlers
    from error_handlers import register_error_handlers
    register_error_handlers(app)

    # Register blueprints
    from routes.products import product_bp
    from routes.stock import stock_bp
    from routes.logs import log_bp

    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(stock_bp, url_prefix='/api/stock')
    app.register_blueprint(log_bp, url_prefix='/api/logs')

    # Main blueprint for web pages
    from routes.main import main_bp
    app.register_blueprint(main_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app

# 创建应用实例供 Gunicorn 使用
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)