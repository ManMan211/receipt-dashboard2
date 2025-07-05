from fpdf import FPDF
import os
from datetime import datetime
import random

def export_receipt_as_pdf(merchant, date, time, items, total, notes):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"{merchant} Receipt", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Date: {date}  Time: {time}", ln=True, align='C')
    pdf.ln(10)
    for item in items:
        pdf.cell(200, 10, txt=f"{item:<20} £{round(1 + 9 * random.random(), 2):>5}", ln=True)
    pdf.cell(200, 10, txt=f"TOTAL: £{total}", ln=True)
    if notes:
        pdf.ln(10)
        pdf.multi_cell(0, 10, txt=f"Notes: {notes}")
    if not os.path.exists("exports"):
        os.makedirs("exports")
    filename = f"exports/receipt_{merchant}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    pdf.output(filename)
