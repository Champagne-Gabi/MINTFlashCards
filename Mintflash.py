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
    "Phase 1: Core Structure & Personnel": [
        {"term": "Today we’re going to talk about the MINT Front.", "definition": "The MINT front is a 3-4 defensive structure using a 4i-0-4i front and a stand-up JACK on the edge. It’s built to handle spread formations while defending the run.", "role": "All"},
        {"term": "What does 4i-0-4i mean?", "definition": "It refers to the alignment of the defensive linemen: both ends line up on the inside shoulder of the offensive tackles (4i), and the nose tackle is head-up on the center (0).", "role": "All"},
        {"term": "Who is the JACK and what’s their job?", "definition": "The JACK is a hybrid edge player—part linebacker, part defensive end. They line up outside the tackle and are responsible for setting the edge or rushing the passer.", "role": "All"},
        {"term": "How does the MINT front help against the run?", "definition": "It lets you keep a light box (only 5 defenders) while still covering interior gaps soundly. This frees up the secondary for pass coverage without giving up run integrity.", "role": "All"},
        {"term": "How many DBs are in MINT?", "definition": "MINT is typically played with nickel personnel—so 5 defensive backs. This includes the STAR, who covers the slot and helps with run fits.", "role": "All"},
        {"term": "Why do we use MINT in this defense?", "definition": "It helps us defend modern spread offenses while sticking to base personnel. It keeps us versatile and able to adapt on the fly.", "role": "All"},
        {"term": "Next: Select Phase 2 to learn about Pre-Snap Reads", "definition": "Up next, we’ll look at how to read the formation and make smart decisions before the ball is snapped.", "role": "All"}
    ],
    "Phase 2: Pre-Snap Reads": [
        {"term": "Now let’s dive into Pre-Snap Reads.", "definition": "Before the snap, it’s crucial to identify offensive formations, personnel groupings, and alignment. This helps anticipate play calls.", "role": "All"},
        {"term": "What’s the first thing I should look for?", "definition": "Start by identifying the strength of the formation—tight end side or wide receiver overload—and communicate it with your teammates.", "role": "All"},
        {"term": "FS: What should I focus on pre-snap?", "definition": "As a Free Safety, your eyes should be on receiver depth, split, and backfield depth. This helps you anticipate deep route concepts.", "role": "Free Safety (FS)"},
        {"term": "SS: What should I focus on pre-snap?", "definition": "As a Strong Safety, check for TE alignment, backfield offset, and wide receiver motions. These often cue run/pass responsibility.", "role": "Strong Safety (SS)"},
        {"term": "How do I call the strength?", "definition": "Use terms like 'Rip' (right) or 'Liz' (left) to alert others. Make sure this is echoed across the defense.", "role": "All"},
        {"term": "What else should I scan for pre-snap?", "definition": "Look at the backfield alignment—pistol, offset, etc.—and the splits of wide receivers. These give clues about run/pass likelihood.", "role": "All"},
        {"term": "What does 'cheat your leverage' mean pre-snap?", "definition": "It means aligning slightly inside or outside your man or zone responsibility based on offensive tendencies and route concepts.", "role": "All"},
        {"term": "Next: Select Phase 3 to learn about Motion Adjustments", "definition": "In the next phase, you’ll learn how to shift your alignment and coverage when the offense uses pre-snap motion.", "role": "All"}
    ],
    "Phase 3: Motion Adjustments": [
        {"term": "Now we’re going to talk about Motion Adjustments.", "definition": "Motion is used by the offense to create mismatches or force communication errors. As a safety, you must react quickly and correctly.", "role": "All"},
        {"term": "What types of motion are common?", "definition": "Watch for jet motion (WR behind QB), return motion (motion out and back), or orbit motion (looping behind QB). Each has a different impact.", "role": "All"},
        {"term": "FS: What’s my role on motion?", "definition": "Stay deep but ready to rotate. If the coverage checks to zone, shift laterally while keeping your eyes in the backfield.", "role": "Free Safety (FS)"},
        {"term": "SS: What’s my role on motion?", "definition": "You may be called to travel with the motion man or bump your alignment. Listen for 'banjo' or 'bump' calls.", "role": "Strong Safety (SS)"},
        {"term": "What does 'bump across' mean?", "definition": "It means defenders shift laterally in response to motion, often passing off coverage responsibilities. Communication is key.", "role": "All"},
        {"term": "How does this affect zone vs. man?", "definition": "In zone, you shift your zone responsibilities. In man, you may travel with the motion or switch men, depending on the call.", "role": "All"},
        {"term": "Next: Select Phase 4 to learn about Coverage Responsibilities", "definition": "Next up, we’ll break down your zone or man coverage rules in the most common installs.", "role": "All"}
    ],
    "Phase 4: Coverage Responsibilities": [
        {"term": "Now let’s talk about Coverage Responsibilities.", "definition": "Safeties play a major role in both man and zone coverages. This phase helps you recognize your assignment across calls.", "role": "All"},
        {"term": "FS: What’s my job in Cover 1?", "definition": "As a Free Safety, you’re usually the deep middle help. Read the QB’s drop and eyes. You’re the last line of defense.", "role": "Free Safety (FS)"},
        {"term": "SS: What’s my job in Cover 1?", "definition": "As a Strong Safety, you’re often in man on a TE or RB. Use physicality early in the route and don’t give up inside leverage.", "role": "Strong Safety (SS)"},
        {"term": "What about Cover 3?", "definition": "You’ll each cover a deep third. FS shades strong side and watches vertical threats. SS may help reroute inside WRs before dropping.", "role": "All"},
        {"term": "FS: What’s my read in quarters?", "definition": "You read #2. If he releases vertically, stay over top. If he breaks out or inside, rob another route coming into your zone.", "role": "Free Safety (FS)"},
        {"term": "SS: How should I play quarters?", "definition": "You may match the TE or slot in man if they go vertical. Keep your eyes in the backfield for run support, too.", "role": "Strong Safety (SS)"},
        {"term": "Tips for transitioning from backpedal", "definition": "Stay square as long as possible, don’t open hips early. Read route stems and anticipate breaks.", "role": "All"},
        {"term": "Next: Select Phase 5 to review Terminology Recap", "definition": "Next up is a summary of the most important calls and concepts to remember from Day 1.", "role": "All"}
    ],
    "Phase 5: Terminology Recap": [
        {"term": "Let’s review some key terminology.", "definition": "You’ve covered a lot today. This phase reviews the most critical terms so you can lock them in.", "role": "All"},
        {"term": "Rip/Liz", "definition": "Used to call formation strength. 'Rip' = strength to the right. 'Liz' = strength to the left.", "role": "All"},
        {"term": "Jack", "definition": "The stand-up edge player in the MINT front. Responsible for contain, sometimes rush, sometimes drop.", "role": "All"},
        {"term": "STAR", "definition": "The nickel DB, usually lines up over the slot. Big role in coverage and run fits.", "role": "All"},
        {"term": "FS: What does leverage mean for me?", "definition": "You must maintain outside leverage on deep routes in zone, and inside leverage when protecting middle-of-field help in man.", "role": "Free Safety (FS)"},
        {"term": "SS: What’s my eyes and leverage responsibility?", "definition": "Eyes in the backfield pre-snap, and leverage depends on help. Typically outside leverage in Cover 3, inside in man.", "role": "Strong Safety (SS)"},
        {"term": "You’ve completed Day 1!", "definition": "Great job. Review these terms anytime, and get ready to build on this tomorrow.", "role": "All"}
    ]
}

# Get filtered cards by role
all_cards = flashcards_by_phase[phase]
filtered = [f for f in all_cards if role == "All" or f["role"] == role or f["role"] == "All"]

if not filtered:
    st.warning("No flashcards available for this role in the selected phase.")
    st.stop()

# Flashcard navigation state
if "last_phase" not in st.session_state:
    st.session_state.last_phase = phase

if phase != st.session_state.last_phase:
    st.session_state.card_index = 0
    st.session_state.last_phase = phase

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

