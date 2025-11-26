from domain.models import Player, Round
from infrastructure.api_client import ApiClient

class UserRepository:
    def __init__(self, client: ApiClient):
        self.client = client

    def list_users(self):
        r = self.client.get("/users")
        r.raise_for_status()
        data = r.json()
        return [
            Player(
                id=u["id"],
                name=u["name"],
                balance=float(u["balance"]),
                initial_balance=float(u.get("initial_balance", u["balance"])),
                bonus_spins=int(u.get("bonus_spins", 0)),
            )
            for u in data
        ]

    def get_by_id(self, user_id: str):
        r = self.client.get(f"/users/{user_id}")
        r.raise_for_status()
        u = r.json()
        return Player(
            id=u["id"],
            name=u["name"],
            balance=float(u["balance"]),
            initial_balance=float(u.get("initial_balance", u["balance"])),
            bonus_spins=int(u.get("bonus_spins", 0)),
        )

    def update_balance(self, user_id: str, new_balance: float):
        r = self.client.put(f"/users/{user_id}", json={"balance": new_balance})
        r.raise_for_status()


class RoundRepository:
    def __init__(self, client: ApiClient):
        self.client = client

    def save_round(self, data):
        r = self.client.post("/rounds", json=data)
        r.raise_for_status()
        d = r.json()
        return Round(
            id=d["id"],
            player_id=d["player_id"],
            bet_amount=float(d["bet_amount"]),
            win_amount=float(d["win_amount"]),
            casino_profit=float(d["casino_profit"]),
        )
