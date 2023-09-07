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
    'SAINT LEU: Plage citerne quarante-six 2023 prelevement': 1,
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

          
data = {
 'date': [
  "03/01/23", 
  "10/01/23",
  "17/01/23",
  "24/01/23",
  "31/01/23",
  "07/02/23", 
  "14/02/23",
  "21/02/23",
  "28/02/23",
  "07/03/23",
  "14/03/23", 
  "21/03/23", 
  "28/03/23", 
  "04/04/23", 
  "13/04/23", 
  "18/04/23", 
  "25/04/23", 
  "02/05/23", 
  "09/05/23", 
  "23/05/23",
  "06/06/23", 
  "04/07/23", 
  "18/07/23", 
  "25/07/23", 
  "01/08/23", 
  "08/08/23"
 ],
 'escherichia coli':
 [
  0,
  0,
  94,
  0,
  0,
  0,
  0,
  15,
  0,
  0,
  0,
  0,
  46,
  15,
  0,
  61,
  0,
  0,
  0,
  0,
  0,
  15,
  0,
  0,
  0,
  0
 ]
}

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


