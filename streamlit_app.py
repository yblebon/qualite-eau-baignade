import streamlit as st
import pandas as pd
import numpy as np
import math
import random
from leu import data as leu_data
from gilles import data as gilles_data
from gilles_2 import data as gilles_data_2
from PIL import Image



st.sidebar.title("""
PRELEVEMENT QUALITE DES EAUX DE BAIGNADE 
""")

plages = {
    'SAINT LEU: Plage citerne quarante-six': {
        'id': 1,
        'img': 'IMG_2367.jpeg',
        'data': leu_data,
        'warning': """
           - <15 and <16 are considered as 0,
           - notice double 23 index
           - last coli value is not visible
        """
    },
    
    'SAINT GILLES: Plage ermitage village': {
         'id': 2,
         'warning': None,
        'img': 'IMG_0445.jpeg',
        'data': gilles_data
    },
    'SAINT GILLES: Plage des roches noires': {
         'id': 3,
         'warning': """
           - 04/01/23 prelevement index 13
           - 17/01/23 prelevement index 12
         """,
        'img': 'IMG_2479.jpeg',
        'data': gilles_data_2
    },
    'SAINT LEU: Plage du centre ville': {
        'id': 4,
        'warning': """
           - notice double 24 index
        """,
        'img': 'IMG_2522.jpeg',
        'data': 'https://yblebon-public.s3.eu-north-1.amazonaws.com/qualite-eau-baignade/stleu-centre.csv'
    }
}

option = st.sidebar.selectbox(
    'Sélectionner une plage:',
    plages.keys()
)

plage_data = plages[option]

st.header("""
Source de donnees
""")

if plage_data["warning"]:
   st.warning(plage_data["warning"], icon="🚨")


if plage_data['img']:
   image = Image.open(plage_data['img'])
   st.image(image, caption='Source')


if plage_data['data'] !=  None:
  data = plage_data['data']

  if isinstance(data, str) and data.startswith("https://"):
    df = pd.read_csv(data, sep=";", usecols=['date', 'escherichia coli'])
  else:
    df = pd.DataFrame.from_dict(data)
      
  df['date'] = pd.to_datetime(df['date'], format="%d/%m/%y")
  df = df.sort_values(by="date")
  df['days diff'] = df['date'].diff().dt.days

  st.dataframe(df, use_container_width=True)


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


