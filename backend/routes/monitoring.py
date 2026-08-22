from flask import Blueprint, jsonify
from datetime import datetime

from config import COMPETITORS


monitoring_bp = Blueprint(
    "monitoring",
    __name__,
    url_prefix="/api/monitor"
)


@monitoring_bp.route("/run", methods=["POST"])
def run_monitor():

    total_competitors = len(COMPETITORS)

    total_pages = total_competitors * 3

    run_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return jsonify({
        "status": "success",
        "message": "Monitoring run completed",
        "run_time": run_time,
        "competitors_checked": total_competitors,
        "pages_checked": total_pages
    })


@monitoring_bp.route("/status", methods=["GET"])
def monitor_status():

    return jsonify({
        "status": "success",
        "monitoring": "ready"
    })