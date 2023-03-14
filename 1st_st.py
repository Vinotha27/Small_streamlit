#import Packages
import streamlit as st
import pandas as pd

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
df.dropna(inplace=True)
st.dataframe(df, use_container_width=True)

# --- STREAMLIT SELECTION
department = df['Station_name'].unique().tolist()
ages = df['Departure_time'].unique().tolist()

age_selection = st.slider('Station_name:',
                        min_value= min(ages),
                        max_value= max(ages),
                        value=(min(ages),max(ages)))

department_selection = st.multiselect('Departure_time:',
                                    department,
                                    default=department)









