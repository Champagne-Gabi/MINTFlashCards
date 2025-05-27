import streamlit as st
from PIL import Image

st.set_page_config(page_title="Safety Flashcards - MINT Package", layout="centered")

st.title("📱 Flashcards: MINT Package for Safeties")

# Define flashcards for MINT package (Safeties only)
flashcards = [
    {
        "term": "Base MINT Alignment",
        "definition": "In a standard MINT look, your safeties are gonna be deep—like 10 to 12 yards. FS lines up to the field, SS to the boundary. Think 2-high shell, ready to disguise or rotate based on what the offense gives you.",
        "image": None
    },
    {
        "term": "Motion Adjustments in MINT",
        "definition": "If the offense sends motion, you’ve gotta be loud and clear. STAR might bump out, SS could spin down, and FS has to be ready to rotate depending on what coverage check you’re in—like Cloud or Thin.",
        "image": None
    },
    {
        "term": "Coverage Responsibility - FS",
        "definition": "You’re reading #2 to the field. If he goes vertical? You stay on top. Inside break? Prepare to help inside. Your job is to erase the deep threat and support wherever the route breaks down.",
        "image": None
    },
    {
        "term": "Coverage Responsibility - SS",
        "definition": "You’re the enforcer on the boundary. Watch #2 to #1 and be ready to rotate into the curl/flat or the box, depending on the call—Trap, Robber, or Buzz might be coming your way.",
        "image": None
    },
    {
        "term": "MINT Check: Empty",
        "definition": "Offense lines up in Empty? Get ready to check out of MINT—probably into something like Play Out. STAR or SS might need to flex wide to take away that #3 quick game threat.",
        "image": None
    },
    {
        "term": "MINT vs 3x1",
        "definition": "Trips to the field? FS has to lean that way, usually over the top. SS stays to the boundary. You might hear a Push call to adjust who’s helping where.",
        "image": None
    }
]

# Flashcard state
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

current = flashcards[st.session_state.card_index]

# Phone-style container
st.markdown("""
    <div style='background-color: #f0f2f6; border-radius: 30px; padding: 30px; max-width: 400px; margin: auto; box-shadow: 0px 0px 15px rgba(0,0,0,0.1);'>
        <h4 style='text-align: center;'>{}</h4>
        <p style='font-size: 18px; line-height: 1.5;'>{}</p>
    </div>
    <br>
""".format(current["term"], current["definition"]), unsafe_allow_html=True)

# Show image if available
if current.get("image"):
    st.image(Image.open(current["image"]), caption="Diagram", use_column_width=True)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅️ Previous"):
        st.session_state.card_index = (st.session_state.card_index - 1) % len(flashcards)

with col2:
    if st.button("Next ➡️"):
        st.session_state.card_index = (st.session_state.card_index + 1) % len(flashcards)

st.caption("Tap through to review key safety concepts from the MINT package. Diagrams coming soon!")

