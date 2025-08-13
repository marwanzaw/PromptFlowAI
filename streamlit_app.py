
import json
import re
import streamlit as st

st.set_page_config(page_title="PromptFlowAI – Research Edition", layout="centered")
st.title("🎓 PromptFlowAI — Research Edition")
st.markdown("Generate high‑quality **academic prompts** in seconds. This edition focuses on research writing only.")

# --- Load prompts (Research only) ---
@st.cache_data
def load_prompts(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Force Research-only view (ignore any other categories if present)
    research = [p for p in data if p.get("category") == "Research"]
    # Fallback: if no category field, assume all are research
    return research or data

def extract_placeholders(template: str):
    return sorted(set(re.findall(r"\{([^}]+)\}", template)))

DATA_PATH = "research_prompts.json"

try:
    prompts = load_prompts(DATA_PATH)
except Exception as e:
    st.error(f"Could not load prompts from '{DATA_PATH}'. Make sure the file exists next to this app.\nError: {e}")
    st.stop()

titles = [p["title"] for p in prompts]
selected_title = st.selectbox("Select a research prompt:", titles)

selected_prompt = next(p for p in prompts if p["title"] == selected_title)

# Dynamic inputs based on detected placeholders
ph_keys = extract_placeholders(selected_prompt["prompt"])
with st.expander("Detected placeholders", expanded=True):
    st.write(", ".join(ph_keys) if ph_keys else "No inputs required.")

values = {}
for key in ph_keys:
    values[key] = st.text_input(f"Enter {key}")

# Generate
if st.button("Generate Prompt", type="primary"):
    out = selected_prompt["prompt"]
    for k, v in values.items():
        out = out.replace("{" + k + "}", v if v else "{" + k + "}")
    st.text_area("🔎 Final Prompt", out, height=240)
    st.download_button("📥 Download", out, file_name="prompt.txt")

st.markdown("---")
st.caption("Created by **Marwan Al Zawahra** · Research Edition")
