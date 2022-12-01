from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import io
import yaml
import streamlit_authenticator as stauth

from yaml.loader import SafeLoader
from helpers.query_execution import excecute_query

from sql.create import create_tables

def main() -> None:
    # Setting wide as the default layout
    st.set_page_config(layout="wide")

    # Load the configuration file
    with open('src/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Create the authenticator
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    # SIDEBAR 
    # Add a logo to the sidebar
    image = Image.open('assets/images/pudina.png')
    st.sidebar.image(image, use_column_width=True)

    # Add expander to provide app information
    expander = st.sidebar.expander("About")
    expander.write("This app is a project management dashboard that allows you to track your projects and tasks.")

    # Authenticate the user
    name, authentication_status, username = authenticator.login('Login', 'main')

    # If the user is authenticated, display the app
    if authentication_status:
        # SIDEBAR
        menu = ['Home', 'Execute Query', 'Logout']
        
        choice = st.sidebar.selectbox('Navigation Menu', menu, label_visibility = 'hidden')
        
        # MAIN
        if choice == 'Home':
            st.title(f'Welcome, {name}!')
            st.write('This is the home page of the app')
        elif choice == "Execute Query":
            st.title('Execute Query')
            excecute_query()
        elif choice == "My Profile":
            st.title('My Profile')
            st.write('This is the my profile page of the app')
        if choice == "Logout":
            st.title('Logout')
            st.write('Are you sure you want to log out?')
            authenticator.logout('Logout', 'main')
        
        # create the tables, in case they don't exist
        create_tables()

    # Incorrect username or password
    elif authentication_status == False:
        st.error('Username/password is incorrect')

    # No input provided
    elif authentication_status == None:
        st.warning('Please enter your username and password')


if __name__ == '__main__':
    main()
