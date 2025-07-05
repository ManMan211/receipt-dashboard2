import streamlit as st
from datetime import datetime
import random
import json
from utils.export import export_receipt_as_pdf

# Load merchant templates
def load_templates():
    try:
        with open("templates/sample.json", "r") as f:
            return json.load(f)
    except:
        return {}

MERCHANTS = load_templates()

st.set_page_config(page_title="Receipt Dashboard", layout="centered")
st.title("🧾 Receipt Generator")

if not MERCHANTS:
    st.warning("No merchants loaded. Add a valid JSON template in /templates/sample.json")
else:
    merchant = st.selectbox("Choose a Merchant", list(MERCHANTS.keys()))
    receipt_time = st.time_input("Select Time", datetime.now().time())
    receipt_date = st.date_input("Select Date", datetime.now().date())
    notes = st.text_area("Add any notes (optional)")

    if st.button("Generate Receipt"):
        data = MERCHANTS[merchant]
        items = random.sample(data["items"], k=len(data["items"]))
        total = round(random.uniform(5.0, 50.0), 2)

        st.markdown("---")
        st.text(f"{merchant.upper()}")
        st.text(data["address"])
        st.text(f"Date: {receipt_date.strftime('%d/%m/%Y')}")
        st.text(f"Time: {receipt_time.strftime('%H:%M:%S')}")
        st.markdown("---")
        for item in items:
            st.text(f"{item:<20}  £{round(random.uniform(0.99, 9.99), 2):>5}")
        st.markdown("---")
        st.text(f"{'TOTAL':<20}  £{total:>5}")
        if notes:
            st.markdown("---")
            st.text("Notes: " + notes)

        export_receipt_as_pdf(merchant, receipt_date, receipt_time, items, total, notes)
