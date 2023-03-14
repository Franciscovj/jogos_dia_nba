
import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date
st.markdown(
    """
    <style>
    body {
        background-color: #F0F0F0;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("Web App fvj Stats")

st.sidebar.header('Jogos do Dia')

dia = st.date_input(
    "Data de Análise",
    date.today())

def load_data_jogos():
    data_jogos = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/"+str(dia)+"_Jogos_do_Dia_FlashScore.csv?raw=true")
    data_jogos = data_jogos[["League","Date","Home","Away","FT_Odd_H","FT_Odd_D","FT_Odd_A","FT_Odd_Over25","FT_Odd_Under25","FT_Odd_Under35",
      "FT_Odd_BTTS_Yes","FT_Odd_BTTS_No"]]
    
    return data_jogos

df_jogos = load_data_jogos()
# Define o valor mínimo e máximo iniciais com base na coluna "FT_Odd_H" do DataFrame
valor_min_home = float(df_jogos['FT_Odd_H'].min())
valor_max_home = float(df_jogos['FT_Odd_H'].max())
valor_min_draw = float(df_jogos['FT_Odd_D'].min())
valor_max_draw = float(df_jogos['FT_Odd_D'].max())
valor_min_away = float(df_jogos['FT_Odd_A'].min())
valor_max_away = float(df_jogos['FT_Odd_A'].max())
valor_min_over = float(df_jogos['FT_Odd_Over25'].min())
valor_max_over = float(df_jogos['FT_Odd_Over25'].max())

# Cria controles deslizantes para definir os valores mínimo e máximo
#valor_min_home = st.slider('valor_min_home', float(df_jogos['FT_Odd_H'].min()), float(df_jogos['FT_Odd_H'].max()), value=valor_min_home)
#valor_max_home = st.slider('valor_max_home', float(df_jogos['FT_Odd_H'].min()), float(df_jogos['FT_Odd_H'].max()), value=valor_max_home)
#valor_min_draw = st.slider('valor_min_draw', float(df_jogos['FT_Odd_D'].min()), float(df_jogos['FT_Odd_H'].max()), value=valor_min_draw)
#valor_max_draw = st.slider('valor_max_draw', float(df_jogos['FT_Odd_D'].min()), float(df_jogos['FT_Odd_H'].max()), value=valor_max_draw)
#valor_min_away = st.slider('valor_min_away', float(df_jogos['FT_Odd_A'].min()), float(df_jogos['FT_Odd_H'].max()), value=valor_min_away)
#valor_max_away = st.slider('valor_max_away', float(df_jogos['FT_Odd_A'].min()), float(df_jogos['FT_Odd_H'].max()), value=valor_max_away)
valor_min_home, valor_max_home = st.slider('Casa', float(df_jogos['FT_Odd_H'].min()), float(df_jogos['FT_Odd_H'].max()), (valor_min_home, valor_max_home), step=0.01)
valor_min_draw, valor_max_draw = st.slider('Empate', float(df_jogos['FT_Odd_D'].min()), float(df_jogos['FT_Odd_D'].max()), (valor_min_draw, valor_max_draw), step=0.01)
valor_min_away, valor_max_away = st.slider('Fora', float(df_jogos['FT_Odd_A'].min()), float(df_jogos['FT_Odd_A'].max()), (valor_min_away, valor_max_away), step=0.01)
valor_min_over, valor_max_over = st.slider('Over 2,5', float(df_jogos['FT_Odd_Over25'].min()), float(df_jogos['FT_Odd_Over25'].max()), (valor_min_over, valor_max_over), step=0.01)

# Filtra o DataFrame com base nos valores mínimos e máximos selecionados nos controles deslizantes
#df_filtrado = df_jogos.query("@valor_min_home<= FT_Odd_H <= @valor_max_home")
df_filtrado = df_jogos.query("@valor_min_home<= FT_Odd_H <= @valor_max_home and @valor_min_draw<= FT_Odd_D <= @valor_max_draw and @valor_min_away<= FT_Odd_A <= @valor_max_away and  @valor_min_over<= FT_Odd_Over25<= @valor_max_over")
st.subheader("Dataframe: Jogos do Dia")
st.dataframe(df_jogos)
st.subheader("Dataframe Filtrado")
st.dataframe(df_filtrado)

