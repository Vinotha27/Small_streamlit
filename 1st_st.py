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
background-image: url("https://www.bing.com/images/search?view=detailV2&ccid=dsNh1%2bqc&id=6D1A6F8656D62782B7192FB614D12D45B8447620&thid=OIP.dsNh1-qc5xGy5fWzvIAV7QHaFj&mediaurl=https%3a%2f%2fwallpapercave.com%2fwp%2fwp5521998.jpg&exph=768&expw=1024&q=Indian+Railway&simid=608048304503276004&FORM=IRPRST&ck=6D8B1FBFDAFA84466F857157965CA60F&selectedIndex=8");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
    

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










