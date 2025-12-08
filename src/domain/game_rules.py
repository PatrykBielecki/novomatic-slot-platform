from app.config import HOUSE_EDGE

def calculate_casino_profit(total_pot: float) -> float:
    return round(total_pot * HOUSE_EDGE, 2)
