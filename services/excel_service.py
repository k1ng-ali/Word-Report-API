from openpyxl import Workbook
from io import BytesIO

def write_to_excel(word_stat: dict, total_lines: int):
    wb = Workbook()
    ws = wb.active
    ws.title = "Words Stats"

    ws.append(["Слово", "Количество", "По строкам"])

    for word, stat in word_stat.items():
        row_count = []

        for i in range(1, total_lines + 1):
            row_count.append(str(stat.word_in_row.get(i,0)))

        row_str = ",".join(row_count)

        ws.append([word, stat.count, row_str])

    stream = BytesIO()
    wb.save(stream)
    stream.seek(0)

    return stream

