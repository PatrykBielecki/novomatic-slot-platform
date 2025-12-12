from infrastructure.api_client import ApiClient
from infrastructure.repositories import UserRepository, RoundRepository
from application.services import GameService

class GameController:
    def __init__(self, client: ApiClient | None = None):
        client = client or ApiClient()
        self.user_repo = UserRepository(client)
        self.round_repo = RoundRepository(client)
        self.game_service = GameService(self.user_repo, self.round_repo)

    def list_players(self):
        return self.user_repo.list_users()

    def get_player(self, pid):
        return self.user_repo.get_by_id(pid)

    def find_player_with_min_balance(self, amount: float):
        for p in self.list_players():
            if p.balance >= amount:
                return p
        raise RuntimeError("No player with sufficient balance")

    def find_player_with_balance_lower_than(self, amount: float):
        for p in self.list_players():
            if p.balance < amount:
                return p
        raise RuntimeError("No player with low enough balance")

    def make_cash_spin(self, pid, bet):
        return self.game_service.make_cash_spin(pid, bet)

    def make_bonus_spin(self, pid, bet):
        return self.game_service.make_bonus_spin(pid, bet)

