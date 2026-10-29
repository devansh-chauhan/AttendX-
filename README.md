# AttendX AI

> A local-first face-recognition attendance prototype built with Python, Streamlit, OpenCV, InsightFace, and SQLite.

AttendX AI provides student registration, local face enrollment, live camera-based recognition, attendance records, analytics, and downloadable reports.

## Features

- Student registration and profile management
- Local face enrollment and embedding generation with InsightFace
- Live attendance with unknown-face, low-light, distance, and multi-face checks
- One attendance record per student per day
- Attendance dashboard, reports, charts, CSV export, and PDF export
- Local SQLite data storage

## Technology

Python · Streamlit · OpenCV · InsightFace · ONNX Runtime · SQLite · NumPy · Pandas · Pillow · ReportLab · QRCode

## Local setup

Prerequisite: Python 3.11 is recommended.

```bash
git clone https://github.com/YOUR-USERNAME/AttendX-AI.git
cd AttendX-AI
python -m venv venv
```

Activate the environment:

```powershell
# Windows PowerShell
venv\Scripts\Activate.ps1
```

```bash
# macOS/Linux
source venv/bin/activate
```

Install dependencies and initialize an empty local database:

```bash
pip install -r requirements.txt
python database/schema.py
streamlit run app.py
```

The app opens at `http://localhost:8501`. A webcam must be connected and permissions granted to the local Python process.

## Data privacy and repository policy

This project processes biometric data. **Do not commit or upload real student data.** The repository deliberately ignores:

- Face photos, embeddings, ID cards, QR codes, attendance exports, and reports
- `database.db` and every local SQLite database
- API keys, `.env` files, Streamlit secrets, virtual environments, and build output

Before sharing screenshots or a demo, use only fictional or consented test identities. The software is an educational prototype and does not include liveness detection, authentication, role-based access controls, consent workflows, or production-grade biometric security.

## Deployment note

The current attendance and enrollment workflow calls `cv2.VideoCapture(0)`. On a hosted service, that targets the server's camera—not a visitor's browser camera—so it is intended for local use.

For a public demo, use one of these approaches:

1. Host a read-only dashboard with fictional sample data and no biometric records.
2. Refactor camera capture to a browser-camera component, then process only consented demo images and use secure external storage.
3. Demonstrate the full recognition flow locally through a recorded video, while hosting only the project documentation and safe dashboard preview.

Local SQLite files are also not durable on many free hosting services. A production version would need authenticated access, secure cloud storage, retention/deletion controls, consent management, liveness detection, and an appropriate legal/privacy review.

## Project structure

```text
app.py                 Streamlit entry point
pages/                 Dashboard, student, attendance, and reporting pages
modules/               Attendance, enrollment, reporting, and student logic
models/                InsightFace recognition engine
database/              SQLite connection and schema
assets/                Public visual assets only
data/                  Local runtime data (ignored by Git)
```

## License

Add a license before making a public release. The recommended default for a portfolio or academic project is MIT, provided all bundled assets and dependencies permit it.
