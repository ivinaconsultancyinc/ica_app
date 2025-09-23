# insurance_app/routers/routers_dashboard.py

from fastapi import APIRouter, Request, Depends

from fastapi.responses import HTMLResponse, StreamingResponse

from sqlalchemy.orm import Session

from insurance_app.connection import get_db

from insurance_app.models.models import Claim

from fastapi.templating import Jinja2Templates

import pandas as pd

import io

from datetime import datetime

from reportlab.lib.pagesizes import letter

from reportlab.pdfgen import canvas

router = APIRouter()

templates = Jinja2Templates(directory="insurance_app/templates")

LRD_TO_USD = 0.005  # Example rate

def claims_by_month(db: Session, currency: str = "LRD"):

    claims = db.query(Claim).all()

    data = []

    for claim in claims:

        if claim.filed_date:

            month = datetime.strptime(claim.filed_date, "%Y-%m-%d").strftime("%Y-%m")

            amount = claim.amount if claim.amount else 0

            if currency == "USD":

                amount *= LRD_TO_USD

            data.append({"month": month, "amount": amount})

    df = pd.DataFrame(data)

    if df.empty:

        return []

    grouped = df.groupby("month").agg(count=("amount", "size"), total_value=("amount", "sum")).reset_index()

    return grouped.to_dict(orient="records")

@router.get("/dashboard", response_class=HTMLResponse)

async def dashboard(request: Request, db: Session = Depends(get_db), currency: str = "LRD"):

    analytics = claims_by_month(db, currency)

    project_tree = [

        "insurance_app/",

        "├── main.py",

        "├── routers/",

        "│   └── routers_dashboard.py",

        "├── templates/",

        "│   └── dashboard.html",

        "├── static/",

        "│   └── dashboard.js"

    ]

    return templates.TemplateResponse("dashboard.html", {

        "request": request,

        "analytics": analytics,

        "currency": currency,

        "project_tree": project_tree

    })

@router.get("/dashboard/export/excel")

async def export_excel(db: Session = Depends(get_db), currency: str = "LRD"):

    analytics = claims_by_month(db, currency)

    df = pd.DataFrame(analytics)

    output = io.BytesIO()

    df.to_excel(output, index=False)

    output.seek(0)

    return StreamingResponse(output, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

                            headers={"Content-Disposition": "attachment; filename=claims_by_month.xlsx"})

@router.get("/dashboard/export/pdf")

async def export_pdf(db: Session = Depends(get_db), currency: str = "LRD"):

    analytics = claims_by_month(db, currency)

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer, pagesize=letter)

    width, height = letter

    p.setFont("Helvetica-Bold", 16)

    p.drawString(50, height - 50, "Claims by Month Report")

    p.setFont("Helvetica", 12)

    p.drawString(50, height - 80, f"Currency: {currency}")

    y = height - 120

    p.drawString(50, y, "Month")

    p.drawString(150, y, "Claim Count")

    p.drawString(300, y, f"Total Value ({currency})")

    y -= 20

    for row in analytics:

        p.drawString(50, y, str(row['month']))

        p.drawString(150, y, str(row['count']))

        p.drawString(300, y, f"{row['total_value']:.2f}")

        y -= 20

        if y < 50:

            p.showPage()

            y = height - 50

    p.save()

    buffer.seek(0)

    return StreamingResponse(buffer, media_type="application/pdf",

                            headers={"Content-Disposition": "attachment; filename=claims_by_month.pdf"})

 

login.html
