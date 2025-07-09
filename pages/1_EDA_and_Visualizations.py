import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv("college_student_management_data.csv")

df = load_data()

st.set_page_config(page_title="Exploratory Data Analysis 🕵️ And Visualizations 📊",page_icon="👓",layout="wide")

st.header("🔍 Let's Begin by Exploring the Dataset")

st.divider()
st.dataframe(df.head())
st.metric("Dataset Rows", df.shape[0])
st.metric("Dataset Columns", df.shape[1])
null_,info=st.columns([1,1])
with null_:
    st.markdown("## Null Values :")
    st.code(df.isnull().sum())
with info:
    st.markdown("## Data Types :")
    st.code(df.dtypes)
st.divider()

st.header("Visualizations And Some Analysis 📊")
st.subheader("Visuals :")
g1,g2=st.columns([1,1])
g3,g4=st.columns([1,1])
sns.set_theme(style="darkgrid")
with g1:
    fig1=plt.figure()
    sns.countplot(data=df,y="major",hue="gender",palette="pastel")
    st.pyplot(fig1)
with g2:
    fig2=plt.figure()
    sns.kdeplot(data=df,x="age",hue='gender',fill=True,palette="pastel")
    st.pyplot(fig2)
with g3:
    fig3=plt.figure()
    sns.boxplot(data=df,x="major",y="GPA",hue="gender",palette="pastel")
    plt.legend(loc="upper right")
    st.pyplot(fig3)
with g4:
    fig4=plt.figure()
    sns.boxplot(data=df,x="major",y="attendance_rate",hue="gender",palette="pastel")
    plt.legend(loc="upper right")
    st.pyplot(fig4)

st.subheader("Insights From Above 🕵️")
st.info("- Girls and Other Gender students are performing significantly better than Boys in the Business major.")
st.info("- In Engineering, Girls tend to score slightly lower compared to Boys and Other Gender students.")
st.info("- Overall, Boys and Girls outperform Other Gender students across most majors.")
st.info("- In the Arts major, all genders show similar academic performance, indicating balanced outcomes.")
st.info("- Since the dataset represents college students, most of them fall within the age range of 18 to 25.")
st.info("- A higher number of Male students have enrolled in Computer Science and Arts majors.")
st.info("- In Engineering and Business, Female and Other Gender students show similar levels of enrollment.")

st.divider()
st.success("Now We are Done With Data Anlysis And lets Go forward to Model")
