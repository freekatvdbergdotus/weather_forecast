import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days.")
option = st.selectbox("Select data to view:",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}.")

# Get the temperature/sky data
try:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        # Create a temperature plot
        temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        images = {"Clear":"clear.png", "Clouds":"cloud.png", "Rain":"rain.png", "Snow":"snow.png"}
        image_paths = [ "images/"+images[s] for s in sky_conditions]
        st.image(image_paths, width=115)
except KeyError:
    st.write("That place does not exist.")