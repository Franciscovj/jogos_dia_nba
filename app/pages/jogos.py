
import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

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

# Cria controles deslizantes para definir os valores mínimo e máximo
valor_min_home = st.slider('valor_min_home', float(df_jogos['FT_Odd_H'].min()), float(df_jogos['FT_Odd_H'].max()), value=valor_minimo)
valor_max_home = st.slider('valor_max_home', float(df_jogos['FT_Odd_H'].min()), float(df_jogos['FT_Odd_H'].max()), value=valor_maximo)



# Filtra o DataFrame com base nos valores mínimos e máximos selecionados nos controles deslizantes
df_filtrado = df_jogos.query("@valor_min_home<= FT_Odd_H <= @valor_max_home")

st.subheader("Dataframe: Jogos do Dia")
st.dataframe(df_jogos)
st.subheader("Dataframe Filtrado")
st.dataframe(df_filtrado)

