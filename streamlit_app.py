import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.warning("""
- <15 and <16 are considered as 0,
- notice double 23 index
- last coli value is not visible 
""", icon="🚨")
          
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





df['diff'] = df['date'].diff().dt.days

st.dataframe(df)



