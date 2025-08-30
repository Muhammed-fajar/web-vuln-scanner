import os, json, datetime
from html import escape
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_reports(results, outdir="reports"):
    os.makedirs(outdir, exist_ok=True)
    stamp = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    json_path = os.path.join(outdir, f"{stamp}.json")
    html_path = os.path.join(outdir, f"{stamp}.html")
    pdf_path = os.path.join(outdir, f"{stamp}.pdf")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Simple HTML report
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("<html><body><h1>WVS Report</h1>")
        for fnd in results.get("findings", []):
            f.write(f"<p><b>{escape(fnd.get('title',''))}</b> - {escape(fnd.get('url',''))} - {escape(fnd.get('severity',''))}</p>")
        f.write("</body></html>")

    # Simple PDF report
    try:
        c = canvas.Canvas(pdf_path, pagesize=letter)
        w, h = letter
        x, y = 40, h-40
        c.setFont("Helvetica-Bold", 14)
        c.drawString(x, y, "WVS Report")
        y -= 20
        c.setFont("Helvetica", 10)
        for fnd in results.get("findings", []):
            if y < 50:
                c.showPage()
                y = h-40
            c.drawString(x, y, f"{fnd.get('severity','')} - {fnd.get('title','')} - {fnd.get('url','')}")
            y -= 12
        c.save()
    except:
        pass

    return {"json": json_path, "html": html_path, "pdf": pdf_path}
