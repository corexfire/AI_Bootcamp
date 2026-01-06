import pandas as pd

class InventoryManager:
    def __init__(self):
        pass

    def abc_analysis(self, items: list):
        """
        Perform ABC Analysis on inventory.
        items: list of dicts [{'sku': 'A1', 'unit_cost': 100, 'annual_demand': 500}, ...]
        """
        df = pd.DataFrame(items)
        df['annual_value'] = df['unit_cost'] * df['annual_demand']
        
        # Sort by value
        df = df.sort_values('annual_value', ascending=False)
        
        # Calculate cumulative percentage
        df['cumulative_value'] = df['annual_value'].cumsum()
        total_value = df['annual_value'].sum()
        df['cumulative_percentage'] = (df['cumulative_value'] / total_value) * 100
        
        # Assign Categories
        # A: Top 80% value
        # B: Next 15% (80-95%)
        # C: Bottom 5% (95-100%)
        
        def assign_class(cum_pct):
            if cum_pct <= 80:
                return 'A'
            elif cum_pct <= 95:
                return 'B'
            else:
                return 'C'
        
        df['category'] = df['cumulative_percentage'].apply(assign_class)
        
        return df[['sku', 'annual_value', 'category']].to_dict(orient='records')
