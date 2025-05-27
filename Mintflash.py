import streamlit as st

st.set_page_config(page_title="Safety Flashcards - MINT Package", layout="centered")

st.title("📱 Safety Flashcards")

# Topic and Role selectors
topic = st.selectbox("Select Install Topic:", ["MINT Package", "Coverage Basics"])
role = st.selectbox("Choose your position:", ["All", "Free Safety (FS)", "Strong Safety (SS)"])

# Define flashcards by topic
topic_flashcards = {
    "MINT Package": [
        {
            "term": "Base MINT Alignment",
            "definition": "In a standard MINT look, safeties are deep—around 10 to 12 yards. FS is to the field, SS to the boundary. Think 2-high shell, disguise-ready.",
            "role": "All"
        },
        {
            "term": "Motion Adjustments in MINT",
            "definition": "If there’s motion, communicate. STAR bumps, SS might spin down, and FS may rotate into Thin or Cloud depending on the call.",
            "role": "All"
        },
        {
            "term": "Coverage Responsibility - FS",
            "definition": "You’re reading #2 to the field. Vertical? Stay on top. Inside break? Be ready to close. Eliminate the deep threat.",
            "role": "Free Safety (FS)"
        },
        {
            "term": "Coverage Responsibility - SS",
            "definition": "You’re the hammer on the boundary. Watch #2 to #1 and rotate into curl/flat or the box—especially in Trap, Robber, or Buzz.",
            "role": "Strong Safety (SS)"
        },
        {
            "term": "MINT Check: Empty",
            "definition": "If the offense shows Empty, check out of MINT. STAR or SS might flex wide to pick up #3. It’s about handling quick threats.",
            "role": "Strong Safety (SS)"
        },
        {
            "term": "MINT vs 3x1",
            "definition": "Trips to the field? FS drifts over the top. SS stays boundary side. You may hear a Push call to balance it out.",
            "role": "Free Safety (FS)"
        }
    ],
    "Coverage Basics": [
        {
            "term": "Cover 1 Basics",
            "definition": "Man coverage underneath with a single high safety (FS) in the post. SS often has TE or helps in the low hole zone.",
            "role": "All"
        },
        {
            "term": "Cover 2 Vision",
            "definition": "Split safeties over deep halves. FS and SS need to break on corner routes and verticals—especially against Smash or Verts.",
            "role": "All"
        },
        {
            "term": "Robber Concept",
            "definition": "SS drops into an intermediate zone. Eyes on the QB to jump crossing routes. High risk, high reward.",
            "role": "Strong Safety (SS)"
        },
        {
            "term": "Cloud Coverage",
            "definition": "Corner drops to the flat. FS shades over #1 or #2 based on route. Be ready to bracket or jump a corner route.",
            "role": "Free Safety (FS)"
        },
        {
            "term": "Route Recognition: Smash",
            "definition": "#1 runs hitch, #2 goes corner. In Cover 2, FS or SS must break quickly on the corner to prevent big gains.",
            "role": "All"
        },
        {
            "term": "Check: Red",
            "definition": "Run fit check. If offense motions to trips or bunch, SS may rotate down to the box to balance numbers.",
            "role": "Strong Safety (SS)"
        }
    ]
}

# Get current topic's cards and filter by role
all_cards = topic_flashcards[topic]
filtered = [f for f in all_cards if role == "All" or f["role"] == role or f["role"] == "All"]

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

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅️ Previous"):
        st.session_state.card_index = (st.session_state.card_index - 1) % len(filtered)

with col2:
    if st.button("Next ➡️"):
        st.session_state.card_index = (st.session_state.card_index + 1) % len(filtered)

st.caption("Choose an install topic and your position to review key flashcards. More topics coming soon!")




