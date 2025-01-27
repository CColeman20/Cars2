
import streamlit as st

import pandas as pd 

df = pd.read_csv("vehicles_us.csv")
df = pd.read_csv("vehicles_us.csv")
df['is_4wd'] = df['is_4wd'].fillna(0)
df['paint_color'] = df['paint_color'].fillna('Unknown')


