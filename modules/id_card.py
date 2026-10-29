import os
import qrcode

from PIL import Image, ImageDraw, ImageFont


def generate_qr(student_id):

    os.makedirs("data/qr", exist_ok=True)

    filename = f"data/qr/{student_id}.png"

    qr = qrcode.make(student_id)

    qr.save(filename)

    return filename


def generate_id_card(student, photo_path):

    os.makedirs("data/id_cards", exist_ok=True)

    qr_path = generate_qr(student[0])

    card = Image.new(
        "RGB",
        (700, 450),
        "white"
    )

    draw = ImageDraw.Draw(card)

    try:
        title_font = ImageFont.truetype("arial.ttf", 28)
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        title_font = ImageFont.load_default()
        font = ImageFont.load_default()

    # Header
    draw.rectangle(
        [(0, 0), (700, 70)],
        fill=(37, 99, 235)
    )

    draw.text(
        (20, 20),
        "AttendX AI - Student ID Card",
        fill="white",
        font=title_font
    )

    # Student Photo
    if photo_path and os.path.exists(photo_path):

        photo = Image.open(photo_path)

        photo = photo.resize((140, 170))

        card.paste(photo, (30, 100))

    # Student Details
    x = 200
    y = 100

    draw.text((x, y),     f"Name : {student[1]}", font=font, fill="black")
    draw.text((x, y+35),  f"ID : {student[0]}", font=font, fill="black")
    draw.text((x, y+70),  f"Department : {student[2]}", font=font, fill="black")
    draw.text((x, y+105), f"Semester : {student[3]}", font=font, fill="black")
    draw.text((x, y+140), f"Section : {student[4]}", font=font, fill="black")
    draw.text((x, y+175), f"Email : {student[5]}", font=font, fill="black")

    # QR Code
    qr = Image.open(qr_path)

    qr = qr.resize((130,130))

    card.paste(qr, (530, 270))

    draw.text(
        (500, 410),
        "Scan Student ID",
        font=font,
        fill="black"
    )

    filename = f"data/id_cards/{student[0]}_card.png"

    card.save(filename)

    return filename