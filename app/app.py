import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

st.title("Web App fvj Stats")
st.markdown(
    '''
    # Boas vindas ao meu app fvj Stats.
    Boas análises!
    '''
)

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League', ['ALEMANHA - 2. BUNDESLIGA', 'ALEMANHA - BUNDESLIGA', 'BRASIL - SÉRIE A', 'BRASIL - SÉRIE B', 'BRASIL - SÉRIE C', 'BÉLGICA - LIGA JUPILER', 'ESPANHA - LALIGA', 'ESPANHA - LALIGA2', 'FRANÇA - LIGUE 1', 'INGLATERRA - PREMIER LEAGUE', 'ITÁLIA - SERIE A', 'ITÁLIA - SERIE B', 'JAPÃO - LIGA J1', 'MÉXICO - LIGA MX', 'NORUEGA - ELITESERIEN', 'PORTUGAL - LIGA PORTUGAL', 'PORTUGAL - LIGA PORTUGAL 2', 'SUÉCIA - ALLSVENSKAN', 'TURQUIA - SUPER LIG'])

def load_data(league):
    url = f"https://raw.githubusercontent.com/Franciscovj/jogos_dia_nba/f2c3a5bde9becbf90d4ec14709cc3f613aaeeb1d/app/dados_exportados.csv?raw=true"
    data = pd.read_csv(url)
    data = data[data['League'] == league]
    return data

df = load_data(selected_league)

# Sidebar - Team selection
sorted_unique_team = sorted(df.Home.unique())
selected_team = st.sidebar.multiselect('Teams', sorted_unique_team, sorted_unique_team)

# Filtering data
df_filtered = df[(df.Home.isin(selected_team))]

# Apply style to the DataFrame
def highlight_above_threshold(val, threshold):
    color = 'background-color: yellow' if val > threshold else ''
    return color

styled_df = df_filtered.style \
    .applymap(lambda x: highlight_above_threshold(x, 10), subset=['FT_Odd_H']) \
    .set_properties(**{'background-color': 'black', 'color': 'white'}) \
    .applymap(lambda x: 'background-color: lightgrey', subset=pd.IndexSlice[::2, :]) \
    .format({'coluna_numerica': '{:.2f}', 'coluna_monetaria': 'R${:.2f}'})

# Display the styled DataFrame
st.subheader('Styled DataFrame - ' + selected_league)
st.dataframe(styled_df, width=800)

