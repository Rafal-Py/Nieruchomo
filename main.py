# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Streamlit')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
