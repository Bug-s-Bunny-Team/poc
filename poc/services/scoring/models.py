from dataclasses import dataclass

@dataclass
class ToAnalyze:
    id: str
    caption: str
    labels: set[str]
    hashtags: set[str]
