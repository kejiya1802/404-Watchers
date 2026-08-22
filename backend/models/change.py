from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Change:
    competitor_id: int
    competitor_name: str
    page_type: str
    url: str

    change_type: str

    added: list
    removed: list

    detected_at: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def create(
        cls,
        competitor_id,
        competitor_name,
        page_type,
        url,
        change_type,
        added,
        removed
    ):
        return cls(
            competitor_id=competitor_id,
            competitor_name=competitor_name,
            page_type=page_type,
            url=url,
            change_type=change_type,
            added=added,
            removed=removed,
            detected_at=datetime.now().isoformat()
        )