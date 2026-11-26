@echo off
REM Double-clic : installe (la premiere fois) puis lance Finance Learning.
cd /d "%~dp0"
where python >nul 2>nul || (echo Python nest pas installe : https://www.python.org/downloads/ & pause & exit /b 1)
if not exist .venv\Scripts\streamlit.exe (
  echo Premiere ouverture : installation, 1 a 2 minutes...
  python -m venv .venv || (pause & exit /b 1)
  .venv\Scripts\python -m pip install -q --upgrade pip
  .venv\Scripts\pip install -q -r requirements.txt || (pause & exit /b 1)
)
start "" http://localhost:8502
.venv\Scripts\streamlit run app.py --server.port 8502 --server.headless true
