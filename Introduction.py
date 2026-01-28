st.title("👤 Patient Introduction")
with st.form("intro_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=12, max_value=60)
    work = st.text_input("Occupation / Where do you work?")
    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (cm)")
    
    submit = st.form_submit_button("Save Profile")
    if submit:
        bmi = weight / ((height/100)**2)
        st.success(f"Welcome, {name}! Profile saved.")
        st.info(f"Your BMI is **{bmi:.1f}**. This helps us customize your health plan.")
