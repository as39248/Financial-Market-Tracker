from datetime import date, datetime, timedelta
import pandas as pd
import pmdarima as pm
import matplotlib.pyplot as plt
from utils.api import get_polygon_client


client = get_polygon_client()

def create_df(ticker):

    close_prices = []
    dates = []

    yesterday = date.today() - timedelta(1)
    start_date = yesterday - timedelta(730)
    
    for a in client.list_aggs(
        ticker,
        1,
        "day",
        start_date,
        yesterday,
        limit=50000,
    ):
        close_prices.append(a.close)
   
        # Convert the timestamp to datetime
        close_date = datetime.fromtimestamp(a.timestamp / 1000)
        dates.append(close_date)
       
    df = pd.DataFrame({
        "Date": dates,
        "Price": close_prices
    })
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    return df


def make_time_series(ticker):
    # Historical Series 
    df = create_df(ticker)
    last_date = df.index[-1]
    forecast_index = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=30, freq='D')
    
    # ARIMA Forecast 
    arima_model = pm.auto_arima(df["Price"], seasonal=True, 
                        suppress_warnings=True, stepwise=True)
    arima_forecast = arima_model.predict(n_periods=30)
    arima = pd.DataFrame({
        "Date": forecast_index,
        "Price": arima_forecast
    })

    arima["Date"] = pd.to_datetime(arima["Date"])
    arima.set_index("Date", inplace=True)

    # plot
    plt.ion() 
    plt.figure(figsize=(10, 5))
    plt.plot(df, label="Historical")
    plt.plot(arima, label="Forecast", linestyle='--')
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"{ticker} Price Forecast")
    plt.legend()
    plt.tight_layout()
    plt.show()
    




