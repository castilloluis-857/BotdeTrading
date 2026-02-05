import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from analizador import AnalizadorTecnico
import time

# Configuración visual de "Proyecto de Excelencia"
st.set_page_config(page_title="Sistema de Trading Algorítmico Pro", layout="wide")

st.title("🤖 Sistema de Trading Inteligente")
st.markdown("---")

# --- BARRA LATERAL (Configuración) ---
st.sidebar.header("Configuración del Bot")
activo = st.sidebar.selectbox("Selecciona Activo", ["NVDA", "AAPL", "SPY", "TSLA", "BTC-USD"])
capital_inicial = st.sidebar.number_input("Capital Inicial (USD)", value=10000)

if 'capital' not in st.session_state:
    st.session_state.capital = capital_inicial
    st.session_state.posicion = 0
    st.session_state.historial = []

# --- LÓGICA DE DATOS ---
analizador = AnalizadorTecnico()

def actualizar_datos():
    df = yf.download(activo, period="1d", interval="1m", progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = analizador.calcular_indicadores(df)
    return df

# --- INTERFAZ PRINCIPAL ---
col1, col2, col3 = st.columns(3)

datos = actualizar_datos()
precio_actual = float(datos['Close'].iloc[-1])
rsi_actual = float(datos['RSI'].iloc[-1])
senal = analizador.generar_senal(datos)

# Métricas visuales rápidas
col1.metric("Precio en Vivo", f"${precio_actual:.2f}")
col2.metric("Salud del Mercado (RSI)", f"{rsi_actual:.2f}/100")
col3.metric("Estado del Bot", "ACTIVO", delta="Escaneando")

# --- SEMÁFORO DE DECISIÓN ---
st.subheader("🎯 Decisión del Algoritmo")
if senal == "COMPRA":
    st.success(f"🚀 SEÑAL DE COMPRA DETECTADA: El precio de {activo} está barato (Sobreventa).")
elif senal == "VENTA":
    st.error(f"💰 SEÑAL DE VENTA DETECTADA: El precio de {activo} está caro (Sobrecompra).")
else:
    st.warning("⚖️ NEUTRAL: Esperando el momento oportuno para operar.")

# --- GRÁFICO PROFESIONAL ---
fig = go.Figure()
fig.add_trace(go.Candlestick(x=datos.index, open=datos['Open'], high=datos['High'],
                low=datos['Low'], close=datos['Close'], name="Precio"))
fig.add_trace(go.Scatter(x=datos.index, y=datos['SMA_20'], line=dict(color='orange'), name="Tendencia (SMA)"))
fig.update_layout(title=f"Gráfico de Velas en Tiempo Real: {activo}", xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)

# --- RESUMEN PARA NO EXPERTOS ---
st.info(f"**¿Qué está pasando?** El bot analiza las últimas velas de {activo}. Si el RSI baja de 35, el sistema entiende que hay pánico y compra. Si sube de 65, entiende que hay euforia y vende.")

# Botón para simular trade manual basado en el bot
if st.button("Ejecutar Operación Sugerida"):
    st.balloons()
    st.write("✅ Operación registrada en el libro de contabilidad virtual.")