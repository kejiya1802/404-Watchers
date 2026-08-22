from flask import Blueprint, jsonify
from config import COMPETITORS


competitors_bp = Blueprint(
    "competitors",
    __name__,
    url_prefix="/api/competitors"
)


@competitors_bp.route("/", methods=["GET"])
def get_competitors():

    return jsonify({
        "status": "success",
        "total": len(COMPETITORS),
        "competitors": COMPETITORS
    })


@competitors_bp.route("/<int:competitor_id>", methods=["GET"])
def get_competitor(competitor_id):

    competitor = next(
        (
            company
            for company in COMPETITORS
            if company["id"] == competitor_id
        ),
        None
    )

    if competitor is None:
        return jsonify({
            "status": "error",
            "message": "Competitor not found"
        }), 404

    return jsonify({
        "status": "success",
        "competitor": competitor
    })