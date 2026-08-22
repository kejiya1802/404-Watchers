from dataclasses import dataclass, asdict


@dataclass
class Competitor:
    id: int
    name: str
    pricing: str
    changelog: str
    careers: str

    def to_dict(self):
        return asdict(self)