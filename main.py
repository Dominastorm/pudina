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
image = Image.open('assets/images/pudina.png')
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


# DASHBOARD
#Add an app title. Use css to style the title
st.markdown(""" <style> .font {                                          
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Upload your project plan file and generate Gantt chart instantly</p>', unsafe_allow_html=True)

#Add a template screenshot as an example 
st.subheader('Step 1: Download the project plan template')
image = Image.open('assets/images/example.png') #template screenshot provided as an example
st.image(image,  caption='Make sure you use the same column names as in the template')

#Allow users to download the template
@st.cache
def convert_df(df):
     return df.to_csv().encode('utf-8')
df=pd.read_csv('assets/documents/template.csv')
csv = convert_df(df)
st.download_button(
     label="Download Template",
     data=csv,
     file_name='project_template.csv',
     mime='text/csv',
 )


