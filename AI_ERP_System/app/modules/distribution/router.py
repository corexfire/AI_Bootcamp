from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Tuple

from app.modules.distribution.route_optimization.solver import RouteOptimizer
from app.modules.distribution.demand_prediction.forecaster import DemandForecaster
from app.modules.distribution.inventory.manager import InventoryManager

router = APIRouter()

# Schemas
class Location(BaseModel):
    id: str
    coords: Tuple[float, float]

class RouteRequest(BaseModel):
    locations: List[Location]

class ForecastRequest(BaseModel):
    historical_data: List[float]
    periods: int = 7

class InventoryItem(BaseModel):
    sku: str
    unit_cost: float
    annual_demand: float

class ABCRequest(BaseModel):
    items: List[InventoryItem]

# Instances
route_optimizer = RouteOptimizer()
forecaster = DemandForecaster()
inventory_manager = InventoryManager()

@router.post("/optimize-route")
def optimize_route(data: RouteRequest):
    # Convert Pydantic models to dicts
    locations_dict = [loc.model_dump() for loc in data.locations]
    return route_optimizer.solve_tsp_nearest_neighbor(locations_dict)

@router.post("/forecast-demand")
def forecast_demand(data: ForecastRequest):
    return forecaster.forecast(data.historical_data, data.periods)

@router.post("/abc-analysis")
def abc_analysis(data: ABCRequest):
    items_dict = [item.model_dump() for item in data.items]
    return inventory_manager.abc_analysis(items_dict)
