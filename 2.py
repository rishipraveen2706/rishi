import streamlit as st

class Buttons:  # Make sure class name is capitalized
    def __init__(self, button_name):
        if st.button(f"Button number is {button_name}"):
            self.calc(button_name * button_name)  # Use st.write() instead of st.toast()

    def calc(self,num):
        if num%2 ==0:
            st.balloons()
        else:
            st.snow()

for i in range(10):
    Buttons(i)