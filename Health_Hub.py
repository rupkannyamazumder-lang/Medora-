import streamlit as st

st.title("🤖 Health Hub & AI Assistant")

# AI Chatbot Logic
st.subheader("Talk to Medora AI")
mood = st.selectbox("How are you feeling?", ["Sad", "Anxious", "Neutral", "Happy"])

if mood == "Sad":
    st.write("🤖 AI: *I'm so sorry you're feeling this way. You are doing great, and I'm here for you. Would you like a 5-minute distraction?*")
    if st.button("Yes, distract me!"):
        st.balloons()
        st.info("Let's try a breathing exercise: Inhale for 4, Hold for 4, Exhale for 4.")

st.divider()

# Reminders
st.subheader("⏰ Daily Reminders")
st.checkbox("💧 Water (8 glasses)")
st.checkbox("💊 Medicine / Vitamins")
st.checkbox("📅 Doctor Checkup (Upcoming)")
st.checkbox("🧘 Exercise (30 mins)")

# Personal Note
note = st.text_area("Handling Notes / Patient Complications")
if st.button("Save Note"):
    st.write("Note recorded for your next medical visit.")
