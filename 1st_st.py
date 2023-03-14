#import Packages
import streamlit as st
import pandas as pd

#Heading
st.header("INDIAN RAILWAYS")

#Caption
st.caption("Safety | Security | Punctuality")

#Background Image
page_bg_img = '''
<style>
body {
background-image: url("https://www.wallpapertip.com/wmimgs/155-1554570_indian-train-images-hd.jpg")
}
</style>
'''
st.image(page_bg_img, unsafe_allow_html=True)
    

#Baloon Display
st.balloons()


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
st.dataframe(merged, use_container_width=True)

st.sidebar.header('User Input Features')










