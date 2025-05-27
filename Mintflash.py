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

# Define flashcards by learning phase
flashcards_by_phase = {
    "Phase 1: Core Structure & Personnel": [
        {"term": "Let’s go over what 'MINT' means.", "definition": "MINT is a defensive front used primarily against spread formations. You’ll see 4i–0–4i alignments across the line, with a Jack or hybrid edge player outside. It lets us keep two high safeties while still defending the run with numbers.", "role": "All"},
        {"term": "What type of defense is MINT typically run out of?", "definition": "MINT is most commonly used in a 3-4 defensive structure, often paired with nickel personnel (that’s five defensive backs). It gives us the flexibility to cover modern spread offenses without sacrificing physicality in the box.", "role": "All"},
        {"term": "What’s the role of the STAR?", "definition": "The STAR is your nickel back—part linebacker, part corner. He handles slot receivers and adjusts with motion. Big communicator in MINT calls.", "role": "All"}
    ],
    "Phase 2: Pre-Snap Reads": [
        {"term": "Now let’s focus on what FS is reading.", "definition": "Your eyes are on #2 to the field. If he goes vertical, you stay on top. If he breaks in, close and take away the window. You’re the last line, but you can also be the playmaker.", "role": "Free Safety (FS)"},
        {"term": "Strong Safety, this one’s for you.", "definition": "You’re the boundary enforcer. Track #2 to #1. Your job? Own the curl/flat or insert down into the box. Trap, Robber, Buzz—know your fit and bring the hammer.", "role": "Strong Safety (SS)"},
        {"term": "How do we handle a 3x1 set? Let’s walk through it.", "definition": "Trips to the field? FS cheats that way over the top, SS stays strong on the backside. You may hear a 'Push' or 'Roll' to balance the coverage. Keep your eyes active and communicate.", "role": "Free Safety (FS)"}
    ],
    "Phase 3: Motion Adjustments": [
        {"term": "Let’s go over what to do when the offense motions.", "definition": "Motion is a communication test. When #2 or #3 shifts, STAR bumps, SS may spin down, and FS might rotate into Cloud or Thin coverage. The key: talk it out and adjust as a unit.", "role": "All"},
        {"term": "Let’s talk about what happens if they go Empty.", "definition": "Empty formation means quick threats. In MINT, you may check out entirely. SS might flex wide to pick up #3. The goal: cover space fast and deny the first read.", "role": "Strong Safety (SS)"}
    ],
    "Phase 4: Coverage Responsibilities": [
        {"term": "Now we're going to cover Cover 1.", "definition": "This is man across the board with FS in the post. SS might be in man against the tight end or helping as a low-hole player. Play it tight, and trust your leverage.", "role": "All"},
        {"term": "Next up: Cover 2 and your deep halves.", "definition": "You and your counterpart are splitting the deep field. Be ready to break on corners and posts. Recognize Smash and Verts—those are your money reads.", "role": "All"},
        {"term": "Let’s talk about Robber coverage for SS.", "definition": "In Robber, you’re dropping into the short middle, tracking crossing routes and looking to jump passes. It’s aggressive—commit when you’re sure.", "role": "Strong Safety (SS)"},
        {"term": "FS, let’s go over Cloud Coverage.", "definition": "With Cloud, the corner plays flat. You’re over the top of #1 or bracketing with the STAR or backer. Don’t let anything leak.", "role": "Free Safety (FS)"}
    ],
    "Phase 5: Terminology Recap": [
        {"term": "Know this: 'Spin', 'Roll', and 'Cloud' calls.", "definition": "'Spin' often means safety rotation. 'Roll' is a coverage shift to a side. 'Cloud' involves the corner playing underneath zone while safety helps over top.", "role": "All"},
        {"term": "Let’s talk about route identifiers.", "definition": "#1 = the outside WR, #2 = the slot, #3 = the inside (usually RB or TE). You’ll hear a lot about reading #2’s release—vertical, in, or out.", "role": "All"},
        {"term": "Key check: what does 'Push' mean?", "definition": "Push is a call to shift defenders toward trips formations. It balances out responsibilities to keep coverage intact versus overloaded sides.", "role": "All"},
        {"term": "SS, this one’s a check you’ll need in your pocket.", "definition": "‘Check Red’ means fit the run when they motion to trips or tight bunch sets. Drop down, help the box, and close space quickly.", "role": "Strong Safety (SS)"},
        {"term": "Great job! You’ve completed Day 1’s flashcards.", "definition": "Feel free to review any phase again, or check back soon for Day 2 installation content!", "role": "All"}
    ]
}

# Get current phase's cards and filter by role
all_cards = flashcards_by_phase[phase]
filtered = [f for f in all_cards if role == "All" or f["role"] == role or f["role"] == "All"]

# Flashcard state
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

if st.session_state.card_index >= len(filtered):
    st.session_state.card_index = len(filtered) - 1

current = filtered[st.session_state.card_index]

# Phone-style container
st.markdown(f"""
    <div style='background-color: #f0f2f6; border-radius: 30px; padding: 30px; max-width: 400px; margin: auto; box-shadow: 0px 0px 15px rgba(0,0,0,0.1);'>
        <h4 style='text-align: center;'>{current['term']}</h4>
        <p style='font-size: 18px; line-height: 1.5;'>{current['definition']}</p>
    </div>
    <br>
""", unsafe_allow_html=True)

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

