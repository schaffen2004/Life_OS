import streamlit as st
import pandas as pd

def run():
    st.title('My App')
    df = pd.read_csv('data\habit.csv')
    st.write(df)

if __name__ == '__main__':
    run()