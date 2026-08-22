from bs4 import BeautifulSoup


def parse_page(html):
    """
    Convert HTML into clean readable text.
    """

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    # Remove unnecessary elements
    for element in soup([
        "script",
        "style",
        "noscript",
        "svg",
        "nav",
        "footer"
    ]):

        element.decompose()

    text = soup.get_text(
        separator="\n"
    )

    # Clean empty lines
    lines = []

    for line in text.splitlines():

        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines)


def parse_title(html):
    """
    Extract webpage title.
    """

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    if soup.title:

        return soup.title.get_text(
            strip=True
        )

    return ""