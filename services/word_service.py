import re
from typing import Dict
from fastapi import UploadFile, File, HTTPException
from models.WordStat import WordStat
import stanza

nlp = stanza.Pipeline("ru", processors='tokenize,lemma', use_gpu=False)

def normalize_word(word: str) -> str:
    doc = nlp(word)
    return doc.sentences[0].words[0].lemma


def calculate_word_count(file: UploadFile = File(...)):
    words: Dict[str, WordStat] = {}
    line_n = 0

    for line in file.file:
        line_n += 1

        if isinstance(line, bytes):
            line = line.decode("utf-8")

        line = line.strip()
        tokens = re.findall(r"\w+", line)

        for word in tokens:
            normalized = normalize_word(word)

            if normalized not in words:
                words[normalized] = WordStat(word=normalized, count=1, word_in_row={})

            stat = words[normalized]
            stat.count += 1

            if line_n not in stat.word_in_row:
                stat.word_in_row[line_n] = 0

            stat.word_in_row[line_n] += 1

    if not words:
        raise HTTPException(status_code=400, detail="File is empty")

    return words, line_n



