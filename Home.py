

import streamlit as st


# Page Configuration
st.set_page_config(page_title="Student Risk Predictor", page_icon="🎓", layout="centered")

# Welcome Section
st.markdown("<h1 style='text-align: center;'>👋 Welcome to the Student Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("### Empowering educators to identify and support at-risk students early.")

# Short Summary
st.markdown("""
This interactive app uses machine learning to analyze college student data and **predict each student’s risk level** based on academic performance, attendance, and demographic details.

Educational institutions can use this tool to:
- 🧠 Identify students who may be struggling
- 🛠️ Intervene early with support
- 📈 Improve overall student outcomes
""")

st.markdown("---")

# Introduction
st.markdown("## 📘 Introduction")
st.markdown("""
The dataset used in this project contains detailed records of college students, including:

- 🎓 Academic info like **course**, **department**, **marks**, **attendance**
- 🧾 Personal attributes like **gender**, **age**
- 🕒 Enrollment data like **year**, **admission date**, etc.

By analyzing these features, we aim to uncover patterns that correlate with academic risk.
""")

# Objective
st.markdown("## 🎯 Objective")
st.markdown("""
The target variable is **`risk_level`**, which classifies students based on their academic and behavioral risk profile.

We follow a complete ML pipeline:
- 🔧 Data cleaning & preprocessing  
- 📊 Exploratory Data Analysis (EDA)  
- 🧱 Feature engineering  
- 🤖 Model training and evaluation  
- ✅ Predicting the final `risk_level`

This predictive tool supports educational institutions in **making data-driven decisions** to enhance student support systems.
""")

# Footer Note
st.markdown("---")
st.success("Use the sidebar to explore the data, visualize trends, or predict risk levels!")
st.markdown("### 📊 Check Data Analysis in the sidebar ➡️ [EDA and Visualizations](./EDA_and_Visualizations)")
st.markdown("### 🤖 Try the Prediction Tool in ➡️ [Model Predictions](./Model_Predictions)")