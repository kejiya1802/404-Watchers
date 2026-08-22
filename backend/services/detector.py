def detect_change(
    old_text,
    new_text,
    page_type=""
):
    """
    Detect whether a page has changed.
    """

    if not old_text:

        return {
            "changed": True,
            "type": "new_page",
            "reason": "No previous snapshot exists"
        }

    if old_text == new_text:

        return {
            "changed": False,
            "type": "no_change",
            "reason": "Page is identical"
        }

    # Pricing-specific detection
    if page_type == "pricing":

        return {
            "changed": True,
            "type": "pricing_change",
            "reason": "Pricing page content changed"
        }

    # Changelog-specific detection
    if page_type == "changelog":

        return {
            "changed": True,
            "type": "product_update",
            "reason": "Changelog content changed"
        }

    # Careers-specific detection
    if page_type == "careers":

        return {
            "changed": True,
            "type": "career_change",
            "reason": "Careers page content changed"
        }

    return {
        "changed": True,
        "type": "content_change",
        "reason": "Page content changed"
    }