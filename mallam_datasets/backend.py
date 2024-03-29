import os
from typing import Optional, Dict

import requests


class BackendService:
    def __init__(self, url: Optional[str] = None, secret_key: Optional[str] = None):
        if not url:
            url = os.getenv("BACKEND_URL")
        if not url:
            url = "https://api.mallam.ai"
        if not secret_key:
            secret_key = os.getenv("SECRET_KEY")

        self.url = url.rstrip("/")
        self.secret_key = secret_key

    def invoke(self, action: str, **kwargs) -> Dict:
        res = requests.post(
            f"{self.url}/invoke/{action}",
            headers={"X-Secret-Key": self.secret_key},
            json=kwargs,
        )
        if res.status_code != 200:
            raise Exception(res.text)
        return res.json()
