from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def generate_pdf(df, filename):

    pdf = SimpleDocTemplate(filename)

    data = [list(df.columns)]

    data += df.values.tolist()

    table = Table(data)

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("ALIGN", (0, 0), (-1, -1), "CENTER")
        ])
    )

    pdf.build([table])