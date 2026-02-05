import pandas as pd


class AnalizadorTecnico:
    def calcular_indicadores(self, df):
        # Media Móvil Simple (SMA) para ver la tendencia
        df['SMA_20'] = df['Close'].rolling(window=20).mean()

        # RSI Manual (Indispensable para saber si está caro o barato)
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        return df

    def generar_senal(self, df):
        df = self.calcular_indicadores(df)
        if len(df) < 20:  # Necesitamos al menos 20 datos para la media móvil
            return "ESPERANDO DATOS"

        # Extraemos la última fila
        ultima = df.iloc[-1]

        # Usamos .item() o float() para convertir a un número simple y evitar el error de Series
        try:
            val_rsi = float(ultima['RSI'].iloc[0]) if isinstance(ultima['RSI'], pd.Series) else float(ultima['RSI'])

            if val_rsi < 30: # 35
                return "COMPRA"
            elif val_rsi > 70: # 65
                return "VENTA"
        except Exception as e:
            print(f"Error procesando señal: {e}")

        return "NEUTRAL"