from dataclasses import dataclass
from typing import  Dict


@dataclass
class WordStat:
    word: str
    count: int
    word_in_row: Dict[int, int]

