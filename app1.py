import importlib.util
import streamlit as st
import os

# Directory containing the page files
pages_dir = "./web_app"

# List all Python files in the pages directory
pages = {f.replace('.py', ''): os.path.join(pages_dir, f) for f in os.listdir(pages_dir) if f.endswith('.py')}

# Top navigation bar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page
page_path = pages[page]
spec = importlib.util.spec_from_file_location(page, page_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
