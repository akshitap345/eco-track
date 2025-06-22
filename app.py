import streamlit as st
from carbon_utils import estimate_carbon
from water_utils import estimate_water_usage

st.set_page_config(page_title="EcoTrack", page_icon="🌱")

st.title("🌱 EcoTrack: Sustainability Dashboard")
st.markdown("Track your **personal carbon footprint** and **water usage** easily!")

st.header("🚗 Carbon Footprint Estimator")
km = st.number_input("Kilometers traveled by vehicle (per day)", min_value=0.0)
kwh = st.number_input("Electricity consumed (kWh per day)", min_value=0.0)
if st.button("Estimate Carbon Footprint"):
    carbon = estimate_carbon(km, kwh)
    st.success(f"Your estimated daily carbon footprint is **{carbon} kg CO₂**")

st.markdown("---")

st.header("🚿 Water Usage Estimator")
showers = st.number_input("Number of showers taken per day", min_value=0)
laundry = st.number_input("Laundry loads per week", min_value=0)
dishes = st.number_input("Dishwasher uses per week", min_value=0)
if st.button("Estimate Water Usage"):
    water = estimate_water_usage(showers, laundry, dishes)
    st.success(f"Your estimated water usage is **{water} liters**")

st.markdown("---")
st.markdown("Made with ❤️ using Python + Streamlit")