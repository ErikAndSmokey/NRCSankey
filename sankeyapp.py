import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide', initial_sidebar_state = 'collapsed')

with open('Sankey Diagram 10.30.24.html', 'r') as f:
	html_content = f.read()
	components.html(html_content, height = 800, width = 1200)