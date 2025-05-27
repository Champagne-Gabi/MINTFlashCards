import streamlit as st
from PIL import Image

st.set_page_config(page_title="Safety Flashcards - MINT Package", layout="centered")

st.title("📱 Flashcards: MINT Package – Safeties")

# Role selector
role = st.selectbox("Choose your position:", ["All", "Free Safety (FS)", "Strong Safety (SS)"])

# Define flashcards
flashcards = [
    {
        "term": "Base MINT Alignment",
        "definition": "In a standard MINT look, safeties are deep—around 10 to 12 yards. FS is to the field, SS to the boundary. Think 2-high shell, disguise-ready.",
        "image": "A_digital_flashcards-style_interface_tailored_for_.png",
        "role": "All"
    },
    {
        "term": "Motion Adjustments in MINT",
        "definition": "If there’s motion, communicate. STAR bumps, SS might spin down, and FS may rotate into Thin or Cloud depending on the call.",
        "image": "A_digital_flashcards-style_interface_tailored_for_.png",
        "role": "All"
    },
    {
        "term": "Coverage Responsibility - FS",
        "definition": "You’re reading #2 to the field. Vertical? Stay on top. Inside break? Be ready to close. Eliminate the deep threat.",
        "image": "A_digital_flashcards-style_interface_tailored_for_.png",
        "role": "Free Safety (FS)"
    },
    {
        "term": "Coverage Responsibility - SS",
        "definition": "You’re the hammer on the boundary. Watch #2 to #1 and rotate into curl/flat or the box—especially in Trap, Robber, or Buzz.",
        "image": "A_digital_flashcards-style_interface_tailored_for_.png",
        "role": "Strong Safety (SS)"
    },
    {
        "term": "MINT Check: Empty",
        "definition": "If the offense shows Empty, check out of MINT. STAR or SS might flex wide to pick up #3. It’s about handling quick threats.",
        "image": "A_digital_flashcards-style_interface_tailored_for_.png",
        "role": "Strong Safety (SS)"
    },
    {
        "term": "MINT vs 3x1",
        "definition": "Trips to the field? FS drifts over the top. SS stays boundary side. You may hear a Push call to balance it out.",
        "image": "A_digital_flashcards-style_interface_tailored_for_.png",
        "role": "Free Safety (FS)"
    }
]

# Filter by role
filtered = [f for f in flashcards if role == "All" or f["role"] == role or f["role"] == "All"]

# Flashcard state
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

if st.session_state.card_index >= len(filtered):
    st.session_state.card_index = 0

current = filtered[st.session_state.card_index]

# Phone-style container
st.markdown("""
    <div style='background-color: #f0f2f6; border-radius: 30px; padding: 30px; max-width: 400px; margin: auto; box-shadow: 0px 0px 15px rgba(0,0,0,0.1);'>
        <h4 style='text-align: center;'>{}</h4>
        <p style='font-size: 18px; line-height: 1.5;'>{}</p>
    </div>
    <br>
""".format(current["term"], current["definition"]), unsafe_allow_html=True)

if current.get("image"):
    st.image(Image.open(current["image"]), caption="Diagram", use_column_width=True)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅️ Previous"):
        st.session_state.card_index = (st.session_state.card_index - 1) % len(filtered)

with col2:
    if st.button("Next ➡️"):
        st.session_state.card_index = (st.session_state.card_index + 1) % len(filtered)

st.caption("Use the selector above to study FS or SS responsibilities. Tap through the flashcards and review diagrams!")


