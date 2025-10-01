import json, os, time, math, random
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class FlowScoreResponse:
    symbol: str
    score: float
    components: Dict[str, float]
    timestamp: float

@dataclass
class WhaleEvent:
    wallet: str
    side: str           # 'buy' or 'sell'
    amount: float       # in SOL
    tx: str
    timestamp: float

class OctoFlow:
    """Lightweight client reading from the mock API (file-based or HTTP in the future)."""
    def __init__(self, api_key: str = None, base_url: str = None, mock_dir: str = None):
        self.api_key = api_key or os.environ.get("OCTOFLOW_API_KEY", "DEMO")
        self.base_url = base_url or "http://localhost:5812"
        self.mock_dir = mock_dir or os.environ.get("OCTOFLOW_MOCK_DIR", "data/samples")

    # For demo we read JSON files. In prod, replace with real HTTP calls.
    def _load(self, name: str) -> Any:
        path = os.path.join(self.mock_dir, f"{name}.json")
        with open(path, "r") as f:
            return json.load(f)

    def flow_score(self, symbol: str) -> FlowScoreResponse:
        data = self._load(f"flowscore_{symbol.upper()}")
        return FlowScoreResponse(
            symbol=symbol.upper(),
            score=data["score"],
            components=data["components"],
            timestamp=time.time()
        )

    def whales(self, symbol: str) -> List[WhaleEvent]:
        data = self._load(f"whales_{symbol.upper()}")
        events = []
        for d in data["events"]:
            events.append(WhaleEvent(**d))
        return events

    def liquidity(self, symbol: str) -> Dict[str, float]:
        return self._load(f"liquidity_{symbol.upper()}")

    def social(self, symbol: str) -> Dict[str, float]:
        return self._load(f"social_{symbol.upper()}")
