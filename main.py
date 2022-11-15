# Project management application

from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import io

# SIDEBAR

# Setting wide as the default layout
st.set_page_config(layout="wide")

# Add a logo to the sidebar
image = Image.open('assets/images/Pudina.png')
# Small logo for sidebar
st.sidebar.image(image, use_column_width=True)

# Add expander to provide app information
expander = st.sidebar.expander("About")
expander.write("This app is a project management dashboard that allows you to track your projects and tasks.")

# Add a selectbox to the sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you like to view the data?",
    ("Dashboard", "Data")
)

