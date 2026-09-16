import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Smart Energy-Efficient Classroom",
    page_icon="🏫",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
}

.sensor-box {
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.markdown(
    '<div class="main-title">🏫 Automatic Energy-Efficient Classroom</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Python + Streamlit + Sensor-Based Energy Management System</div>',
    unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("⚙️ Classroom Controls")

st.sidebar.subheader("Sensor Inputs")

occupancy = st.sidebar.selectbox(
    "👤 PIR Sensor - Student Presence",
    ["Students Present", "No Students"]
)

light_level = st.sidebar.slider(
    "🌞 LDR Sensor - Light Level (%)",
    min_value=0,
    max_value=100,
    value=40
)

temperature = st.sidebar.slider(
    "🌡️ Temperature (°C)",
    min_value=15,
    max_value=45,
    value=28
)

st.sidebar.divider()

st.sidebar.subheader("Energy Settings")

electricity_rate = st.sidebar.number_input(
    "Electricity Cost (₹/kWh)",
    min_value=1.0,
    max_value=20.0,
    value=8.0,
    step=0.5
)

# ---------------------------------------------------
# SENSOR LOGIC
# ---------------------------------------------------

students_present = occupancy == "Students Present"

# LIGHT CONTROL
# If students are present and light level is low,
# lights will automatically turn ON.

if students_present and light_level < 60:
    lights_status = "ON"
    light_power = 120
else:
    lights_status = "OFF"
    light_power = 0

# FAN CONTROL
# Fan operates when students are present and
# temperature is greater than 27°C.

if students_present and temperature >= 27:
    fan_status = "ON"
    fan_power = 80
else:
    fan_status = "OFF"
    fan_power = 0

# AC control simulation
if students_present and temperature >= 32:
    ac_status = "ON"
    ac_power = 1200
else:
    ac_status = "OFF"
    ac_power = 0

# ---------------------------------------------------
# ENERGY CALCULATION
# ---------------------------------------------------

total_power = light_power + fan_power + ac_power

# Assume classroom operates for 8 hours/day

daily_energy = total_power / 1000 * 8

daily_cost = daily_energy * electricity_rate

monthly_energy = daily_energy * 30

monthly_cost = daily_cost * 30

# Conventional classroom assumed consumption

conventional_power = 1600

conventional_daily_energy = conventional_power / 1000 * 8

conventional_monthly_energy = conventional_daily_energy * 30

energy_saved = conventional_monthly_energy - monthly_energy

if conventional_monthly_energy > 0:
    saving_percentage = (
        energy_saved / conventional_monthly_energy
    ) * 100
else:
    saving_percentage = 0

# ---------------------------------------------------
# CLASSROOM STATUS
# ---------------------------------------------------

st.subheader("🏫 Classroom Status")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👤 Occupancy",
        occupancy
    )

with col2:
    st.metric(
        "🌞 Light Level",
        f"{light_level}%"
    )

with col3:
    st.metric(
        "🌡️ Temperature",
        f"{temperature} °C"
    )

with col4:
    st.metric(
        "⚡ Total Power",
        f"{total_power} W"
    )

# ---------------------------------------------------
# DEVICE STATUS
# ---------------------------------------------------

st.divider()

st.subheader("💡 Automatic Device Control")

device_col1, device_col2, device_col3 = st.columns(3)

with device_col1:

    if lights_status == "ON":
        st.success("💡 LIGHTS: ON")
    else:
        st.info("💡 LIGHTS: OFF")

    st.write(f"Power Consumption: **{light_power} W**")

with device_col2:

    if fan_status == "ON":
        st.success("🌀 FAN: ON")
    else:
        st.info("🌀 FAN: OFF")

    st.write(f"Power Consumption: **{fan_power} W**")

with device_col3:

    if ac_status == "ON":
        st.success("❄️ AC: ON")
    else:
        st.info("❄️ AC: OFF")

    st.write(f"Power Consumption: **{ac_power} W**")

# ---------------------------------------------------
# ENERGY DASHBOARD
# ---------------------------------------------------

st.divider()

st.subheader("📊 Energy Consumption Dashboard")

energy_col1, energy_col2, energy_col3, energy_col4 = st.columns(4)

with energy_col1:
    st.metric(
        "Daily Energy",
        f"{daily_energy:.2f} kWh"
    )

with energy_col2:
    st.metric(
        "Monthly Energy",
        f"{monthly_energy:.2f} kWh"
    )

with energy_col3:
    st.metric(
        "Monthly Cost",
        f"₹{monthly_cost:.2f}"
    )

with energy_col4:
    st.metric(
        "Estimated Saving",
        f"{saving_percentage:.1f}%"
    )

# ---------------------------------------------------
# DEVICE ENERGY TABLE
# ---------------------------------------------------

st.divider()

st.subheader("📋 Device Energy Details")

device_data = {
    "Device": [
        "LED Lights",
        "Ceiling Fan",
        "Air Conditioner"
    ],
    "Status": [
        lights_status,
        fan_status,
        ac_status
    ],
    "Power (W)": [
        light_power,
        fan_power,
        ac_power
    ]
}

df = pd.DataFrame(device_data)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# ---------------------------------------------------
# ENERGY CHART
# ---------------------------------------------------

st.subheader("📈 Power Consumption")

chart_data = pd.DataFrame(
    {
        "Device": [
            "Lights",
            "Fan",
            "AC"
        ],
        "Power (W)": [
            light_power,
            fan_power,
            ac_power
        ]
    }
)

st.bar_chart(
    chart_data.set_index("Device")
)

# ---------------------------------------------------
# SAVING INFORMATION
# ---------------------------------------------------

st.divider()

st.subheader("🌱 Energy Saving Recommendation")

if not students_present:

    st.success(
        "No students detected. Lights, fan and AC are automatically switched OFF."
    )

elif light_level >= 60:

    st.success(
        "Sufficient natural light detected. Artificial lights are switched OFF."
    )

elif temperature < 27:

    st.success(
        "Temperature is comfortable. Fan and AC remain OFF unless required."
    )

else:

    st.info(
        "Classroom is occupied. Devices are controlled automatically based on sensor conditions."
    )

# ---------------------------------------------------
# PROJECT INFORMATION
# ---------------------------------------------------

st.divider()

with st.expander("ℹ️ About This Project"):

    st.write("""
    This project demonstrates an automatic energy-efficient classroom
    using sensor-based control.

    The system uses:

    • PIR sensor for occupancy detection
    • LDR sensor for light intensity detection
    • Temperature sensor for thermal monitoring
    • Automatic lighting control
    • Automatic fan control
    • Energy consumption calculation
    • Electricity cost estimation

    The Streamlit application provides a simple digital simulation
    of the classroom energy management system.
    """)

st.caption(
    "Developed using Python and Streamlit | Electrical Engineering Project"
)