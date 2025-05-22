import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuaracy_score

st.set_page_config(page_title"predictions")
st.title("predictions")
st.header("predictions")
