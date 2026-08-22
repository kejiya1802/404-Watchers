from flask import Blueprint, jsonify


changes_bp = Blueprint(
    "changes",
    __name__,
    url_prefix="/api/changes"
)


# Temporary data
# Later this will come from the database.

changes = []


@changes_bp.route("/", methods=["GET"])
def get_changes():

    if not changes:

        return jsonify({
            "status": "success",
            "total_changes": 0,
            "message": "Nothing changed",
            "changes": []
        })

    return jsonify({
        "status": "success",
        "total_changes": len(changes),
        "changes": changes
    })


@changes_bp.route("/latest", methods=["GET"])
def latest_changes():

    return jsonify({
        "status": "success",
        "changes": changes
    })