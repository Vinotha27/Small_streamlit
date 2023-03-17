#import Packages
import streamlit as st
import pandas as pd
#Heading
st.header("INDIAN RAILWAYS")
#Caption
st.caption("Safety | Security | Punctuality")
#Background Image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://wallpapercave.com/wp/wp6222650.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://wallpapercave.com/wp/wp6222650.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.image("https://wallpapercave.com/wp/wp6222650.jpg")

st.progress(10)
#read file
import pandas as pd
url = 'https://raw.githubusercontent.com/Vinotha27/Small_streamlit/main/train_schedule.csv'
url1='https://raw.githubusercontent.com/Vinotha27/Small_streamlit/main/train_info.csv'
df = pd.read_csv(url, index_col=0)
df1=pd.read_csv(url1, index_col=0)
df.dropna(inplace=True)
df1.dropna(inplace=True)
#st.dataframe(df, use_container_width=True)
#st.dataframe(df1, use_container_width=True)
merged = pd.merge(df,df1, how="inner", on=["Train_No"])
merged1=merged.dropna()
st.dataframe(merged1, use_container_width=True)


#sidebar message
st.sidebar.header('User Input')
st.sidebar.date_input('Travelling date')

#sidebar rounded trip  option
a=st.sidebar.selectbox('Rounded Trip',['Yes','No'])
if a is 'No':
   st.header('Thank You For Choosing Us🤗')
else:
    st.header("Please Proceed further .....")
    
    
    
st.sidebar.text_input('Email address')
st.spinner('Wait for it...'):   


   




