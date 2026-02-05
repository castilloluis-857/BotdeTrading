import pandas as pd
import plotly.express as px
import streamlit as st


def generar_grafica_rendimiento():
    try:
        # 1. Leer el historial generado por el bot
        df = pd.read_csv("historial_trades.csv")

        # 2. Calcular el valor total del portfolio (Capital + Valor de acciones)
        # Para simplificar el reporte, graficaremos el Capital Restante tras cada trade
        fig = px.line(df, x="Fecha", y="Capital_Restante",
                      title="📈 Evolución del Capital (Equity Curve)",
                      markers=True,
                      line_shape="hv")  # Gráfica de pasos (ideal para trades)

        fig.update_layout(xaxis_title="Tiempo", yaxis_title="Balance USD")
        return fig
    except FileNotFoundError:
        return None


# Si quieres verlo por separado en Streamlit
if __name__ == "__main__":
    st.title("📊 Reporte de Performance del Bot")
    grafica = generar_grafica_rendimiento()
    if grafica:
        st.plotly_chart(grafica)
    else:
        st.warning("Aún no hay trades registrados en 'historial_trades.csv'")