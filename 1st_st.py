#import Packages
import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

#page Title
st.set_page_config(page_title='Indian Railways.com')

#Heading
st.header("INDIAN RAILWAYS")

#Caption
st.caption("Safety | Security | Punctuality")

#Image
st.image("https://www.wallpapertip.com/wmimgs/155-1554570_indian-train-images-hd.jpg.jpg")

#Baloon Display
st.balloons()


#read file
import pandas as pd
url = 'https://raw.githubusercontent.com/Vinotha27/Small_streamlit/main/train_schedule.csv'
df = pd.read_csv(url, index_col=0)
st.dataframe(df, use_container_width=True)


#side button
st.sidebar()






