
# PromptFlowAI — Research Edition

A focused, five-file setup to generate **research-only** prompts for academic writing.

## Files
- `promptflowai.py` — creates/updates `research_prompts.json` with 10 academic prompts.
- `research_prompts.json` — the prompt pack used by the app.
- `streamlit_app.py` — Streamlit app (Research-only).
- `README.md` — this file.
- `PromptFlowAI_Research_Pack.docx` — printable version (export to PDF if needed).

## Run (Windows)
1. Open Command Prompt in the project folder.
2. Create/activate venv and install Streamlit (first time only):
   ```bat
   python -m venv .venv
   .venv\Scripts\activate
   pip install --upgrade pip
   pip install streamlit
   ```
3. (Optional) regenerate JSON:
   ```bat
   python promptflowai.py
   ```
4. Launch:
   ```bat
   streamlit run streamlit_app.py
   ```

## Usage
- Choose a research prompt.
- Fill detected placeholders (e.g., `{topic}`, `{input}`).
- Generate and download the final prompt.

> This edition intentionally focuses on **Research** to keep the product tight and ready for monetization later.
