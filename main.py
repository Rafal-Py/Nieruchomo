# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    st.write(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    x = st.slider("First squared slider")
    st.write(x, 'squared is', x * x)

    # Reuse this data across the runs!
    read_and_cache_csv = st.cache(pd.read_csv)
    BUCKET = f"https://streamlit-self-driving.s3-us-west-2.amazonaws.com/"
    data = read_and_cache_csv(BUCKET + "labels.csv.gz", nrows=1000)
    desired_label = st.selectbox("Filter to:", ["car", "truck"])
    st.write(data[data.label == desired_label])


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data


def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["lon", "lat"],
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ]
    ))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Streamlit')

    # SETTING PAGE CONFIG TO WIDE MODE
    # st.beta_set_page_config(layout="wide")

    # LOADING DATA
    DATE_TIME = "date/time"
    DATA_URL = (
        "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
    )
    data = load_data(100000)
    hour = st.sidebar.slider("Hours", 0, 23)
    data = data[data[DATE_TIME].dt.hour == hour]

    st.write(f'## Geo Data at {hour}h')
    midpoint = (np.average(data["lat"]), np.average(data["lon"]))
    map(data, midpoint[0], midpoint[1], 11)
    # st.map(data)

    if st.checkbox("Show Raw Data"):
        st.write(f'## Raw Data at {hour}h')
        st.write(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
