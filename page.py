import streamlit as st
import subprocess
import os

def execute_program(program_name):
    current_dir = os.getcwd()
    program_path = os.path.join(current_dir, program_name)
    result = subprocess.run(['python', program_path], capture_output=True, text=True)
    return result.stdout

st.title("Keylogger")

if st.button("Run Logger"):
    output = execute_program("1_klog.py")
    st.text_area("Output", value=output, height=200)

if st.button("Show Log"):
    output = execute_program("2_klogoutput.py")
    st.text_area("Output", value=output, height=200)

if st.button("Clear Log"):
    output = execute_program("3_klogclear.py")
    st.text_area("Output", value=output, height=200)