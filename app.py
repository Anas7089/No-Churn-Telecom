import numpy as np
import pandas as pd
import streamlit as st

st.title('Risk Prediction of Custemer Churn')
st.markdown('This application predict the customer leave or not , and i will give flag that customer Churn flag')


st.header('User Input Parameters')
col1,col2,col3 = st.columns(3)
with col1:
    State =st.number_input('States between [0-50]',min_value=0,max_value=50,value=1)
    Account_Length = st.number_input('Account Leanth between 1-243' ,min_value=1,max_value=243,value=2)
    Day_Calls = st.number_input('Day_Calls 0-165',min_value=0,max_value=165,value=3)
    Eve_Calls =st.number_input('Eve_Calls 0-170',min_value=0,max_value=170,value=50)
    Night_Calls = st.number_input('Night_Calls 12-175',min_value=12,max_value=175,value=15)
    International_calls =st.number_input('International_calls 0-19',min_value=0,max_value=19,value=5)

with col2:
    Area_Code = st.radio('Area_Code',[415,408,510],horizontal=True)
    International_Plan = st.radio('International_Plan ',[0,1],horizontal=True)
    VMail_Plan = st.radio('VMail_Plan',[0,1],horizontal=True)
    CustServ_Calls = st.radio('CustServ_Calls',[1,2,3,4,5,6,7,8,9],horizontal=True)
   

with col3:
    Day_Mins = st.slider('Day_Mins',0.514203,1.000000,0.514203)
    Eve_Mins = st.slider('Eve_Mins',0.000000,1.000000,0.551211)
    Night_Mins =st.slider('Night_Mins ',0.058634,0.964766,0.476232)
    International_Mins =st.slider('International_Mins ',0.000000,1.000000,0.512314)


if st.button('Risk Prediction'):
    df = pd.read_csv('clean_data.csv')
    df = df.drop('Churn',axis=1)  # droping targer

    # import pickle
    import pickle
    model =pickle.load(open('XGmodel.pkl','rb'))

    prediction = model.predict([[State,	Account_Length	,Area_Code,	International_Plan,	
                                 VMail_Plan	,Day_Mins,	Day_Calls,	Eve_Mins,	Eve_Calls,	Night_Mins,
                                Night_Calls,	International_Mins,	International_calls,	CustServ_Calls]])
    if prediction == 0:
        st.markdown('The Churm risk of this person is :green[Low]')
    else:
        st.markdown("The Chrum rik of this person is :red[High]")
