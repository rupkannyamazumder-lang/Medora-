st.title("📅 PCOS Period Tracker")
start_date = st.date_input("Start Date of last period")
end_date = st.date_input("End Date of last period")
flow = st.select_slider("Flow Intensity", options=["Spotting", "Light", "Medium", "Heavy", "Black Flow"])

if st.button("Predict Next Period"):
    # PCOS cycles are often longer (average 35 days for prediction)
    next_period = start_date + timedelta(days=35)
    st.write(f"### Predicted Date: {next_period.strftime('%B %d, %Y')}")
    st.caption("Note: Since PCOS cycles vary, this is an estimate.")
