import numpy as np
import math

class RouteOptimizer:
    def __init__(self):
        pass

    def calculate_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def solve_tsp_nearest_neighbor(self, locations: list):
        """
        locations: list of dicts [{'id': 'depot', 'coords': (0,0)}, {'id': 'A', 'coords': (10,5)}, ...]
        Assumes first location is the start/end point (depot).
        """
        if not locations:
            return []

        unvisited = locations[1:]
        current_loc = locations[0]
        route = [current_loc]
        total_distance = 0

        while unvisited:
            nearest = None
            min_dist = float('inf')
            
            for loc in unvisited:
                dist = self.calculate_distance(current_loc['coords'], loc['coords'])
                if dist < min_dist:
                    min_dist = dist
                    nearest = loc
            
            current_loc = nearest
            route.append(current_loc)
            unvisited.remove(current_loc)
            total_distance += min_dist

        # Return to depot
        dist_to_home = self.calculate_distance(current_loc['coords'], locations[0]['coords'])
        total_distance += dist_to_home
        route.append(locations[0])

        return {
            "optimized_route": [loc['id'] for loc in route],
            "total_distance": round(total_distance, 2),
            "route_details": route
        }
