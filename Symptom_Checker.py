st.title("🔍 Symptom & Risk Chart")
symptoms = [
    "Irregular periods", "Acne", "Thinning hair", 
    "Weight gain", "Excess body hair", "Darkened skin patches",
    "Pelvic pain", "Headaches", "Mood swings", "Fatigue"
]

selected = []
for sym in symptoms:
    if st.checkbox(sym):
        selected.append(sym)

count = len(selected)
if st.button("Calculate Risk"):
    if count <= 3:
        st.success("Risk Level: LOW")
        st.write("🧘 **Yoga:** Butterfly Pose. 🥗 **Diet:** High Fiber.")
    elif 4 <= count <= 5:
        st.warning("Risk Level: MEDIUM")
        st.write("🧘 **Yoga:** Cobra Pose. 🥗 **Diet:** Low Sugar.")
    else:
        st.error("Risk Level: HIGH")
        st.write("🧘 **Yoga:** Child's Pose. 🥗 **Diet:** Anti-inflammatory foods.")
