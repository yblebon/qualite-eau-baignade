import streamlit as st
import pandas as pd
import numpy as np
import math
import random
from PIL import Image



st.title("""
QUALITE DES EAUX DE BAIGNADE
""")

plages = {
    'SAINT LEU: Plage citerne quarante-six 2023 prelevement': {
        'id': 1,
        'img': 'IMG_2367.jpeg',
        
    },
    
    'SAINT GILLES: Plage ermitage 2022 prelevement': 2
}

option = st.selectbox(
    'Sélectionner une plage:',
    plages.keys()
)

plage_id = plages[option]

st.header("""
Source de donnees
""")

st.warning("""
- <15 and <16 are considered as 0,
- notice double 23 index
- last coli value is not visible 
""", icon="🚨")

if plage_id == 2:
    image_name = 'IMG_0446.jpeg'
elif plage_id == 1:
    image_name = 'IMG_2367.jpeg'

image = Image.open(image_name)
st.image(image, caption='Source')

          

df = pd.DataFrame.from_dict(data)
df['date'] = pd.to_datetime(df['date'], format="%d/%m/%y")

df['days diff'] = df['date'].diff().dt.days

st.dataframe(df)


st.header("""
Valeur prelevee de Escherichia coli, <15 et <16 etant considere comme zero
""")
st.line_chart(
    df,
    x = 'date',
    y = 'escherichia coli'
)

st.header("""
Delai entre prelevements en Jours
""")
st.line_chart(
    df,
    x = 'date',
    y = 'days diff'
)


