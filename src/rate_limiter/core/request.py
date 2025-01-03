from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class RateLimitRequest:
    id: str
    timestamp: float
    client_ip: str
    path: str
    method: str
    metadata: Dict[str, Any] = None
