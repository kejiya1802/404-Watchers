import json

from database.db import (
    execute_query,
    insert
)


# ============================================================
# COMPETITORS
# ============================================================

def add_competitor(
    name,
    pricing_url,
    changelog_url,
    careers_url
):

    query = """
        INSERT INTO competitors (
            name,
            pricing_url,
            changelog_url,
            careers_url
        )
        VALUES (?, ?, ?, ?)
    """

    return insert(
        query,
        (
            name,
            pricing_url,
            changelog_url,
            careers_url
        )
    )


def get_competitors():

    query = """
        SELECT *
        FROM competitors
        ORDER BY id
    """

    rows = execute_query(
        query,
        fetch=True
    )

    return [
        dict(row)
        for row in rows
    ]


# ============================================================
# SNAPSHOTS
# ============================================================

def save_snapshot(
    competitor_id,
    competitor_name,
    page_type,
    url,
    content,
    created_at
):

    query = """
        INSERT INTO snapshots (
            competitor_id,
            competitor_name,
            page_type,
            url,
            content,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """

    return insert(
        query,
        (
            competitor_id,
            competitor_name,
            page_type,
            url,
            content,
            created_at
        )
    )


def get_latest_snapshot(
    competitor_id,
    page_type
):

    query = """
        SELECT *
        FROM snapshots
        WHERE competitor_id = ?
        AND page_type = ?
        ORDER BY id DESC
        LIMIT 1
    """

    rows = execute_query(
        query,
        (
            competitor_id,
            page_type
        ),
        fetch=True
    )

    if not rows:

        return None

    return dict(rows[0])


# ============================================================
# CHANGES
# ============================================================

def save_change(
    competitor_id,
    competitor_name,
    page_type,
    url,
    change_type,
    added,
    removed,
    detected_at
):

    query = """
        INSERT INTO changes (
            competitor_id,
            competitor_name,
            page_type,
            url,
            change_type,
            added,
            removed,
            detected_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """

    return insert(
        query,
        (
            competitor_id,
            competitor_name,
            page_type,
            url,
            change_type,
            json.dumps(added),
            json.dumps(removed),
            detected_at
        )
    )


def get_changes():

    query = """
        SELECT *
        FROM changes
        ORDER BY id DESC
    """

    rows = execute_query(
        query,
        fetch=True
    )

    results = []

    for row in rows:

        item = dict(row)

        item["added"] = json.loads(
            item["added"] or "[]"
        )

        item["removed"] = json.loads(
            item["removed"] or "[]"
        )

        results.append(item)

    return results


# ============================================================
# CLEAR DATABASE
# ============================================================

def clear_changes():

    query = """
        DELETE FROM changes
    """

    execute_query(query)


def clear_snapshots():

    query = """
        DELETE FROM snapshots
    """

    execute_query(query)