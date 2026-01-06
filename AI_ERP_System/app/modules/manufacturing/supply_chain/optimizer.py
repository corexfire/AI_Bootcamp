import pandas as pd
import numpy as np

class SupplyChainOptimizer:
    def __init__(self):
        pass

    def optimize_reorder_point(self, daily_usage: list, lead_time_days: int, service_level_z: float = 1.645):
        """
        Calculate Reorder Point (ROP) and Safety Stock.
        ROP = (Average Daily Usage * Lead Time) + Safety Stock
        Safety Stock = Z * std_dev_usage * sqrt(Lead Time)
        
        service_level_z: 1.645 for 95% service level
        """
        usage_array = np.array(daily_usage)
        avg_usage = np.mean(usage_array)
        std_dev_usage = np.std(usage_array)
        
        safety_stock = service_level_z * std_dev_usage * np.sqrt(lead_time_days)
        reorder_point = (avg_usage * lead_time_days) + safety_stock
        
        return {
            "average_daily_usage": float(avg_usage),
            "safety_stock": float(safety_stock),
            "reorder_point": float(reorder_point),
            "recommendation": f"Reorder when inventory drops below {int(reorder_point)} units"
        }

    def forecast_demand_simple(self, historical_data: list, periods: int = 30):
        """
        Simple Moving Average forecast for demonstration.
        """
        df = pd.DataFrame(historical_data, columns=['demand'])
        # Simple moving average of last 7 days
        forecast = df['demand'].rolling(window=7).mean().iloc[-1]
        
        return {
            "predicted_demand_next_period": float(forecast),
            "method": "7-day Moving Average"
        }
