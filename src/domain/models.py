from dataclasses import dataclass

@dataclass
class Player:
    id: str
    name: str
    balance: float
    initial_balance: float
    bonus_spins: int = 0

@dataclass
class SpinResult:
    bet_amount: float
    win_amount: float
    balance_before: float
    balance_after: float
    used_bonus: bool

@dataclass
class Round:
    id: str | None
    player_id: str
    bet_amount: float
    win_amount: float
    casino_profit: float
