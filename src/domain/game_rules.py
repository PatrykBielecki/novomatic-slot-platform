HOUSE_EDGE = 0.10

def calculate_casino_profit(total_pot: float) -> float:
    return round(total_pot * HOUSE_EDGE, 2)
