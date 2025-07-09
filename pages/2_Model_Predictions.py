import streamlit as st
import pandas as pd
import numpy as np
import joblib 

@st.cache_resource
def load_model():
    return joblib.load("Model/FirstPipeline.pkl")

model=load_model()

st.header("📋 Enter Student Details for Risk Prediction")
with st.form("student_form"):
    age=st.slider(label="Age Of Student",min_value=17,max_value=30,value=20,step=1,format="%d")
    GPA=st.slider("GPA Scored ",min_value=0.00,max_value=4.00,format="%f",step=0.01,value=2.4)
    Course_Load=st.slider("Course Load On Students",min_value=3,max_value=6,step=1,value=3,format="%d")
    Avg_course_grade=st.number_input("Average Course Grade Scored In Previous Sessions",min_value=0.00,max_value=100.00,step=0.01,value=65.0)
    Attendance_rate=st.number_input("Attendance Rate of Students",min_value=0.4,max_value=1.0,step=0.01,value=0.75)
    Logins_last_month= st.slider("No. Of Times Student Visited The Website Last Month",min_value=0,max_value=50,step=1,value=10)
    Session_duration=st.slider("Average Duration in Minutes On Websites",min_value=0,max_value=100,value=35,step=1)
    Ass_Sub=st.number_input("Assignment Rate Of Student",min_value=0.00,max_value=1.00,value=0.70,step=0.01)
    Part_Count = st.slider("No. of Participations By Student",min_value=0,max_value=25,step=1,value=0)
    Video_comp = st.number_input("Completion Rate Of Introductory Videos",min_value=0.0,max_value=1.00,value=0.75,step=0.01)
    Gender= st.selectbox("Gender :",["Male","Female","Other"])
    Major= st.radio("Major :",['Computer Science' ,'Arts', 'Engineering', 'Business'])
    Enrollment= st.radio("Enrollment Status : ",['Graduated','Leave','Active'])
    
    submit = st.form_submit_button("Predict Risk Level")

if submit:
    if Logins_last_month==0:
        Session_duration=0
    data={'age':age, 'gender':Gender, 'major':Major, 'GPA':GPA, 'course_load':Course_Load, 'avg_course_grade':Avg_course_grade,
        'attendance_rate':Attendance_rate, 'enrollment_status':Enrollment, 'lms_logins_past_month':Logins_last_month,
        'avg_session_duration_minutes':Session_duration, 'assignment_submission_rate':Ass_Sub,
        'forum_participation_count':Part_Count, 'video_completion_rate':Video_comp}
    
    input_df = pd.DataFrame([data])

    pred=model.predict(input_df)[0]
    result="Unknown"
    if pred==0:
        result="Low"
    if pred==1:
        result="Medium"
    if pred==2:
        result="High"

    st.markdown(f'Therefore , There is {result} risk in Student\'s Studies')

    if pred==0:
        st.success("✅ The Student is doing well and does not require any consultation.")
    if pred==1:
        st.warning("⚠️ Student is facing some problems and should be monitored.")
    if pred==2:
        st.error("❗ The student is at high risk and needs immediate support.")
else:
    st.info("Please Submit Required Information For prediction ")
