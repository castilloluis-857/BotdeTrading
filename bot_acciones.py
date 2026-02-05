import yfinance as yf
import time
import pandas as pd
from analizador import AnalizadorTecnico


class AccionesBot:
    def __init__(self, activo="NVDA"):
        self.activo = activo
        self.analizador = AnalizadorTecnico()
        self.capital = 10000.0
        self.acciones_poseidas = 0

    def ejecutar_ciclo(self):
        print(f"\n[{time.strftime('%H:%M:%S')}] 📡 Conectando con Yahoo Finance...")

        # Intentamos bajar 5 días para asegurar que haya datos aunque sea fin de semana
        df = yf.download(self.activo, period="5d", interval="1m", progress=False)

        if df.empty:
            print(f"❌ ERROR: No hay datos para {self.activo}. Verifica tu internet o el ticker.")
            return

        # Limpiar columnas (evita el error de MultiIndex)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        print(f"📊 Datos recibidos ({len(df)} filas). Procesando indicadores...")

        df = self.analizador.calcular_indicadores(df)
        senal = self.analizador.generar_senal(df)

        # Extraer valores limpios
        precio_actual = float(df['Close'].iloc[-1])
        rsi_actual = float(df['RSI'].iloc[-1])

        print(f"📈 {self.activo} | Precio: ${precio_actual:.2f} | RSI: {rsi_actual:.2f}")
        print(f"🤖 DECISIÓN: {senal}")

        # Lógica de compra/venta (solo print para demo)
        # Dentro de ejecutar_ciclo, cuando detecta COMPRA:
        if senal == "COMPRA" and self.capital >= precio_actual:
            # Simulamos comprar el máximo posible con nuestro capital
            cant = int(self.capital // precio_actual)
            costo = cant * precio_actual
            self.acciones_poseidas = cant
            self.capital -= costo

            # Guardamos en el CSV
            self.registrar_trade("COMPRA", precio_actual, cant)
            print(f"✅ COMPRA EJECUTADA VIRTUALMENTE: {cant} acciones a ${precio_actual:.2f}")
        elif senal == "VENTA":
            print("💰 SEÑAL DE VENTA DETECTADA")

    def iniciar(self):
        print(f"🤖 BOT INICIADO | Activo: {self.activo} | Capital: ${self.capital}")
        while True:
            self.ejecutar_ciclo()
            print(f"😴 Esperando actualización...", end="")
            for _ in range(10):
                time.sleep(6)  # Total 60 segundos
                print(".", end="", flush=True)
            print("\n")


if __name__ == "__main__":
    bot = AccionesBot(activo="NVDA")
    bot.iniciar()