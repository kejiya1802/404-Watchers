from flask import Flask, jsonify
from flask_cors import CORS

from config import (
    APP_NAME,
    HOST,
    PORT,
    DEBUG
)

from database.db import init_database

from routes.competitors import competitors_bp
from routes.monitoring import monitoring_bp
from routes.changes import changes_bp


# ============================================================
# CREATE FLASK APPLICATION
# ============================================================

app = Flask(__name__)

# Allow frontend to communicate with backend
CORS(app)


# ============================================================
# REGISTER API ROUTES
# ============================================================

app.register_blueprint(competitors_bp)
app.register_blueprint(monitoring_bp)
app.register_blueprint(changes_bp)


# ============================================================
# HOME
# ============================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "app": APP_NAME,
        "message": "Watcher Backend is running!",
        "status": "success"
    })


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route("/api/health", methods=["GET"])
def health_check():

    return jsonify({
        "status": "success",
        "message": "Backend API is healthy"
    })


# ============================================================
# 404 ERROR
# ============================================================

@app.errorhandler(404)
def page_not_found(error):

    return jsonify({
        "status": "error",
        "message": "API endpoint not found"
    }), 404


# ============================================================
# 500 ERROR
# ============================================================

@app.errorhandler(500)
def internal_server_error(error):

    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    # Create database and tables
    init_database()

    print("=" * 60)
    print(f"🚀 {APP_NAME}")
    print("=" * 60)
    print(f"🌐 Server  : http://{HOST}:{PORT}")
    print(f"❤️ Health  : http://{HOST}:{PORT}/api/health")
    print(f"👥 Competitors : http://{HOST}:{PORT}/api/competitors/")
    print(f"📊 Changes : http://{HOST}:{PORT}/api/changes/")
    print("=" * 60)

    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    )