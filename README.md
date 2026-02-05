# 📈 TradingBot Pro: Sistema de Análisis Algorítmico en Tiempo Real

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/UI-Streamlit-FF4B4B)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Descripción General
Este proyecto es un **Bot de Trading Algorítmico** desarrollado en Python, diseñado para el análisis técnico de acciones, ETFs y Criptomonedas en tiempo real. Utiliza una arquitectura desacoplada para separar el procesamiento de señales financieras de la interfaz de usuario.

El sistema implementa una estrategia de **Reversión a la Media** basada en el Índice de Fuerza Relativa (RSI), permitiendo identificar puntos críticos de sobrecompra y sobreventa para la toma de decisiones financieras automatizadas.

---

## 📸 Demostración Visual

### Dashboard Principal
<p alig="center">
<img width="1901" height="834" alt="image" src="https://github.com/user-attachments/assets/a7c34be1-0642-40c5-baa1-171e30ae61e0" />
</p>
> *Interfaz interactiva mostrando el gráfico de velas y el estado actual de la estrategia.*
---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Datos:** `yfinance` (Yahoo Finance API)
* **Procesamiento de Datos:** `pandas` (Cálculo vectorial de indicadores)
* **Visualización:** `plotly` (Gráficos interactivos de velas japonesas)
* **Dashboard:** `streamlit` (Interfaz web reactiva)

## 🧠 Lógica del Algoritmo
El bot utiliza un motor técnico que calcula:
1.  **RSI (Relative Strength Index):** Período de 14 minutos para detectar momentum.
2.  **SMA (Simple Moving Average):** Período de 20 para identificar la tendencia primaria.

**Criterios de Operación:**
- **SEÑAL DE COMPRA:** RSI < 30 (Activo infravalorado/Pánico).
- **SEÑAL DE VENTA:** RSI > 70 (Activo sobrevalorado/Euforia).

## 🚀 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/BotdeTrading.git](https://github.com/tu-usuario/BotdeTrading.git)
   cd BotdeTrading
