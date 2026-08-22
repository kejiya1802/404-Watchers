from datetime import datetime


def create_report(
    company,
    page_type,
    url,
    comparison,
    detection
):
    """
    Create a structured change report.
    """

    if not detection["changed"]:

        return {
            "company": company,
            "page": page_type,
            "changed": False,
            "message": "Nothing changed",
            "url": url
        }

    return {
        "company": company,
        "page": page_type,
        "changed": True,
        "change_type": detection["type"],
        "reason": detection["reason"],
        "added": comparison["added"],
        "removed": comparison["removed"],
        "diff": comparison["diff"],
        "url": url,
        "detected_at": datetime.now().isoformat()
    }


def create_summary(reports):
    """
    Create overall monitoring summary.
    """

    changed = [
        report
        for report in reports
        if report["changed"]
    ]

    unchanged = [
        report
        for report in reports
        if not report["changed"]
    ]

    return {
        "total_pages": len(reports),
        "changed_pages": len(changed),
        "unchanged_pages": len(unchanged),
        "changes": changed,
        "unchanged": unchanged
    }