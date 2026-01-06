import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import warnings

warnings.filterwarnings("ignore")

class DemandForecaster:
    def __init__(self):
        pass

    def forecast(self, historical_data: list, periods: int = 7):
        """
        Forecast using Holt-Winters Exponential Smoothing.
        historical_data: list of values (ordered by time)
        """
        if len(historical_data) < 10:
            return {"error": "Not enough data for forecasting (min 10 points required)"}

        data = pd.Series(historical_data)
        
        # Simple Exponential Smoothing (Holt-Winters)
        # In a real scenario, we'd check for seasonality and trend
        model = ExponentialSmoothing(data, trend='add', seasonal=None).fit()
        forecast = model.forecast(periods)
        
        return {
            "historical_last_5": historical_data[-5:],
            "forecast": forecast.tolist(),
            "model": "Exponential Smoothing (Holt-Winters)"
        }
