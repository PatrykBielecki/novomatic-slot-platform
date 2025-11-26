import requests
from typing import Optional

from app.config import MOCKAPI_BASE_URL

class ApiClient:
    def __init__(self, base_url: str = MOCKAPI_BASE_URL):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.last_response: Optional[requests.Response] = None

    def _url(self, path: str) -> str:
        if not path.startswith("/"):
            path = "/" + path
        return self.base_url + path

    def get(self, path: str):
        r = self.session.get(self._url(path), timeout=5)
        self.last_response = r
        return r

    def post(self, path: str, json=None):
        r = self.session.post(self._url(path), json=json, timeout=5)
        self.last_response = r
        return r

    def put(self, path: str, json=None):
        r = self.session.put(self._url(path), json=json, timeout=5)
        self.last_response = r
        return r
