import streamlit as st

st.set_page_config(page_title="Safety Flashcards - MINT Package", layout="centered")

st.title("📱 Safety Flashcards")

# Topic, Phase, and Role selectors
topic = st.selectbox("Select Install Topic:", ["MINT Package"])
phase_options = [
    "Phase 1: Core Structure & Personnel",
    "Phase 2: Pre-Snap Reads",
    "Phase 3: Motion Adjustments",
    "Phase 4: Coverage Responsibilities",
    "Phase 5: Terminology Recap"
]
phase = st.selectbox("Learning Phase:", phase_options)
role = st.selectbox("Choose your position:", ["All", "Free Safety (FS)", "Strong Safety (SS)"])

# Define flashcards for each phase
flashcards_by_phase = {
    # full expanded card content here (already discussed)
    # abbreviated here for clarity
    "Phase 1: Core Structure & Personnel": [...],
    "Phase 2: Pre-Snap Reads": [...],
    "Phase 3: Motion Adjustments": [...],
    "Phase 4: Coverage Responsibilities": [...],
    "Phase 5: Terminology Recap": [...]
}

# Get filtered cards by role
all_cards = flashcards_by_phase[phase]
filtered = [f for f in all_cards if role == "All" or f["role"] == role or f["role"] == "All"]

# Flashcard navigation state
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
if st.session_state.card_index >= len(filtered):
    st.session_state.card_index = len(filtered) - 1

current = filtered[st.session_state.card_index]

# Flashcard tracker display
card_num = st.session_state.card_index + 1
card_total = len(filtered)
st.markdown(f"<div style='text-align: center; font-size: 16px; color: gray;'>Card {card_num} of {card_total}</div>", unsafe_allow_html=True)

# Phone-style container
st.markdown(f"""
    <div style='background-color: #f0f2f6; border-radius: 30px; padding: 30px; max-width: 400px; margin: auto; box-shadow: 0px 0px 15px rgba(0,0,0,0.1);'>
        <h4 style='text-align: center;'>{current['term']}</h4>
        <p style='font-size: 18px; line-height: 1.5;'>{current['definition']}</p>
    </div>
    <br>
""", unsafe_allow_html=True)

# Navigation buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("⬅️ Previous"):
        if st.session_state.card_index > 0:
            st.session_state.card_index -= 1
with col2:
    if st.button("Next ➡️"):
        if st.session_state.card_index < len(filtered) - 1:
            st.session_state.card_index += 1

st.caption("Select a phase of learning, your role, and work through the key install concepts step-by-step.")

