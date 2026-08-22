import difflib


def compare_text(old_text, new_text):
    """
    Compare old and new webpage text.
    """

    old_lines = old_text.splitlines()
    new_lines = new_text.splitlines()

    diff = list(
        difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile="Previous Run",
            tofile="Current Run",
            lineterm=""
        )
    )

    added = []
    removed = []

    for line in diff:

        if line.startswith("+") and not line.startswith("+++"):
            added.append(line[1:].strip())

        elif line.startswith("-") and not line.startswith("---"):
            removed.append(line[1:].strip())

    changed = len(added) > 0 or len(removed) > 0

    return {
        "changed": changed,
        "added": added,
        "removed": removed,
        "diff": diff
    }


def similarity_score(old_text, new_text):
    """
    Calculate similarity between two versions.
    """

    return difflib.SequenceMatcher(
        None,
        old_text,
        new_text
    ).ratio()