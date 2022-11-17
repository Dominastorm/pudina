from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import io


def main() -> None:
    
    # Setting wide as the default layout
    st.set_page_config(layout="wide")

    # SIDEBAR
    # Add a logo to the sidebar
    image = Image.open('assets/images/pudina.png')
    st.sidebar.image(image, use_column_width=True)

    # Add expander to provide app information
    expander = st.sidebar.expander("About")
    expander.write("This app is a project management dashboard that allows you to track your projects and tasks.")

    # Add a selectbox to the sidebar:
    menu = ("Create", "Read", "Update", "Delete")
    choice = st.sidebar.selectbox("Menu", menu)

    

if __name__ == '__main__':
    main()