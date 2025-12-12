from dataclasses import dataclass

@dataclass
class Player:
    player_id: str
    name: str
    balance: float
    initial_balance: float
    bonus_spins: int = 0

    def has_active_bonus(self) -> bool:
        return self.bonus_spins > 0 
    
    def bonus_spins_remaining(self) -> int:
        return self.bonus_spins


class SpinResult:
    def __init__(self, bet_amount: float, win_amount: float, balance_before: float,
                 balance_after: float, used_bonus: bool):
        self.bet_amount = bet_amount
        self.win_amount = win_amount
        self.balance_before = balance_before
        self.balance_after = balance_after
        self.used_bonus = used_bonus

    def __repr__(self):
        return (
            f"SpinResult(bet_amount={self.bet_amount}, win_amount={self.win_amount}, "
            f"balance_before={self.balance_before}, balance_after={self.balance_after}, "
            f"used_bonus={self.used_bonus})"
        )


class Round:
    def __init__(self, id: str | None, player_id: str,
                 bet_amount: float, win_amount: float, casino_profit: float):
        self.id = id
        self.player_id = player_id
        self.bet_amount = bet_amount
        self.win_amount = win_amount
        self.casino_profit = casino_profit

    def __repr__(self):
        return (
            f"Round(id={self.id}, player_id={self.player_id}, bet_amount={self.bet_amount}, "
            f"win_amount={self.win_amount}, casino_profit={self.casino_profit})"
        )
