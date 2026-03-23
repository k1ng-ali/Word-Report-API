from starlette.responses import StreamingResponse
from services.word_service import calculate_word_count
from services.excel_service import write_to_excel
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/public/report/export")
async def export_report(file: UploadFile = File(...)):
    stats, line_n = calculate_word_count(file)

    excel_file = write_to_excel(stats, line_n)

    return StreamingResponse(
        excel_file,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename=report.xlsx"},
    )



