import random
from domain.models import SpinResult
from domain.game_rules import calculate_casino_profit

class GameService:
    def __init__(self, users, rounds):
        self.users = users
        self.rounds = rounds

    def make_cash_spin(self, player_id: str, bet_amount: float) -> SpinResult:
        player = self.users.get_by_id(player_id)

        if player.balance < bet_amount:
            raise ValueError("Insufficient funds")
        elif bet_amount <= 0:
            raise ValueError("Bet amount must be > 0")
        # zakładamy maksymalny zakład 1000 jednostek
        elif bet_amount > 1000:
            raise ValueError("Bet amount exceeds maximum limit")
        elif bet_amount != round(bet_amount, 2):
            raise ValueError("Bet amount must have at most two decimal places")

        balance_before = player.balance
        win_amount = round(random.uniform(0, 3) * bet_amount, 2)
        balance_after = balance_before - bet_amount + win_amount

        self.users.update_balance(player_id, balance_after)

        self.rounds.save_round({
            "player_id": str(player_id),
            "bet_amount": float(bet_amount),
            "win_amount": float(win_amount),
            "casino_profit": float(calculate_casino_profit(bet_amount)), 
        })

        return SpinResult(
            bet_amount=bet_amount,
            win_amount=win_amount,
            balance_before=balance_before,
            balance_after=balance_after,
            used_bonus=False,
        )

    def make_bonus_spin(self, player_id: str, bet_amount: float) -> SpinResult:
        player = self.users.get_by_id(player_id)

        if player.balance < bet_amount:
            raise ValueError("Insufficient funds")
        elif bet_amount <= 0:
            raise ValueError("Bet amount must be > 0")
        # zakładamy maksymalny zakład 1000 jednostek
        elif bet_amount > 1000:
            raise ValueError("Bet amount exceeds maximum limit")
        elif bet_amount != round(bet_amount, 2):
            raise ValueError("Bet amount must have at most two decimal places")
        
        if not player.has_active_bonus:
            raise ValueError("Player does not have an active bonus") 
        elif player.bonus_spins_remaining <= 0:
            raise ValueError("No bonus spins remaining for player") 
        

        balance_before = player.balance
        win_amount = round(random.uniform(0, 3) * bet_amount, 2)
        balance_after = balance_before + win_amount

        self.users.update_balance(player_id, balance_after)

        self.rounds.save_round({
            "player_id": player_id,
            "bet_amount": 0.0,
            "win_amount": win_amount,
            "casino_profit": 0.0,
        })

        return SpinResult(
            bet_amount=bet_amount,
            win_amount=win_amount,
            balance_before=balance_before,
            balance_after=balance_after,
            used_bonus=True,
        )
