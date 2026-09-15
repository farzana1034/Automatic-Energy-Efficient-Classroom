import streamlit as st

st.set_page_config(
    page_title="Energy-Efficient Classroom",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Automatic Energy-Efficient Classroom")
st.write("Python + Streamlit Simulation")

st.header("Classroom Conditions")

col1, col2, col3 = st.columns(3)

with col1:
    occupancy = st.selectbox(
        "👥 Occupancy",
        ["Occupied", "Empty"]
    )

with col2:
    light_level = st.selectbox(
        "💡 Light Level",
        ["Bright", "Dark"]
    )

with col3:
    temperature = st.slider(
        "🌡️ Temperature (°C)",
        20,
        40,
        30
    )

# Automatic control logic

if occupancy == "Empty":
    light1 = "OFF"
    light2 = "OFF"
    fan1 = "OFF"
    fan2 = "OFF"

else:
    if light_level == "Dark":
        light1 = "ON"
        light2 = "ON"
    else:
        light1 = "OFF"
        light2 = "OFF"

    if temperature < 28:
        fan1 = "OFF"
        fan2 = "OFF"
    elif temperature <= 32:
        fan1 = "ON"
        fan2 = "OFF"
    else:
        fan1 = "ON"
        fan2 = "ON"

st.header("⚙️ Automatic Control")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💡 Light 1", light1)

with col2:
    st.metric("💡 Light 2", light2)

with col3:
    st.metric("🌀 Fan 1", fan1)

with col4:
    st.metric("🌀 Fan 2", fan2)

st.success("Classroom automation is working successfully!")