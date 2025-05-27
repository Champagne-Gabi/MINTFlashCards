import streamlit as st

st.set_page_config(page_title="Safety Flashcards - MINT Package", layout="wide")

st.title("🧠 Flashcards: MINT Package for Safeties")

# Define flashcards for MINT package (Safeties only)
flashcards = [
    {
        "term": "Base MINT Alignment",
        "definition": "Safeties are typically aligned in a 2-high shell, ~10-12 yards deep. Free Safety (FS) aligns to field, Strong Safety (SS) to boundary."
    },
    {
        "term": "Motion Adjustments in MINT",
        "definition": "Safeties communicate motion calls: STAR may bump, SS may spin down, FS rotates depending on coverage check (e.g. Cloud, Thin)."
    },
    {
        "term": "Coverage Responsibility - FS",
        "definition": "FS usually plays over the top of #2 to the field. Reads #2's release for vertical threats or inside/outside breaks."
    },
    {
        "term": "Coverage Responsibility - SS",
        "definition": "SS plays boundary support. May rotate into box or curl/flat depending on check (e.g. Trap, Robber, Buzz). Reads #2 to #1."
    },
    {
        "term": "MINT Check: Empty",
        "definition": "Safeties check out of MINT into an Empty adjustment (e.g. Play Out). STAR or SS may have to flex wide to account for #3."
    },
    {
        "term": "MINT vs 3x1",
        "definition": "FS takes over top of trips. SS aligns to boundary. May require a push call to adjust coverage balance."
    }
]

# Flashcard state
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

current = flashcards[st.session_state.card_index]

st.header(current["term"])
st.write(current["definition"])

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅️ Previous"):
        st.session_state.card_index = (st.session_state.card_index - 1) % len(flashcards)

with col2:
    if st.button("Next ➡️"):
        st.session_state.card_index = (st.session_state.card_index + 1) % len(flashcards)

st.caption("Use the arrows to cycle through flashcards for MINT package (Safeties focus).")
