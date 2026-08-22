from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Snapshot:
    competitor_id: int
    competitor_name: str
    page_type: str
    url: str
    content: str
    created_at: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def create(
        cls,
        competitor_id,
        competitor_name,
        page_type,
        url,
        content
    ):
        return cls(
            competitor_id=competitor_id,
            competitor_name=competitor_name,
            page_type=page_type,
            url=url,
            content=content,
            created_at=datetime.now().isoformat()
        )